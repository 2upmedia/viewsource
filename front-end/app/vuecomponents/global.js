'use strict';

var Vue = require('vue');
var VueResource = require('vue-resource');
var $ = require('jquery');
var hljs = require('highlight.js');

Vue.use(VueResource);

Vue.config.delimiters = ['${', '}'];
Vue.config.unsafeDelimiters = ['{!!', '!!}'];

Storage.prototype._setItem = localStorage.setItem;
Storage.prototype._getItem = localStorage.getItem;

localStorage.setItem = function (key, data) {
    return this._setItem(key, JSON.stringify(data));
};

localStorage.getItem = function (key) {
    return JSON.parse(this._getItem(key));
};

window.store = {
    state: {
        currentlyActive: 'noWrap',
        setCurrentlyActive: function(identifier) {
            this.currentlyActive = identifier;
        }
    }
};

Object.freeze(window.store);

new Vue({
    el: 'body',
    data: {
        url: null,
        code: 'No source code yet',
        state: store.state
    },
    methods: {
        getURL: function() {
            var that = this;
            this.$http.get('http://api.viewsourceit.local/sources', {params: {url: this.url}}).then(
                function(response) {
                    console.log(response);
                    if (response.data.data) {
                        that.code = response.data.data.attributes.source_code;

                        // setInterval(() => hljs.initHighlighting($('pre code')), 300); // TODO: seems like highlight destroys vue watches
                    }
                },
                function(response) {
                    that.code = response.data.errors[0].detail;
                }
            )
        }
    }
});

Vue.http.interceptors.push(function(request, next) {
    next(function(response) {
        if (response.headers['Content-Type'] == 'application/vnd.api+json') {
            response.data = JSON.parse(response.data);
        }
    });
});
