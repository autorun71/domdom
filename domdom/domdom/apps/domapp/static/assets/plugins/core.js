var tplOptions = {
    browserWidth: document.documentElement.clientWidth
}

window.onresize = function() {
    tplOptions.browserWidth = document.documentElement.clientWidth;
    headerReplacements();
    categoriesSlider();
    newsGrid();
}

window.onload = function() {
    headerReplacements();
    categoriesSlider();
    newsGrid();
}



/* =============================================== */
/* Перемещение элементов в адаптиве
/* =============================================== */
function replaceFirstDomElement(from, to) {
    var fromWrap = document.getElementById(from);
        
    if( fromWrap.children.length ) {
        var getDomNode = fromWrap.firstElementChild;
        var newDomNode = getDomNode.cloneNode(true);

        getDomNode.remove();
        document.getElementById(to).appendChild(newDomNode);
    }
}
function headerReplacements() {
    if( tplOptions.browserWidth < 769 ) {
        replaceFirstDomElement('main-nav', 'mobile-nav-holder');
        replaceFirstDomElement('js-user-holder', 'js-m-user-holder');
        replaceFirstDomElement('js-cart-holder', 'js-m-cart-holder');
    }
    else {
        replaceFirstDomElement('mobile-nav-holder', 'main-nav');
        replaceFirstDomElement('js-m-user-holder', 'js-user-holder');
        replaceFirstDomElement('js-m-cart-holder', 'js-cart-holder');
    }
}



/* =============================================== */
/* Открыть/закрыть мобильное меню
/* =============================================== */
$(document).on('click', '.nav-toggle', function() {
    var btn = $(this);
    var mobNav = $('#mobile-nav-holder');
    
    if( btn.hasClass('active') ) {
        btn.removeClass('active');
        mobNav.removeClass('active');
        $('body').removeClass('overflow');
    }
    else {
        btn.addClass('active');
        mobNav.addClass('active');
        $('body').addClass('overflow');
    }
})



/* =============================================== */
/* Меню каталога
/* =============================================== */
$(document).on('click', 'a.top-nav__catalog-link', function(e) {
    if( tplOptions.browserWidth < 992 ) {
        e.preventDefault();
        
        var btn = $(this);
        var nav = btn.next('ul');
        
        if( btn.hasClass('active') ) {
            nav.stop(true, true).slideUp(200, function() {
                nav.removeAttr('style');
            });
            btn.removeClass('active');
        }
        else {
            nav.stop(true, true).slideDown(200);
            btn.addClass('active');
        }
    }
})



/* =============================================== */
/* Слайдеры
/* =============================================== */
$(function() {
    if( $('#main-slider').length ) {
        $('#main-slider').slick({
            autoplay : true,
            centerPadding : 0,
            dots : true,
            prevArrow : '<button type="button" class="slick-prev"></button>',
            nextArrow : '<button type="button" class="slick-next"></button>',
        });
    }
    
    if( $('.slider-runner').length ) {
        $('.slider-runner').each(function() {
            var controlsWrap = $(this).prev('.headline').children('.slider_controls');
            
            $(this).slick({
                autoplay : true,
                centerPadding : 0,
                dots : false,
                arrows : true,
                appendArrows : controlsWrap,
                prevArrow : '<button type="button" class="slick-prev"></button>',
                nextArrow : '<button type="button" class="slick-next"></button>',
            });
        })
    }
    
    categoriesSlider();
})
function categoriesSlider() {
    if( $('.category-slider-runner').length ) {
        if( tplOptions.browserWidth < 510 ) {
            $('.category-slider-runner').each(function() {
                $(this).slick({
                    autoplay : false,
                    centerPadding : 0,
                    slidesToShow : 1,
                    adaptiveHeight : true,
                    infinite : false,
                    dots : true,
                    arrows : false,
                    //appendArrows : controlsWrap,
                    prevArrow : '<button type="button" class="slick-prev"></button>',
                    nextArrow : '<button type="button" class="slick-next"></button>',
                });
            });
        }
        else {
            $('.category-slider-runner.slick-initialized').each(function() {
                $(this).slick('unslick');
            })
        }
    }
}



