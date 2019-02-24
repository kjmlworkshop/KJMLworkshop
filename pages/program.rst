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
    <p style="min-height: 220px;">${talk['Abstract']}</p>
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
<b>${poster['Presenter']}</b> (${poster['Affiliation']})<br>
${poster['Poster Title']}
</li>
% endfor
</ol>
<br>
{{% /template %}}



------------------
**Participants**
------------------


.. image:: /images/participants.jpg
   :width: 800px
   :align: center



{{% template %}}

% for person in data['participants']:
<div style="margin-top:10px;">
    <div>
    <img src="../images/${person['Pic']}" class="pic2">
    </div>
    <div>
    <p>
    % if person['Volunteer'] == 'Y':
    <strong style="color:#009900;">[Volunteer] </strong>
    % endif
    <strong>${person['Name']}</strong> (${person['Affiliation']})</p>
    <p style="min-height: 100px;">${person['Keywords']}</p>
    </div>
</div>
% endfor

{{% /template %}}
