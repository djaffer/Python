


<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    
    
    <title>cs373/FunctionDict.py at master · gpdowning/cs373</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="gpdowning/cs373" name="twitter:title" /><meta content="Contribute to cs373 development by creating an account on GitHub." name="twitter:description" /><meta content="https://avatars0.githubusercontent.com/u/315177?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars0.githubusercontent.com/u/315177?v=3&amp;s=400" property="og:image" /><meta content="gpdowning/cs373" property="og:title" /><meta content="https://github.com/gpdowning/cs373" property="og:url" /><meta content="Contribute to cs373 development by creating an account on GitHub." property="og:description" />
      <meta name="browser-stats-url" content="/_stats">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035">
    <link rel="xhr-socket" href="/_sockets">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>
      <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="434E6142:3729:F8C04:54F2573F" name="octolytics-dimension-request_id" /><meta content="5740725" name="octolytics-actor-id" /><meta content="djaffer" name="octolytics-actor-login" /><meta content="c466db9cf8ef4e3e9b43b99de70a4fb7ecaa319d0b30ca6439a742285a1938b3" name="octolytics-actor-hash" />
    
    <meta content="Rails, view, blob#show" name="analytics-event" />

    
    <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">


    <meta content="authenticity_token" name="csrf-param" />
<meta content="c/4GkzoLdE0pBSKUx1Pr/qIOKOe91W6hxYizqKs1saf3OHumBYGf/FX3Ejcl/hvCINIH0l9Aaev9uuJ/e0PfPw==" name="csrf-token" />

    <link href="https://assets-cdn.github.com/assets/github-84e4144e3c0347e1187b021a88b6bcbad5186ac898c63e26b13332c7c53504a6.css" media="all" rel="stylesheet" />
    <link href="https://assets-cdn.github.com/assets/github2-8f9492ba1b29d6e5b41cd7e06e0e88a5b1c8ae107269e75f5ca3bbba8afc5a3f.css" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="5639dbee804d4503f9a9dbc99fac39bb">

      
  <meta name="description" content="Contribute to cs373 development by creating an account on GitHub.">
  <meta name="go-import" content="github.com/gpdowning/cs373 git https://github.com/gpdowning/cs373.git">

  <meta content="315177" name="octolytics-dimension-user_id" /><meta content="gpdowning" name="octolytics-dimension-user_login" /><meta content="29568912" name="octolytics-dimension-repository_id" /><meta content="gpdowning/cs373" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="29568912" name="octolytics-dimension-repository_network_root_id" /><meta content="gpdowning/cs373" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/gpdowning/cs373/commits/master.atom" rel="alternate" title="Recent Commits to cs373:master" type="application/atom+xml">

  </head>


  <body class="logged_in  env-production windows vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      
      


      <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <form accept-charset="UTF-8" action="/gpdowning/cs373/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/gpdowning/cs373/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <input type="text"
    class="js-site-search-field is-clearable"
    data-hotkey="s"
    name="q"
    placeholder="Search"
    data-global-scope-placeholder="Search GitHub"
    data-repo-scope-placeholder="Search"
    tabindex="1"
    autocapitalize="off">
  <div class="scope-badge">This repository</div>
</form>
      </div>
      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item explore">
          <a class="header-nav-link" href="/explore" data-ga-click="Header, go to explore, text:explore">Explore</a>
        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="/blog" data-ga-click="Header, go to blog, text:blog">Blog</a>
          </li>
        <li class="header-nav-item">
          <a class="header-nav-link" href="https://help.github.com" data-ga-click="Header, go to help, text:help">Help</a>
        </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name" href="/djaffer" data-ga-click="Header, go to profile, text:username">
      <img alt="Danish J." class="avatar" data-user="5740725" height="20" src="https://avatars2.githubusercontent.com/u/5740725?v=3&amp;s=40" width="20" />
      <span class="css-truncate">
        <span class="css-truncate-target">djaffer</span>
      </span>
    </a>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link js-menu-target tooltipped tooltipped-s" href="#" aria-label="Create new..." data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      
