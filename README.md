<h2>External Dependencies</h2>
<h4>Psycopg2</h4>
<p>You can install the Windows port from one of the following links:</p>
<ul>
	<li>http://initd.org/psycopg/download/</li>
	<li>http://www.stickpeople.com/projects/python/win-psycopg/</li>
</ul>
<br/>


<h2>Python Files: py</h2>
<h4>gauntlet.py</h4>
<p>Handles spatial SQL queries submitted to the database with Psycopg2.<p>
<h4>main.py</h4> 
<p>Generates a Subject instance for each individual in the original sample. The function genSubjectList (gauntlet.py) is currently set to only query the following subjects: 14, 47, 58, 62, 114. All subjects will be part of the query when the Subject class is expanded to treat aspects of individual subgroup configurations.</p> 
<h4>subject.py</h4> 
<p>Handles the class model for a given subject. The current plan is to expand upon how individual subgroup configurations are treated.</p>
<h4>util.py</h4>
<p>Simple console logging. CSV documentation and plotting functions will be added back to this module after the Subject class model has been completed.</p>
<br/>


<h2>PostgreSQL: postgres</h2>
<p>A backup file containing the following tables:</p>
<ul>
	<li>originxy: Point of Origin for the plane provided in each subject response.</li>
	<li>t1_circles: Collection of subject responses collected at Time One.</li>
	<li>t2_circles: Collection of subject responses collected at Time Two.</li>
</ul>
<br/>


<h2>Prior Research</h2>
<p>The following link will direct you to a shared Google Drive space with several key pieces of research literature. Each of these documents should provide you with a general understanding of other research efforts dedicated to the subject of Social Identity.</p>
<a href="https://drive.google.com/drive/folders/0B5SPOPlZuJ4FVlNueFdYWGpiZDg?usp=sharing">Google Drive</a>
<br/><br/>


<h2>An Overview of the Subject Model</h2>
<p>Presented below is a visual guide to how this research will be approaching geometric representations of the social self.
Subjects have been selected for discussion based upon characteristics that we find particularly interesting. 
A brief introduction of terms that are useful in describing the geometric configurations of our sample is set forth below.</p>
<ul>
	<li>Origin: The center of the response plane provided to each subject.</li>
	<li>Identity: A circle drawn by the subject.</li>
	<li>Primary Identity: The identity reported as Rank One in the overall configuration. This identity will be shown in blue in all figures and will not be labeled.</li>
	<li>Bridge Identity: An indentity that provides a geometric link between the Primary Identity and another identity that is not overlapping the Primary Identity.</li>
	<li>Subsumed Identity: An identity that is completely contained by another identity.</li>
	<li>Group: The overall collection of indentities reported by the subject.</li>
	<li>Subgroup: A collection of identities that overlap.</li>
</ul>

<div>
	<h3>Subject 14 @ Time 1</h3>
	<img src='https://github.com/Jwmazzi/sic/blob/master/illustrations/SUB_14_T1.jpg'/>
	<h4>Subgroup One (Primary Identity)</h4>
	<ul>
		<li>1: Daughter</li>
		<li>2: Sister</li>
		<li>3: Jewish</li>
	</ul>
	<h4>Subgroup Two</h4>
	<ul>
		<li>4: Painting Major</li>
		<li>5: VPA</li>
	</ul>
</div>

<div>
	<h3>Subject 14 @ Time 2</h3>
	<img src='https://github.com/Jwmazzi/sic/blob/master/illustrations/SUB_14_T2.jpg'/>
	<h4>Subgroup One (Primary Identity)</h4>
	<ul>
		<li>1: Daughter</li>
		<li>2: Sister</li>
	</ul>
	<h4>Subgroup Two</h4>
	<ul>
		<li>3: Jewish</li>
		<li>5: VPA Student</li>
	</ul>
	<h4>Subgroup Three</h4>
	<ul>
		<li>4: Friend</li>
	</ul>
</div>