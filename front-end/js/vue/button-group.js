;(function() {
    'use strict';

    Vue.component('button-group', {
        template: '#tmpl-button-group',
        props: {
            activeClass: {
                default: 'active'
            },
            state: Object
        },
        data: function() {
            return {}
        },
        methods: {
            change: function(identifier) {
                this.setCurrentlyActive(identifier);
            },
            setCurrentlyActive: function(identifier) {
                this.state.setCurrentlyActive(identifier);
                this.$emit('change', identifier);
                localStorage.setItem('currentlyActive', identifier);
            }
        },
        activate: function(done) {
            if (this.currentlyActive) {
                this.setCurrentlyActive(this.currentlyActive);
            }

            if (localStorage.getItem('currentlyActive')) {
                this.setCurrentlyActive(localStorage.getItem('currentlyActive'));
            }

            done();
        }
    });

    Vue.component('button-item', {
        template: '#tmpl-button-item',
        props: {
            identifier: null
        },
        computed: {
            isSelected: function() {
                return this.identifier == this.$parent.state.currentlyActive;
            },
            classesActive: function() {
                var temp = {};
                temp[this.$parent.activeClass] = this.isSelected;
                return temp;
            }
        },
        methods: {
            selected: function(event) {
                this.$parent.change(this.identifier)
            }
        }
    });
})();