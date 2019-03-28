var loadingService = angular.module('loadingService', [])
    .service('loadingService', function ($rootScope) {

        var loadingService = this;

        loadingService.create_loader = function(text) {
            var loadingWrapperEle = document.createElement('div');
            loadingWrapperEle.setAttribute('id', 'loadingWrapper')
            loadingWrapperEle.setAttribute('class', 'loading-wrapper')

            var loadingModalEle = document.createElement('div', {
                'id': 'loadingModal',
                'class': 'loading-modal'
            });
            loadingModalEle.setAttribute('id', 'loadingModal')
            loadingModalEle.setAttribute('class', 'loading-modal')

            var loadingBar = document.createElement('div', {
                'class': 'loading-bar'
            });
            loadingBar.setAttribute('class', 'loading-bar')
            
            var loadingText = document.createElement('div', {
                'class': 'loading-text'
            });
            loadingText.setAttribute('class', 'loading-text')

            loadingText.textContent = text;

            loadingModalEle.appendChild(loadingBar)
            loadingModalEle.appendChild(loadingText)
            loadingWrapperEle.appendChild(loadingModalEle);
            document.body.appendChild(loadingWrapperEle);

            return loadingWrapperEle
        }

        loadingService.remove_loader = function(ele) {
            document.body.removeChild(ele);
            return 'bye bye'
        }

    });