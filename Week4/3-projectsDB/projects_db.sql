SELECT project.name 
FROM project
	JOIN project_uses_tech
		ON project_uses_tech.project_id = project.id
	JOIN tech
		ON project_uses_tech.tech_id = tech.id
WHERE tech.name = 'JavaScript';

--

SELECT tech.name 
FROM tech
	JOIN project_uses_tech
		ON project_uses_tech.tech_id = tech.id
	JOIN project
		ON project_uses_tech.project_id = project.id
WHERE project.name = 'Personal Website';

--

SELECT tech.name 
FROM tech
	LEFT OUTER JOIN project_uses_tech
		ON project_uses_tech.tech_id = tech.id
WHERE project_uses_tech.project_id IS NULL;
		
--

SELECT tech.name, COUNT(tech.name)
FROM tech
	LEFT OUTER JOIN project_uses_tech
		ON project_uses_tech.tech_id = tech.id
WHERE project_uses_tech.project_id IS NOT NULL
GROUP BY tech.name;

--

SELECT project.name
FROM project
	LEFT OUTER JOIN project_uses_tech
		ON project_uses_tech.project_id = project.id
WHERE project_uses_tech.project_id IS NULL;

--

SELECT project.name, COUNT(project.name)
FROM project
	LEFT OUTER JOIN project_uses_tech
		ON project_uses_tech.project_id = project.id
WHERE project_uses_tech.project_id IS NOT NULL OR project_uses_tech.project_id IS NULL
GROUP BY project.name;

--

SELECT project.name, tech.name 
FROM project
	JOIN project_uses_tech
		ON project_uses_tech.project_id = project.id
	JOIN tech
		ON project_uses_tech.tech_id = tech.id
WHERE project.id = project_uses_tech.project_id;

--

SELECT DISTINCT (tech.name)
FROM tech
	JOIN project_uses_tech
		ON project_uses_tech.tech_id = tech.id
WHERE tech.id = project_uses_tech.tech_id;


--

SELECT tech.name
FROM tech
	LEFT OUTER JOIN project_uses_tech
		ON project_uses_tech.tech_id = tech.id
WHERE project_uses_tech.tech_id IS NULL;

--

SELECT DISTINCT (project.name)
FROM project
	JOIN project_uses_tech
		ON project_uses_tech.project_id = project.id
WHERE project.id = project_uses_tech.project_id;

--

SELECT DISTINCT (project.name)
FROM project
	LEFT OUTER JOIN project_uses_tech
		ON project_uses_tech.project_id = project.id
WHERE project_uses_tech.project_id IS NULL;

--

SELECT project.name, COUNT(project.name) AS count
FROM project
	JOIN project_uses_tech
		ON project_uses_tech.project_id = project.id
WHERE project_uses_tech.project_id = project_uses_tech.project_id
GROUP BY project.name
ORDER BY count DESC;

--

SELECT tech.name, COUNT(tech.name) AS count
FROM tech
	JOIN project_uses_tech
		ON project_uses_tech.tech_id = tech.id
WHERE project_uses_tech.tech_id = tech.id
GROUP BY tech.name
ORDER BY count DESC;

--
SELECT AVG(count)
FROM 
	(SELECT COUNT(tech.name) AS count
	FROM tech
		JOIN project_uses_tech
			ON project_uses_tech.tech_id = tech.id
	WHERE project_uses_tech.tech_id = tech.id
	GROUP BY tech.name) AS techNum;



