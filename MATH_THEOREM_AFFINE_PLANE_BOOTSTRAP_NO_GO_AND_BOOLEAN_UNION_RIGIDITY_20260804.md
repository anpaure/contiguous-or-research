# Affine-plane bootstrap no-go and the missing Boolean union rigidity

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical obstruction theorem.  It
constructs, for arbitrarily large aperture, abstract optional-gap systems
which satisfy every local conclusion of the wide-gap bootstrap theorem:
`C_4`-freeness, left degree at least three, right degree at least the
aperture, strict capacitated `2`-Hall expansion, one-token robustness, and
a unique positive minimal maximizer.  Therefore those conclusions alone
cannot close the co-small gate.  The same theorem proves that these
examples cannot occur in the Boolean middle-level incidence graph.  The
additional property which must be used next is literal-union rigidity of
Johnson cliques, not generic linear-design expansion.

No computation, search, or solver result is used.

## 0. The abstract threshold model

Let `q>=3` be a prime power and let `AG(2,q)` be the affine plane of order
`q`.  It has

\[
 v=q^2
\]

points and

\[
 b=q(q+1)
\]

lines.  Every line has `q` points, every point lies on `q+1` lines, and
every pair of points lies on a unique line.

Take the points as optional lower vertices and the lines as abstract owner
gaps.  For every line `ell`, put

\[
 G_\ell=\ell,
 \qquad g_\ell=q,
 \qquad c_\ell=2.
\tag{0.1}
\]

For a point bank `S`, define

\[
 \Psi(S)=
 \sum_\ell\bigl(|S\cap\ell|-(q-2)\bigr)_+-2|S|.
\tag{0.2}
\]

This is exactly the optional overflow functional with capacity-two
unprotected owners.

## 1. Strict two-Hall expansion

### Theorem 1.1 (affine-plane strict overflow core)

Let `B` be the full point set.  Give every line its full overflow capacity

\[
 a_\ell=(q-(q-2))_+=2.
\]

Then, for every nonempty `D subseteq B`,

\[
 \boxed{
 \sum_\ell\min\{2,|D\cap\ell|\}>2|D|.}
\tag{1.1}
\]

Consequently:

1. the point--line incidence graph is `C_4`-free;
2. its left degree is `q+1>=3` and its right degree is `q`;
3. it has an integral lower-degree-two, line-capacity-two matching;
4. that matching remains feasible after deletion of any one line-capacity
   unit; and
5. `B` is the unique inclusion-minimal and unique inclusion-maximal
   maximizer of `Psi`, with

\[
 \boxed{\Psi(B)=2q>0.}
\tag{1.2}
\]

#### Proof

Put `t_ell=|D cap ell|`.  Since `0<=t_ell<=q`,

\[
 \min\{2,t_\ell\}\ge {2t_\ell\over q}.
\]

Every point lies on `q+1` lines, so

\[
 \sum_\ell\min\{2,t_\ell\}
 \ge {2\over q}\sum_\ell t_\ell
 ={2(q+1)\over q}|D|
 >2|D|.
\]

This proves (1.1).  Two different points lie on only one common line, so
the incidence graph has no `4`-cycle.  The degree statements are the
standard affine-plane parameters.  Capacitated Hall and bipartite
integrality give the matching.  The strict cut margin is integral and
hence at least one, so deleting one capacity unit preserves every Hall
inequality.

At the full bank every line contributes two, whence

\[
 \Psi(B)=2q(q+1)-2q^2=2q.
\]

For any nonempty deletion `D`, the exact block-deletion identity gives

\[
 \Psi(B)-\Psi(B\setminus D)
 =\sum_\ell\min\{2,|D\cap\ell|\}-2|D|>0.
\]

Thus every proper subset has smaller objective, proving uniqueness of the
maximizer. \(\square\)

### Corollary 1.2 (all local aperture scales occur)

For every integer `R>=3`, choose a power of two `q>=R`.  The construction
has right minimum degree at least `R` and satisfies all conclusions of
Theorem 1.1.  In particular it models the abstract wide-gap conditions
with `R=d-3` along an unbounded sequence.