/* =============================================== */
/* Template UI: Tabs
/* =============================================== */
$(document).on('click', '.tpl_ui_tabs .tabs a', function(e) {
    e.preventDefault();
    
    var select = $(this);
    var tab = select.attr('href');
    var tabs = select.parents('.tabs')
    var tabsContent = tabs.next('.tabs_content')
    
    $('.active', tabs).removeClass('active');
    $('.active', tabsContent).removeClass('active');
    $(tab, tabsContent).addClass('active');
    $(select).addClass('active');
})



/* =============================================== */
/* Выравнивание в /catalog/
/* =============================================== */
function setTopCategoryHeight() {
    if( $('.catalog_categories').length ) {
        if( tplOptions.browserWidth >= 450 ) {
            var h = 0;

            $('.catalog_categories .top_category-list').each(function() {
                var currentHeight = $(this).height();
                h = currentHeight > h ? currentHeight : h;
            })
            $('.top_category-list').height(h);
            console.log('set');
        }
        else {
            $('.top_category-list').removeAttr('style');
            console.log('rmv');
        }
    }
}
$(function() {
    setTopCategoryHeight();
})
$(window).resize(function() {
    setTopCategoryHeight();
})



/* =============================================== */
/* Фильтр товаров
/* =============================================== */
$(document).on('click', '.catalog_filter .filter_block-header', function() {
    var spd = 250;
    var state = $(this).data('state');
    var header = $(this);
    
    if( state == 0 ) {
        header.data('state', 1).addClass('active').next('.filter_block-params').slideDown(spd);
    }
    else {
        header.data('state', 0).removeClass('active').next('.filter_block-params').slideUp(spd);
    }
})

$(document).on('click', '.catalog_filter .hidden-opener span', function() {
    var spd = 250;
    var btn = $(this).parents('.hidden-opener');
    
    if( btn.data('state') == 0 ) {
        btn.data('state', 1).prev('.hidden').slideDown(spd);
        $(this).text('Скрыть');
    }
    else {
        btn.data('state', 0).prev('.hidden').slideUp(spd);
        $(this).text('Показать еще');
    }
})

$(document).on('click', '.filter-close', function() {
    var filter = $(this).parents('#filter_holder');
    var filterWidnth = filter.outerWidth();
    
    filter.animate({'left' : '-' + filterWidnth + 'px'}, 250, function() {
        $(this).data('state', 0);
        $('body').removeClass('overflow');
    });
})

$(document).on('click', '.filter-show', function() {
    var filter = $('#filter_holder');
    var filterWidnth = filter.outerWidth();
    
    if( filter.data('state') != 1 ) {
        $('body').addClass('overflow');
        filter.data('state', 1).css({'left' : '-' + filterWidnth + 'px'}).animate({'left' : '0px'}, 250);
    }
})
$(document).on('change', '.catalog_sorter_mobile', function() {
    location = $(this).val();
})



/* =============================================== */
/* Карточка товара
/* =============================================== */
$(document).on('click', '.show_hidden_params', function() {
    var btn = $(this);
    var tbl = btn.prev('.params_table');
    
    if( $('.hidden', tbl).length ) {
        $('.hidden', tbl).addClass('opened').removeClass('hidden');
        btn.text('Закрыть');
    }
    else {
        $('.opened', tbl).addClass('hidden').removeClass('opened');
        btn.text('Все характеристики');
    }
})



/* =============================================== */
/* Доставка по России
/* =============================================== */
var default_city = 'Тула'; // Здесь надо указать город, который определит (или который задан вручную), модулем геопозиции в шапке

