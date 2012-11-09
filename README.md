#App wide messages for Django

## Install
Add the app to ```settings.py```
```
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'says',
    'myapp',
)
```

## Configure
Says comes with a default close action. It is attached to the close button in the ```notifications div```. You can override it in your ```settings.py```. 
```
USE_DEFAULT_CLOSE = False 
```
Once you've disable that you can simply attach whatever ```close``` action you want by binding an click handler to ```#says-close-btn```.

## Using it in template
Add the nessary code to your template. You'll need to load the ```says``` template tags.
```
{%load says_extras%}
<html>
<head>
        <title>
		My sweet Django App
        </title>
</head>
<body>
{%get_messages%}

</body>
</html>
```

## HTML Output Example
Here's an example of what gets injected into your page.
```
<div id="says-wrap">

<div id='says-p-mssgs'>
	<ul>
	
		<li class='says-p-mssg' id="persistent-message">
			This is a persistent message. It appears every where and cannot be closed or asked not to appear anymore. You can set duration times.
		</li>
	
	</ul>
</div><!-- end says-pers-->


<div id='says-notices'>
	<a href="#" id="says-close-btn">Close</a>
	<h4> Notifications</h4>
	<ul>
	
		<li class='says-notice' id="simple-notification">
			This is simple notification. It has no duration set so it will show up till its gone.
		</liv>
	
		<li class='says-notice' id="timed-notification">
			This notification has a duration. It will only show up between the specified dates.
		</liv>
	
	</ul>

</div><!-- end says-notices-->

<script type="text/javascript" charset="utf-8">
	var says = {};
	says.set_cookie = function(name, value, expire_days){
		var expire_date = new Date();
		expire_date.setDate(expire_date.getDate()+expire_days);
		document.cookie=name+"="+escape(value)+";expires="+expire_date.toGMTString();
	}
	says.get_cookie = function(name){
		var results = document.cookie.match ( '(^|;) ?' + name + '=([^;]*)(;|$)' );
  		if(results){
    			return (unescape(results[2]));
  		}else{
    			return null;
		}
	}
	says.init = function(){
		
		if(says.get_cookie('simple-notification')){
			var elem = document.getElementById('simple-notification');
			elem.parentNode.removeChild(elem);
		}else{
			says.set_cookie('simple-notification',true,10);
		}
		
		if(says.get_cookie('timed-notification')){
			var elem = document.getElementById('timed-notification');
			elem.parentNode.removeChild(elem);
		}else{
			says.set_cookie('timed-notification',true,10);
		}
		
		
		//cleanup
		if(document.getElementsByClassName('says-notice').length==0){
			var elem = document.getElementById('says-notices');
			elem.parentNode.removeChild(elem);
		}

	}();	


</script>

</div><!-- end says-wrap-->
```

## Styling
Says comes completely unstyled so its up to you to make it look awesome. See the sample html above to determine what classes and id's come with it.

## TODO
* There should be a setting for how long notication cookies are set for.
* Im considering setting up some push notification type of deal via redis, gevent and longpolling.
* Markdown enable message contents