Therefore `C_4`-freeness, degrees `(3,d-3)`, strict `2`-Hall, one-token
robustness, and the trihedral-petal property do not by themselves rule out
a positive optional obstruction.

## 2. Why the affine plane is not a Boolean owner system

The affine construction is an abstract linear incidence design.  We now
show exactly which Boolean property it violates.

### Lemma 2.1 (Johnson clique classification)

Let `mathcal A` be a pairwise adjacent family of `k`-sets.  Then one of
the following holds:

1. all members of `mathcal A` contain one fixed `(k-1)`-set; or
2. all members of `mathcal A` lie inside one fixed `(k+1)`-set.

#### Proof

Choose distinct

\[
 A=R\cup\{a\},
 \qquad B=R\cup\{b\},
 \qquad |R|=k-1.
\]

A `k`-set adjacent to both either contains `R`, or has the form

\[
 (R\setminus\{r\})\cup\{a,b\}
\]

and hence lies in `A union B`.  A member of the first type using a new
coordinate outside `{a,b}` is not adjacent to a member of the second
type.  Thus the whole clique has one of the two displayed forms.
\(\square\)

### Theorem 2.2 (literal-union nonembedding)

For `q>=3`, there do not exist injections

\[
 \phi:\operatorname{Pts}(AG(2,q))
       \longrightarrow\binom{[2m-1]}{m-1},
\]

\[
 \eta:\operatorname{Lines}(AG(2,q))
       \longrightarrow\binom{[2m-1]}m
\]

such that

\[
 p\in\ell
 \Longrightarrow
 \phi(p)\subset\eta(\ell).
\tag{2.1}
\]

#### Proof

Every two affine points lie on a common line.  Their two distinct
rank-`m-1` images therefore lie in one rank-`m` owner, so they are Johnson
adjacent and their owner is forced to be their literal union.  Hence the
entire point image is a Johnson clique.

Apply Lemma 2.1 with `k=m-1`.

If all point images lie in one fixed rank-`m` set, the literal union of
every pair is that same owner.  Since every affine line contains at least
two points, all line images would coincide, contradicting injectivity of
`eta`.

If instead all point images contain one fixed rank-`m-2` core, a rank-`m`
owner contains at most two of them: it has room for only two coordinates
outside the core.  But every affine line contains `q>=3` points.  This is
again impossible. \(\square\)

## 3. Sharp implication for the co-small programme

The abstract affine plane proves a genuine no-go:

\[
 \boxed{
 \text{local bootstrap degrees + linearity + strict two-Hall}
 \not\Longrightarrow\text{absence of positive obstruction}.}
\]

The property omitted by that abstraction is:

> **Boolean literal-union rigidity.**  If two lower vertices share an
> owner, they must be Johnson adjacent and that owner is uniquely their
> set-theoretic union.  Large collections of mutually co-owned pairs are
> consequently constrained by the star/top classification of Johnson
> cliques.

Thus the next noncircular theorem must exploit the actual coordinate
labels of the bouquet petals, not only their incidence graph.  One useful
target is a Boolean stability theorem of the following form:

> A localized, one-token-robust `(2,a)`-Hall bouquet complex with right
> aperture `Omega(d)` either concentrates inside a bounded union of
> literal Johnson star/top intervals, already covered by the
> subcube/DNF/Macaulay theorems, or has enough forced coordinate-union
> expansion to violate the localization bound.

The affine-plane example shows why a proof phrased only in terms of
`C_4`-free incidence expansion cannot establish this statement.

## 4. Dependency

| role | file | SHA-256 |
|---|---|---|
| wide-gap optional bootstrap core and strict internal Hall | `MATH_THEOREM_CO_SMALL_WIDE_GAP_BOOTSTRAP_CORE_AND_COMPRESSION_BARRIER_20260804.md` | `159ef7c2acd1a1106409912920b5f40b44c6ff8356712c0b20f02c2190b12805` |