<ul class="dropdown-menu">
  <li>
    <a href="/new" data-ga-click="Header, create new repository, icon:repo"><span class="octicon octicon-repo"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new" data-ga-click="Header, create new organization, icon:organization"><span class="octicon octicon-organization"></span> New organization</a>
  </li>


    <li class="dropdown-divider"></li>
    <li class="dropdown-header">
      <span title="gpdowning/cs373">This repository</span>
    </li>
      <li>
        <a href="/gpdowning/cs373/issues/new" data-ga-click="Header, create new issue, icon:issue"><span class="octicon octicon-issue-opened"></span> New issue</a>
      </li>
</ul>

    </div>
  </li>

  <li class="header-nav-item">
        <a href="/notifications" aria-label="You have unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:unread" data-hotkey="g n">
        <span class="mail-status unread"></span>
        <span class="octicon octicon-inbox"></span>
</a>
  </li>

  <li class="header-nav-item">
    <a class="header-nav-link tooltipped tooltipped-s" href="/settings/profile" id="account_settings" aria-label="Settings" data-ga-click="Header, go to settings, icon:settings">
      <span class="octicon octicon-gear"></span>
    </a>
  </li>

  <li class="header-nav-item">
    <form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="fK+hDB0XXYAnKm3QvymdwQeXLkqj/sMI4bv9wGg/VCc8Ers7jJqF9QWoDYHbbChCPVgZ1U8sB4MRQx7FTKSnQg==" /></div>
      <button class="header-nav-link sign-out-button tooltipped tooltipped-s" aria-label="Sign out" data-ga-click="Header, sign out, icon:logout">
        <span class="octicon octicon-sign-out"></span>
      </button>
</form>  </li>

</ul>


    
  </div>
</div>

      

        


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        
<ul class="pagehead-actions">

  <li>
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="zMzQiT25Wu5aet1EWB288etqRHrmLm4MVk4dNHt8zunazQR+yQb93iUlufwR7ARQTBF6Jrk5XF6N1kNwSja3zg==" /></div>    <input id="repository_id" name="repository_id" type="hidden" value="29568912" />

      <div class="select-menu js-menu-container js-select-menu">
        <a class="social-count js-social-count" href="/gpdowning/cs373/watchers">
          3
        </a>
        <a href="/gpdowning/cs373/subscription"
          class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0" aria-haspopup="true">
          <span class="js-select-button">
            <span class="octicon octicon-eye"></span>
            Watch
          </span>
        </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header">
              <span class="select-menu-title">Notifications</span>
              <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
            </div>

            <div class="select-menu-list js-navigation-container" role="menu">

              <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                  <span class="select-menu-item-heading">Not watching</span>
                  <span class="description">Be notified when participating or @mentioned.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Watch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                  <span class="select-menu-item-heading">Watching</span>
                  <span class="description">Be notified of all conversations.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Unwatch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_ignore" name="do" type="radio" value="ignore" />
                  <span class="select-menu-item-heading">Ignoring</span>
                  <span class="description">Never be notified.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-mute"></span>
                    Stop ignoring
                  </span>
                </div>
              </div>

            </div>

          </div>
        </div>
      </div>
</form>

  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <form accept-charset="UTF-8" action="/gpdowning/cs373/unstar" class="js-toggler-form starred js-unstar-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="yeo5dWLpwmTqfYib9GEt//ZMkzYvv/pEX81N8tSde1DBGwATYTkSQ+kiOXBuk3GPhJIiMq38rcBm/Q2fuTEmiQ==" /></div>
      <button
        class="minibutton with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar gpdowning/cs373">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/gpdowning/cs373/stargazers">
          2
        </a>
</form>
    <form accept-charset="UTF-8" action="/gpdowning/cs373/star" class="js-toggler-form unstarred js-star-button" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="yNQnwS2tVBzAwnoax5SWjLn1xwSVNRNW0ENj03mqdH1oi32Aial44tuaghg+jp1asZYqmna8rGmmhwjhzxoe1g==" /></div>
      <button
        class="minibutton with-count js-toggler-target"
        aria-label="Star this repository" title="Star gpdowning/cs373">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/gpdowning/cs373/stargazers">
          2
        </a>