function changeDeliveryMap(city) {
    cityName = default_city;
    
    if( city != undefined ) {
        cityName = city;
    }

    $.ajax({
        type : 'post',
        dataType : 'json',
        url : '/pickup_points.php',
        data : {
            action: 'get_points_by_city',
            city: cityName,
        },
        beforeSend: function() {
            $('#pickup_map').html('').slideDown(250);
            $('#pickup_points-list').html('hidden').slideDown(250);
        },
        success: function(data) {
            if( data.length ) {

                ymaps.ready(function() {
                    $('#pickup_points-list').html('<ul></ul>');

                    var myMap;
                    var pointsList = $('#pickup_points-list ul');

                    ymaps.geocode('Россия, ' + cityName, {
                        results: 1
                    }).then(function (res) {
                        var firstGeoObject = res.geoObjects.get(0);
                        cityCoords = firstGeoObject.geometry.getCoordinates();

                        myMap = new ymaps.Map("pickup_map", {
                            center: cityCoords,
                            zoom: 11
                        });

                        data.forEach(function(point, i) {
                            ymaps.geocode('Россия, ' + point.address, {
                                results: 1
                            }).then(function (res) {
                                var firstGeoObject = res.geoObjects.get(0);
                                coords = firstGeoObject.geometry.getCoordinates();

                                placemark = new ymaps.Placemark(coords, {
                                    hintContent: point.address,
                                    balloonContent: point.address + '<br>' + point.worktime + '<br>' + point.phone + '<br>Курьерская доставка: ' + point.courier_available,
                                });

                                myMap.geoObjects.add(placemark);

                                var pickupItem = '<li>';
                                    pickupItem += '<div>';
                                        pickupItem += '<strong class="address">' + point.address + '</strong>';
                                    pickupItem += '</div>';

                                    pickupItem += '<div>';
                                        pickupItem += '<strong>Режим работы:</strong> ' + point.worktime;
                                    pickupItem += '</div>';

                                    pickupItem += '<div>';
                                        pickupItem += '<strong>Телефон:</strong> ' + point.phone;
                                    pickupItem += '</div>';

                                    pickupItem += '<div>';
                                        pickupItem += '<strong>Курьерская доставка:</strong> ' + point.courier_available;
                                    pickupItem += '</div>';
                                pickupItem += '</li>';

                                pointsList.append(pickupItem);
                                
                                $('#pickup_map').removeClass('hidden');
                                $('#pickup_points-list').removeClass('hidden');
                            })
                        })
                    });
                })
            }
        },
        error: function() {
            alert('Ошибка запроса. Попробуйте позже');
        },
    });
}
$(function() {
    if( $('#delivery-pickups').length ) {
        $.ajax({
            type : 'post',
            dataType : 'json',
            url : '/pickup_points.php',
            data : {
                action: 'list',
                default_city: default_city,
            },
            success: function(data) {
                if( data.length ) {
                    var list = '<option disabled selected>Выберите город доставки</option>';

                    data.forEach(function(name, i) {
                        if( name == default_city ) {
                            list += '<option selected>' + name + '</option>';
                            changeDeliveryMap();
                        }
                        else {
                            list += '<option>' + name + '</option>';
                        }
                    })
                    $('#pickup_cities_list').append(list);
                    $('#pickup_cities_list').parents('.pickup_map-selector').removeClass('hidden');
                }
            },
            error: function() {
                console.log('Ошибка запроса городов.');
            }
        });
    }
});
$(document).on('change', '#pickup_cities_list', function() {
    changeDeliveryMap($(this).val());
})



/* =============================================== */
/* Пункты самовывоза
/* =============================================== */
$(document).on('click', '.local_stores .opener', function() {
    var stores = $(this).parents('.local_stores');
    var opener = $(this);
    
    if( opener.hasClass('active') ) {
        opener.removeClass('active').next('.store_details').stop(true, true).slideUp(250);
    }
    else {
        $('.active', stores).removeClass('active').next('.store_details').stop(true, true).slideUp(250);;
        opener.addClass('active').next('.store_details').stop(true, true).slideDown(250);
    }
})



/* =============================================== */
/* Сетка новостей
/* =============================================== */
function newsGrid() {
    if( $('.masonry-grid').length ) {
        if( tplOptions.browserWidth >= 1200 ) {
            $('.masonry-grid').masonry({
                itemSelector: '.grid-item',
                columnWidth: 270,
                gutter: 30
            })
        }
        else {
            $('.masonry-grid').masonry('destroy');
        }
    }
}