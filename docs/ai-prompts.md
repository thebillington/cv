# AI Prompts for CV Management

These prompts are designed for use with LLMs to help maintain and improve CV content.

## Rewrite an Achievement

```
I have a CV achievement written in YAML format. Rewrite it to be more impactful
and ATS-friendly while keeping the same factual content.

```yaml
title: Built automated endpoint parity testing suite
description: Developed a Python-based regression testing framework that validated
  behavioural parity between old and new service implementations during migration.
impact: medium
tags:
  - testing
  - automation
  - python
  - migration
```

Rewrite it with a stronger emphasis on business impact and measurable outcomes.
```

## Generate a Targeted Summary

```
I'm applying for a [Senior Platform Engineer] role that requires strong
Terraform, AWS, and CI/CD skills. Generate a professional summary for my CV
that highlights my platform engineering experience.

My background:
- Leading service extraction with Terraform/AWS at Blue Light Card
- Built CI/CD pipelines at Sano Genetics
- Architected AWS infrastructure at Paperound
- Engineering management experience at Pion and Sano Genetics

The summary should be 2-3 sentences, professional tone, suitable for a CV header.
```

## Tailor CV for a Specific Role

```
Given this job description, which of my achievements should I prioritise?

Job Description:
[Paste job description here]

My achievements (tagged):
[Paste relevant achievements from YAML files]

For each achievement, rate its relevance as high/medium/low and explain why.
```

## Generate a Cover Letter

```
Generate a professional cover letter for a [role] position at [company].

My background:
- [Key achievement 1]
- [Key achievement 2]
- [Key achievement 3]

The role requires:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

Keep it concise (3-4 paragraphs), professional, and tailored to the company.
```

## Improve Wording

```
Improve the wording of this CV achievement bullet point. Make it more active
and impactful. Keep it to one line.

Before: "Was responsible for the migration of the CI pipeline from CircleCI
to GitHub Actions which made builds faster."

After: [AI generates improved version]
```

## Identify Missing Skills

```
Based on the following job description and my current CV skills, identify
which skills I should highlight more or acquire. Suggest specific achievements
I could add to my CV.

Job description keywords:
[Keywords from JD]

My current skills:
[Skills from skills.yml]
```
