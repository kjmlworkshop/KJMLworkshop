.. title: Program
.. slug: program
.. date: 2018-10-29 18:03:28 UTC+09:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. hidetitle: true
.. hasmath: true


.. raw:: html

    <link src="assets/css/custom.css">
    <script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>


============
**Program**
============


.. contents::  :local:

-----------
**Talks**
-----------


{{% template %}}

% for talk in data['talks']:
<div style="margin-top:10px;">
    <div>
    <img src="../images/${talk['Pic']}" class="pic">
    </div>
    <div>
    <p><strong>${talk['Title']}</strong></p>
    <p>${talk['Name']} (${talk['Affiliation']})</p>
    <p style="min-height: 170px;">${talk['Abstract']}</p>
    </div>
</div>
% endfor

{{% /template %}}



--------------
**Posters**
--------------

{{% template %}}

<ol>
% for poster in data['posters']:
<li class='poster-list'>
<b>${poster['Poster Title']}</b><br>
${poster['Presenter']} (${poster['Affiliation']})
</li>
% endfor
</ol>

{{% /template %}}


------------------
**Participants**
------------------

{{% template %}}

% for person in data['participants']:
<div style="margin-top:10px;">
    <div>
    <img src="../images/${person['Pic']}" class="pic">
    </div>
    <div>
    <p><strong>${person['Name']}</strong></p>
    <p>${person['Affiliation']}</p>
    <p style="min-height: 170px;">${person['Keywords']}</p>
    </div>
</div>
% endfor

{{% /template %}}




The list of participants will be updated soon.
