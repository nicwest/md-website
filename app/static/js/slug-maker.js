/**
 * Created with PyCharm.
 * User: nic
 * Date: 16/02/14
 * Time: 17:47
 * To change this template use File | Settings | File Templates.
 */


(function ($) {
	'use strict';

	$.fn.slugMaker = function (target) {
        var slugParent = this,
            slugTarget = target,
            makeSlug = function () {
            var current = $(slugParent).val().toLowerCase();
            var slug = current.replace(/[^a-z0-9]/gi, "-");
            $(slugTarget).val(slug);
        };

        $(slugParent).bind('change', function(){
            makeSlug();
        });

		return this;
    };
}(window.jQuery));