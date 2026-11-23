> This AI-written manuscript is being released to record the author’s claim of priority for the result. The proof was developed jointly by the author and ChatGPT. The author plans to revise the manuscript and post the revised version on arXiv.

# The minimum area translation cover for planar sets of diameter one

**Author:** Akatsuki Nishioka  
**Affiliation:** Department of Mathematical and Computing Science, Institute of Science Tokyo  
**Manuscript date:** November 23, 2026

**[Read the manuscript (PDF)](./minimum_area_translation_covers%281%29.pdf)**

## Abstract

We resolve a translation-only variant of Lebesgue’s universal covering problem that had remained open since at least 1980. We prove that Duff’s truncated unit square is, up to congruence, the unique convex body of least area that contains a translate of every planar set of diameter one. Its area is $\pi/6 + 2\sqrt{3} - 3$. The proof uses reflected Reuleaux triangles to compare vertical sections of an arbitrary cover. Equality forces the cover into a unit square, where the placement of each Reuleaux triangle is unique.

## Main result

A **translation cover** is a compact convex set $K \subset \mathbb{R}^2$ such that every planar set of diameter at most one has a translate contained in $K$.

The manuscript claims to establish that every translation cover satisfies

$$
|K| \geq \frac{\pi}{6} + 2\sqrt{3} - 3,
$$

with equality if and only if $K$ is congruent to **Duff's truncated unit square**. In particular, this would settle the minimum-area translation-cover problem, a translation-only variant of **Lebesgue's universal covering problem**.

The proof uses placements of Reuleaux triangles, estimates for vertical sections of convex bodies, and explicit arithmetic comparisons. Appendix A contains Python code for verifying the finite rational-arithmetic comparisons.

## Manuscript status and AI disclosure

This repository makes the preliminary manuscript publicly available to document the author's claimed priority for the result. The statement at the top of this README reproduces the notice printed above the title in the PDF. The manuscript also includes an AI disclosure near its references.

The author developed the proof in collaboration with ChatGPT, which generated this version of the manuscript, including its LaTeX source and verification code. The author plans to revise the manuscript before posting a revised version on arXiv.

This preliminary release should not be confused with independent verification or peer review of the proof.

## Versions and publication date

The date **November 23, 2026** is the date printed on the manuscript. For the actual public-release date and a version-specific record, please consult this repository's **Releases** page. Subsequent revisions should be published as separate releases, preserving the original version for reference.

## Keywords

Translation cover; minimum-area translation cover; translative covering; Lebesgue's universal covering problem; Duff's truncated square; Reuleaux triangle; bodies of constant width; convex geometry; geometric covering; shape optimization.
