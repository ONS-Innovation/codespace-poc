# GitHub Codespaces Proof of Concept: Findings and Recommendations

## Executive Summary

This report summarizes the experience of using GitHub Codespaces for a proof of concept project. It includes the benefits and drawbacks of using Codespaces, as well as recommendations for future use.

To summarise, the main findings are:

- **Benefits**: Quick setup, consistent environment, simple to use.
- **Drawbacks**: Cost (major), initial setup overhead.
- **Recommendations**: Codespaces are well suited to our use case, but the cost is a major drawback. A free alternative would be to use a Dev Container with VS Code, which provides an identical experience without the cost of compute (highly recommended).

## Contents

- [GitHub Codespaces Proof of Concept: Findings and Recommendations](#github-codespaces-proof-of-concept-findings-and-recommendations)
  - [Executive Summary](#executive-summary)
  - [Contents](#contents)
  - [General Experience](#general-experience)
  - [Key Findings](#key-findings)
    - [Codespace Ownership](#codespace-ownership)
    - [Cost](#cost)
    - [Signed Commits](#signed-commits)
    - [Setup Overhead](#setup-overhead)
  - [Recommendations / Next Steps](#recommendations--next-steps)

## General Experience

Over the course of the spike, I have completed all development while working within a GitHub Codespace, using them within the browser and within Visual Studio Code locally. My overall experience has been positive, with the Codespaces providing a consistent and easy-to-use environment for development. The initial setup was straightforward, and the Codespaces were quick to start up before use. Both the browser and VS Code experiences were smooth, with no significant issues encountered during development, bar minor pain points when using keyboard shortcuts in the browser.

It was nice to be able to work on the project without having to set up a local development environment (excluding the initial configuration of the Codespace), which I think will be a major benefit in a few areas:

- **Onboarding**: New developers can quickly get started without needing to install dependencies or configure their local environment.
- **Consistency**: All developers will be working in the same environment, reducing the chances of "it works on my machine" issues.
- **Simplicity**: Non-technical users can easily contribute to the project without needing to understand the technology stack or set up a local development environment—they can click a button and code.

Dev Containers, and furthermore Codespaces, are a great way to allow anybody to quickly get started with a project, even if they are not familiar with the technology stack or know nothing about the project itself.

## Key Findings

### Codespace Ownership

If we were to adopt GitHub Codespaces across ONSdigital, we need to consider how we would manage ownership of them. Within the organisation's settings, you can decide:

- Who can create a Codespace (i.e., all members, specific teams, etc.)
- Who takes ownership of the Codespace (i.e., the user who created it or the organisation)

This is something that needs to be considered, as it will affect how we manage Codespaces and who is billed for their usage. If the organisation owns the Codespaces, then they will be billed for each hour of usage, which could become expensive if many developers are using them. If the user owns the Codespaces, then they will be billed for their usage past their free quota (more on this in the Cost section below).

If the organisation owns the created Codespaces, you can then apply policies to manage their usage, such as controlling which hardware is available, how many Codespaces a user can create at once, and how long they can run for. Deciding on the ownership model and any policies will be crucial to ensure that Codespaces are used effectively and do not become a financial burden.

See the following GitHub Documentation for more information: [Choosing who owns and pays for codespaces in your organisation](https://docs.github.com/en/codespaces/managing-codespaces-for-your-organization/choosing-who-owns-and-pays-for-codespaces-in-your-organization).

### Cost

Codespaces are billed based on the amount of time they are running, the type of machine used, and the amount of storage used. GitHub provides a free quota of Codespace usage per month for each user, which is currently 120 or 180 hours depending on the plan (GitHub Pro or not). For organisations, there is no free quota, and all usage is billed to the organisation. See [Monthly included storage and core hours for personal accounts](https://docs.github.com/en/billing/managing-billing-for-your-products/about-billing-for-github-codespaces#monthly-included-storage-and-core-hours-for-personal-accounts) for more information.

To give an example, if a user creates a Codespace in ONSdigital with **user ownership**, they will be billed for the usage of that Codespace past their free quota. If a user creates a Codespace with **organisation ownership**, the organisation will be billed for the usage of that Codespace.

GitHub provides the following table to estimate the cost of Codespaces based on the type of machine used per hour:

| Machine Type | Usage Multiplier | Cost per Hour (USD) |
|--------------|------------------|---------------------|
| 2 Core | 2 | $0.18 |
| 4 Core | 4 | $0.36 |
| 8 Core | 8 | $0.72 |
| 16 Core | 16 | $1.44 |
| 32 Core | 32 | $2.88 |

and the storage cost is $0.07 per GB per month.

I have been using the 2 core machine during the spike, which has been sufficient, although there were some wait times when initially building containers.

If we were to estimate a monthly cost for a **single Codespace**, it would be:

- **2 Core Machine**: $0.18 per hour
- **8 hours of usage per day**: $0.18 * 8 = $1.44
- **5 working days per week**: $1.44 * 5 = $7.20
- **4 weeks in a month**: $7.20 * 4 = $28

This would mean that for a single Codespace, on the minimum hardware, the cost would be approximately **$28 per month, plus storage costs, per developer**.

If we were to scale this up to **600 users**, the cost would be approximately **$16,800 per month**, plus storage costs. This also doesn't factor in if a developer has multiple Codespaces running at the same time, which would increase the cost significantly.

If the organisation were to own Codespaces, they would have to pay these costs. Average developers would also need to pay above the quota, as 120 hours is not enough for a full month of work.

As mentioned above, there are policies that can be applied to manage the usage of GitHub Codespaces. This would help to control costs and ensure that Codespaces are used effectively (i.e., developers are not leaving Codespaces running when they are not needed, and only two Codespaces can be running at once).

### Signed Commits

A positive of using GitHub Codespaces is that signed commits are much easier to achieve across the organisation than with a local development environment. To enable signed commits in a Codespace, each user has to enable GPG Verification in their GitHub account settings. This is a one-time action that will enable signed commits across all repositories they contribute to.

There is an initial effort to set this up, but once it is done, all commits made in the Codespace will be signed by default. This would also solve the issue of enforcing signed commits across the organisation, instead of a best-effort approach.

### Setup Overhead

To adopt GitHub Codespaces across ONSdigital, there is an initial setup overhead to consider. This includes:

- Setting up the organisation's policies for Codespaces, including ownership, usage limits, and hardware types.
- Creating Dev Container templates for projects to adopt.
- Updating existing projects to include a Dev Container configuration. This can be avoided by using GitHub's default Dev Container configuration, but this may not be suitable for all projects.
- Training users on how to use Codespaces effectively, including how to create and manage them, and how to use the Dev Container configuration.

## Recommendations / Next Steps

Following the spike, I think that GitHub Codespaces are well suited to our use case, but the cost is a major drawback. If we were to adopt the "programming out of a container" approach, I would recommend using a Dev Container with Visual Studio Code instead of GitHub Codespaces, as this removes the cost of compute. This alternative would cause some initial setup overhead, such as installing a Docker daemon and configuring Dev Containers for each project, but would be worth the reward in the long run. In terms of less technical users, I think that Codespaces would be a great way to allow them to contribute to projects without needing to understand the technology stack or set up a local development environment, but this could also be achieved with Dev Containers and Visual Studio Code (perhaps with an initial learning curve).

In terms of next steps, I would recommend the following:

- **Ownership Model**: Decide on the ownership model for Codespaces within ONSdigital. This would include who can create Codespaces, who owns them, and what policies should be applied to manage their usage.
- **Costing Trial**: If we were to adopt GitHub Codespaces, I would recommend running a costing trial with a small group of developers to see how much it would cost in practice. This would help to understand the financial implications of using Codespaces and whether they are feasible for the organisation.
- **Dev Container Adoption**: Start adopting Dev Containers across projects. This would allow us to start using GitHub Codespaces, and, if too expensive, we can fall back to using Dev Containers with Visual Studio Code without losing the benefits of a consistent development environment. If templates are created for common container configurations, this would speed up the adoption process.
- **Other Languages**: Investigate using Codespaces with other languages, such as JavaScript. This would help to understand how well Codespaces work with different technology stacks. If we were to investigate a web stack, for example, React with Node.js, this would allow us to see how Codespaces scale with project complexity.
- **Lightning Talk/Demo**: Present the findings of this spike to potential users to understand their thoughts and concerns. This would help to gauge interest in using GitHub Codespaces and Dev Containers, whether users are willing to adopt them, and if they actually solve the problems we are trying to address.