</form>  </div>

  </li>

        <li>
          <a href="/gpdowning/cs373/fork" class="minibutton with-count js-toggler-target tooltipped-n" title="Fork your own copy of gpdowning/cs373 to your account" aria-label="Fork your own copy of gpdowning/cs373 to your account" rel="facebox nofollow">
            <span class="octicon octicon-repo-forked"></span>
            Fork
          </a>
          <a href="/gpdowning/cs373/network" class="social-count">3</a>
        </li>

</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="mega-octicon octicon-repo"></span>
          <span class="author"><a href="/gpdowning" class="url fn" itemprop="url" rel="author"><span itemprop="title">gpdowning</span></a></span><!--
       --><span class="path-divider">/</span><!--
       --><strong><a href="/gpdowning/cs373" class="js-current-repository" data-pjax="#js-repo-pjax-container">cs373</a></strong>

          <span class="page-context-loader">
            <img alt="" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      <div class="repository-with-sidebar repo-container new-discussion-timeline  ">
        <div class="repository-sidebar clearfix">
            
<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/gpdowning/cs373/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/gpdowning/cs373" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /gpdowning/cs373">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/gpdowning/cs373/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /gpdowning/cs373/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull Requests">
      <a href="/gpdowning/cs373/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /gpdowning/cs373/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>


      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="/gpdowning/cs373/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /gpdowning/cs373/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/gpdowning/cs373/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /gpdowning/cs373/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/gpdowning/cs373/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /gpdowning/cs373/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/assets/spinners/octocat-spinner-32-e513294efa576953719e4e2de888dd9cf929b7d62ed8d05f25e731d02452ab6c.gif" width="16" />
</a>    </li>
  </ul>


</nav>

              <div class="only-with-full-nav">
                  
<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/gpdowning/cs373.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone">
  <h3><span class="text-emphasized">SSH</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="git@github.com:gpdowning/cs373.git" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/gpdowning/cs373" readonly="readonly">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



<p class="clone-options">You can clone with
  <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>, <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>, or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
    <span class="octicon octicon-question"></span>
  </a>
</p>


  <a href="github-windows://openRepo/https://github.com/gpdowning/cs373" class="minibutton sidebar-button" title="Save gpdowning/cs373 to your computer and use it in GitHub Desktop." aria-label="Save gpdowning/cs373 to your computer and use it in GitHub Desktop.">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>

                <a href="/gpdowning/cs373/archive/master.zip"
                   class="minibutton sidebar-button"
                   aria-label="Download the contents of gpdowning/cs373 as a zip file"
                   title="Download the contents of gpdowning/cs373 as a zip file"
                   rel="nofollow">
                  <span class="octicon octicon-cloud-download"></span>
                  Download ZIP
                </a>
              </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          

<a href="/gpdowning/cs373/blob/73e9b959aff42f3df587df9a06ee1ea0b9128915/examples/FunctionDict.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:58888884bdc50d281e9be2fe7e5316af -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu js-menu-container js-select-menu left">
  <span class="minibutton select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    title="master"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button css-truncate-target">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/gpdowning/cs373/blob/master/examples/FunctionDict.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="button-group right">
    <a href="/gpdowning/cs373/find/master"
          class="js-show-file-finder minibutton empty-icon tooltipped tooltipped-s"
          data-pjax
          data-hotkey="t"
          aria-label="Quickly jump between files">
      <span class="octicon octicon-list-unordered"></span>
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard minibutton zeroclipboard-button" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
  </div>

  <div class="breadcrumb js-zeroclipboard-target">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/gpdowning/cs373" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">cs373</span></a></span></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/gpdowning/cs373/tree/master/examples" class="" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">examples</span></a></span><span class="separator">/</span><strong class="final-path">FunctionDict.py</strong>
  </div>
