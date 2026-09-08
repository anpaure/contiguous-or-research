# Pair-cell cycles versus protected MSW rows: the exact coloured-factor gate

**Date:** 2026-08-13  
**Status:** unconditional owner/lower completion theorem and sharp protected-owner
obstruction.  It formulates exactly when prescribed pair-cell cycle edges and frozen
first-aligned MSW rows coexist at the incidence level.  Upper support and residence
remain additional joint rows, stated explicitly below.

## 1. Coloured owner factors

Put \(k=2R-1\), let

\[
 \mathcal O={ [k]\choose R},\qquad
 \mathcal L={ [k]\choose R-1}.
\]

The two shores have the same cardinality \(W\).  A coloured owner/lower factor is a
map

\[
 e:\mathcal L\longrightarrow {\mathcal O\choose2},       \tag{1.1}
\]

such that the two owners in \(e(L)\) both contain \(L\), and every owner occurs in
exactly two pairs.  Since two distinct rank-\(R\) supersets of \(L\) are Johnson
adjacent with intersection \(L\), (1.1) is precisely a simple Johnson 2-factor with
every lower colour used once.

Let \(e_0\) be the complete first-aligned MSW factor.  Freeze a family
\(\mathcal P\subseteq\mathcal L\) of its coloured edges, for example every facet of
the selected protected portal rows.  Let \(\Gamma\) be a prescribed partial Johnson
2-factor, typically a disjoint family of pair-cell cycles, and colour every edge
\(TT'\) by

\[
                         \kappa(TT')=T\cap T'.             \tag{1.2}
\]

Write \(\mathcal C=\kappa(E(\Gamma))\).

## 2. Two immediate compatibility obstructions

### Lemma 2.1 (lower-colour injection)

The edges of \(\Gamma\) can belong to an exact coloured factor only if \(\kappa\) is
injective on \(E(\Gamma)\).

For cycles internal to one fixed pair structure, an internal edge colour is a facet
with a chosen empty matched pair.  A facet empty on several matched pairs can occur as
an internal edge in several different pair cells.  Componentwise lower simplicity
therefore does not imply the global injection required here.

### Lemma 2.2 (protected-owner saturation)

Suppose \(\Gamma\) is 2-regular on its owner support \(S\).  If a protected old edge
\(e_0(L)\), \(L\in\mathcal P\), meets \(S\), then it must itself be the prescribed
\(\Gamma\)-edge of colour \(L\).  In particular, if no protected MSW edge is a desired
pair-cell edge, the pair-cell owner support must be disjoint from every owner occurring
on a protected row.

#### Proof

Each owner in \(S\) already has its two final incidences in \(\Gamma\).  A distinct
frozen edge through it would give final degree at least three.  \(\square\)

This is stronger than facet avoidance.  Freezing the coloured facets of an MSW portal
row also freezes both incident owner occurrences, so a proposed pair-cell cycle cannot
merely avoid the same colours while reusing those owners.

## 3. Exact owner/lower completion theorem

Assume Lemma 2.1 and consistency on \(\mathcal C\cap\mathcal P\): whenever a colour is
both prescribed and protected, the two prescribed edges are identical.  Let
\(\mathcal F=\mathcal C\cup\mathcal P\), and fix on every \(L\in\mathcal F\) the
corresponding edge.  If two fixed colours give an owner more than two incidences,
completion is impossible.  Otherwise put

\[
 d_T=2-\deg_{\mathcal F}(T),qquad T\in\mathcal O,         \tag{3.1}
\]

and let \(\mathcal L'=\mathcal L-\mathcal F\).  For
\(\mathcal A\subseteq\mathcal L'\), define

\[
 n_{\mathcal A}(T)=|\{L\in\mathcal A:L\subset T\}|.       \tag{3.2}
\]

### Theorem 3.1 (capacitated facet Hall criterion)

The prescribed pair-cell edges and frozen MSW rows extend to an exact owner/lower
factor if and only if

\[
 \boxed{
  \sum_{T\in\mathcal O}\min\{d_T,n_{\mathcal A}(T)\}
       \ge 2|\mathcal A|
       \quad\text{for every }\mathcal A\subseteq\mathcal L'.}
                                                               \tag{3.3}
\]

#### Proof

Build the bipartite flow network

\[
 s\longrightarrow L\longrightarrow T\longrightarrow t,
\]

with capacity two on \(sL\), capacity one on \(LT\) when \(L\subset T\), and
capacity \(d_T\) on \(Tt\).  A full integral flow chooses two distinct containing
owners for every residual facet and supplies exactly every residual owner degree.
Integrality follows from the ordinary integral max-flow theorem.

The total residual facet demand and owner capacity agree:

\[
 2|\mathcal L'|=2(W-|\mathcal F|)=\sum_Td_T.              \tag{3.4}
\]

For a fixed facet set \(\mathcal A\), the maximum amount it can send to owner \(T\)
is \(\min\{d_T,n_{\mathcal A}(T)\}\), giving necessity of (3.3).  Conversely the
usual capacitated Hall/max-flow cut condition is exactly (3.3): after fixing
\(\mathcal A\), minimizing over the owner side of a cut replaces each owner
contribution by that minimum.  Thus every source-facet arc can be saturated.

Pair the two selected endpoints of each residual facet.  Capacity one makes them
distinct.  The resulting edges, together with the fixed ones, use every lower colour
once and give every owner degree two.  \(\square\)

This theorem is an incidence theorem only.  It may create many Euler components, and
it does not preserve residence.

## 4. A stronger relative certificate

There is a simple sufficient certificate which leaves every unprescribed MSW edge
unchanged.  For \(L\in\mathcal C\), let \(e_1(L)\) be the desired pair-cell edge.

### Proposition 4.1 (same-colour relative replacement)

Assume \(\mathcal C\cap\mathcal P\) is consistent and

\[
 \sum_{L\in\mathcal C}\deg_{e_1(L)}(T)
 =
 \sum_{L\in\mathcal C}\deg_{e_0(L)}(T)
 \qquad(T\in\mathcal O).                                \tag{4.1}
\]

Then replacing \(e_0(L)\) by \(e_1(L)\) on \(\mathcal C\) and changing nothing
else gives an exact owner/lower factor.  Conversely, (4.1) is necessary for a trade
whose changed-colour set is exactly \(\mathcal C\).

Endpoint-rotation circuits and paired open paths are constructive ways to enlarge
\(\mathcal C\) until (4.1) holds while avoiding \(\mathcal P\).  Their path labels
must be mutually distinct; abstract reachability without colour disjointness is not a
trade certificate.

## 5. The immediate-upper row

For a coloured factor \(e\), define

\[
 \mu_e^+(U)=|\{L\in\mathcal L:\bigcup e(L)=U\}|,
       \qquad U\in{[k]\choose R+1}.                       \tag{5.1}
\]

In the same-colour relative certificate, old upper support is preserved exactly when

\[
 \boxed{
 \mu_{e_0}^+(U)
 +\#\{L\in\mathcal C:\bigcup e_1(L)=U\}
 -\#\{L\in\mathcal C:\bigcup e_0(L)=U\}
 \ge1
 }
                                                               \tag{5.2}
\]

for every \(U\) with \(\mu_{e_0}^+(U)>0\).  This is support monotonicity, not
multiplicity preservation and not universal upper coverage unless the base already
has it.

For a general completion from Theorem 3.1, upper coverage adds the rows

\[
 \sum_{L,\{T,T'\}:T\cup T'=U}x_{L,T,T'}\ge1.              \tag{5.3}
\]

These rows are coupled to the endpoint flow and destroy the plain bipartite-flow
reduction.  They must be proved by a support-slack argument, an upper backup atlas, or
a genuinely joint matching theorem.

## 6. Exact coexistence checklist

Thus installing pair-cell chronologies inside a protected first-aligned MSW factor
requires, in order:

1. global injectivity of their lower colours;
2. exact agreement with every protected edge meeting their saturated owner support;
3. the capacitated Hall inequalities (3.3), or a stronger relative-trade certificate;
4. upper support via (5.2), (5.3), or a named backup;
5. an occurrence chronology whose seams pass the `q`-transition-collar test.

The long-run theorem inside each pair cell supplies only the internal part of item 5.
It does not imply items 1--4, and freezing selected MSW rows makes item 2 an owner-level
constraint rather than merely a colour-level avoidance condition.