</div>


  <div class="commit file-history-tease">
    <div class="file-history-tease-header">
        <img alt="Glenn Downing" class="avatar" data-user="315177" height="24" src="https://avatars3.githubusercontent.com/u/315177?v=3&amp;s=48" width="24" />
        <span class="author"><a href="/gpdowning" rel="author">gpdowning</a></span>
        <time datetime="2015-02-20T01:42:44Z" is="relative-time">Feb 19, 2015</time>
        <div class="commit-title">
            <a href="/gpdowning/cs373/commit/6b30a1f89a1205effd1f924b6a07e6c4834cdbde" class="message" data-pjax="true" title="another commit">another commit</a>
        </div>
    </div>

    <div class="participation">
      <p class="quickstat">
        <a href="#blob_contributors_box" rel="facebox">
          <strong>1</strong>
           contributor
        </a>
      </p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="Glenn Downing" data-user="315177" height="24" src="https://avatars3.githubusercontent.com/u/315177?v=3&amp;s=48" width="24" />
            <a href="/gpdowning">gpdowning</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
    <div class="file-info">
        <span class="file-mode" title="File mode">executable file</span>
        <span class="file-info-divider"></span>
        46 lines (35 sloc)
        <span class="file-info-divider"></span>
      1.521 kb
    </div>
    <div class="file-actions">
      <div class="button-group">
        <a href="/gpdowning/cs373/raw/master/examples/FunctionDict.py" class="minibutton " id="raw-url">Raw</a>
          <a href="/gpdowning/cs373/blame/master/examples/FunctionDict.py" class="minibutton js-update-url-with-hash">Blame</a>
        <a href="/gpdowning/cs373/commits/master/examples/FunctionDict.py" class="minibutton " rel="nofollow">History</a>
      </div><!-- /.button-group -->

        <a class="octicon-button tooltipped tooltipped-nw"
           href="github-windows://openRepo/https://github.com/gpdowning/cs373?branch=master&amp;filepath=examples%2FFunctionDict.py" aria-label="Open this file in GitHub for Windows">
            <span class="octicon octicon-device-desktop"></span>
        </a>

            <a class="octicon-button tooltipped tooltipped-n js-update-url-with-hash"
               aria-label="Clicking this button will fork this project so you can edit the file"
               href="/gpdowning/cs373/edit/master/examples/FunctionDict.py"
               data-method="post" rel="nofollow"><span class="octicon octicon-pencil"></span></a>

          <a class="octicon-button danger tooltipped tooltipped-s"
             href="/gpdowning/cs373/delete/master/examples/FunctionDict.py"
             aria-label="Fork this project and delete file"
             data-method="post" data-test-id="delete-blob-file" rel="nofollow">
        <span class="octicon octicon-trashcan"></span>
      </a>
    </div><!-- /.actions -->
  </div>
  
  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size-8 js-file-line-container">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code js-file-line"><span class="pl-c">#!/usr/bin/env python3</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code js-file-line"><span class="pl-c"># ---------------</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code js-file-line"><span class="pl-c"># FunctionDict.py</span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code js-file-line"><span class="pl-c"># ---------------</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code js-file-line"><span class="pl-k">print</span>(<span class="pl-s1"><span class="pl-pds">&quot;</span>FunctionDict.py<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code js-file-line"><span class="pl-st">def</span> <span class="pl-en">f</span> (<span class="pl-vpf">x</span>, <span class="pl-vpf">y</span>, **<span class="pl-vpf">z</span>) :</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code js-file-line">    <span class="pl-k">assert</span> <span class="pl-s3">type</span>(z) <span class="pl-k">is</span> <span class="pl-s3">dict</span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code js-file-line">    <span class="pl-k">return</span> [x, y, z]</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code js-file-line"><span class="pl-k">assert</span> f(<span class="pl-c1">2</span>, <span class="pl-c1">3</span>)               <span class="pl-k">==</span> [<span class="pl-c1">2</span>, <span class="pl-c1">3</span>, {}]</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code js-file-line"><span class="pl-k">assert</span> f(<span class="pl-c1">2</span>, <span class="pl-c1">3</span>, <span class="pl-vpf">a</span> <span class="pl-k">=</span> <span class="pl-c1">4</span>)        <span class="pl-k">==</span> [<span class="pl-c1">2</span>, <span class="pl-c1">3</span>, {<span class="pl-s1"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">4</span>}]</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code js-file-line"><span class="pl-k">assert</span> f(<span class="pl-c1">2</span>, <span class="pl-c1">3</span>, <span class="pl-vpf">a</span> <span class="pl-k">=</span> <span class="pl-c1">4</span>, <span class="pl-vpf">b</span> <span class="pl-k">=</span> <span class="pl-c1">5</span>) <span class="pl-k">==</span> [<span class="pl-c1">2</span>, <span class="pl-c1">3</span>, {<span class="pl-s1"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">4</span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>b<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">5</span>}]</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code js-file-line"><span class="pl-k">assert</span> f(<span class="pl-c1">2</span>, <span class="pl-c1">3</span>, <span class="pl-vpf">a</span> <span class="pl-k">=</span> <span class="pl-c1">4</span>, <span class="pl-vpf">b</span> <span class="pl-k">=</span> <span class="pl-c1">5</span>) <span class="pl-k">==</span> [<span class="pl-c1">2</span>, <span class="pl-c1">3</span>, {<span class="pl-s1"><span class="pl-pds">&#39;</span>b<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">5</span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">4</span>}]</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code js-file-line"><span class="pl-c">#f(2, 3, {&#39;b&#39; : 5, &#39;a&#39; : 4})   # TypeError: f() takes exactly 2 arguments (3 given)</span></td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code js-file-line"><span class="pl-c">#f(2, 3, [(&#39;b&#39;, 5), (&#39;a&#39;, 4)]) # TypeError: f() takes exactly 2 arguments (3 given)</span></td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code js-file-line">d <span class="pl-k">=</span> {<span class="pl-s1"><span class="pl-pds">&quot;</span>b<span class="pl-pds">&quot;</span></span> : <span class="pl-c1">4</span>, <span class="pl-s1"><span class="pl-pds">&quot;</span>a<span class="pl-pds">&quot;</span></span> : <span class="pl-c1">3</span>}</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code js-file-line">u <span class="pl-k">=</span> (<span class="pl-c1">2</span>,)</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code js-file-line"><span class="pl-k">assert</span> d                 <span class="pl-k">==</span> {<span class="pl-s1"><span class="pl-pds">&#39;</span>b<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">4</span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">3</span>}</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code js-file-line"><span class="pl-k">assert</span> d                 <span class="pl-k">==</span> {<span class="pl-s1"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">3</span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>b<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">4</span>}</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code js-file-line"><span class="pl-k">assert</span> f(<span class="pl-c1">2</span>, <span class="pl-c1">5</span>,     <span class="pl-k">**</span>d)  <span class="pl-k">==</span> [<span class="pl-c1">2</span>, <span class="pl-c1">5</span>, {<span class="pl-s1"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">3</span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>b<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">4</span>}]</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code js-file-line"><span class="pl-k">assert</span> f(<span class="pl-c1">2</span>, <span class="pl-vpf">y</span> <span class="pl-k">=</span> <span class="pl-c1">5</span>, <span class="pl-k">**</span>d)  <span class="pl-k">==</span> [<span class="pl-c1">2</span>, <span class="pl-c1">5</span>, {<span class="pl-s1"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">3</span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>b<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">4</span>}]</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code js-file-line"><span class="pl-k">assert</span> f(<span class="pl-vpf">y</span> <span class="pl-k">=</span> <span class="pl-c1">5</span>, <span class="pl-k">*</span>u, <span class="pl-k">**</span>d) <span class="pl-k">==</span> [<span class="pl-c1">2</span>, <span class="pl-c1">5</span>, {<span class="pl-s1"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">3</span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>b<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">4</span>}]</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code js-file-line"><span class="pl-k">assert</span> f(<span class="pl-k">*</span>u, <span class="pl-vpf">y</span> <span class="pl-k">=</span> <span class="pl-c1">5</span>, <span class="pl-k">**</span>d) <span class="pl-k">==</span> [<span class="pl-c1">2</span>, <span class="pl-c1">5</span>, {<span class="pl-s1"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">3</span>, <span class="pl-s1"><span class="pl-pds">&#39;</span>b<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">4</span>}]</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code js-file-line"><span class="pl-c">#f(2, **d, y = 5)                                      # SyntaxError: invalid syntax</span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code js-file-line">d <span class="pl-k">=</span> {<span class="pl-s1"><span class="pl-pds">&quot;</span>y<span class="pl-pds">&quot;</span></span> : <span class="pl-c1">3</span>, <span class="pl-s1"><span class="pl-pds">&quot;</span>x<span class="pl-pds">&quot;</span></span> : <span class="pl-c1">2</span>}</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code js-file-line"><span class="pl-c">#f(2, **d)                   # TypeError: f() got multiple values for keyword argument &#39;x&#39;</span></td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code js-file-line"><span class="pl-k">assert</span> f(<span class="pl-k">**</span>d) <span class="pl-k">==</span> [<span class="pl-c1">2</span>, <span class="pl-c1">3</span>, {}]</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code js-file-line">d <span class="pl-k">=</span> {<span class="pl-s1"><span class="pl-pds">&quot;</span>y<span class="pl-pds">&quot;</span></span> : <span class="pl-c1">3</span>}</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code js-file-line"><span class="pl-k">assert</span> f(<span class="pl-c1">2</span>,     <span class="pl-k">**</span>d) <span class="pl-k">==</span> [<span class="pl-c1">2</span>, <span class="pl-c1">3</span>, {}]</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code js-file-line"><span class="pl-k">assert</span> f(<span class="pl-vpf">x</span> <span class="pl-k">=</span> <span class="pl-c1">2</span>, <span class="pl-k">**</span>d) <span class="pl-k">==</span> [<span class="pl-c1">2</span>, <span class="pl-c1">3</span>, {}]</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code js-file-line"><span class="pl-c">#f(**d)                            # TypeError: f() takes exactly 2 arguments (1 given)</span></td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code js-file-line">d <span class="pl-k">=</span> {<span class="pl-s1"><span class="pl-pds">&quot;</span>y<span class="pl-pds">&quot;</span></span> : <span class="pl-c1">3</span>, <span class="pl-s1"><span class="pl-pds">&quot;</span>a<span class="pl-pds">&quot;</span></span> : <span class="pl-c1">2</span>}</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code js-file-line"><span class="pl-k">assert</span> f(<span class="pl-c1">2</span>,     <span class="pl-k">**</span>d) <span class="pl-k">==</span> [<span class="pl-c1">2</span>, <span class="pl-c1">3</span>, {<span class="pl-s1"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">2</span>}]</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code js-file-line"><span class="pl-k">assert</span> f(<span class="pl-vpf">x</span> <span class="pl-k">=</span> <span class="pl-c1">2</span>, <span class="pl-k">**</span>d) <span class="pl-k">==</span> [<span class="pl-c1">2</span>, <span class="pl-c1">3</span>, {<span class="pl-s1"><span class="pl-pds">&#39;</span>a<span class="pl-pds">&#39;</span></span> : <span class="pl-c1">2</span>}]</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code js-file-line"><span class="pl-c">#f(**d)                                   # TypeError: f() takes exactly 2 arguments (1 given)</span></td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code js-file-line">
</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code js-file-line"><span class="pl-k">print</span>(<span class="pl-s1"><span class="pl-pds">&quot;</span>Done.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
</table>

  </div>

</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="http://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="http://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="/" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.04858s from github-fe121-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
    </ul>
  </div>
</div>


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-9643b0378c6bcb216adcdaaaa703eed77aa239aaf1c2ae44cadb2fb5099ec172.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-d967f968a967d73050b6f00df5ceb05917ff8f3c7f3803e832bee5eda8037365.js"></script>
      
      

  </body>
</html>

