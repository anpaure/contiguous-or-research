# Contiguous deletion runs give both anchor edge covers, but must be chosen with direct incidence

Date: 2026-07-31  
Status: complete all-`n>=6` run-bank lemma and exact finite coupling
counterexample; not a construction of the two-coordinate collar

## 0. Result

Let `F` be an oriented Catalan linear forest at parameter `n`, with
`K=Cat_n` path components and `N=nK` ordered child edges.  Put

\[
 C=\operatorname {Cat}_{n+1},\qquad R=N-C,
 \qquad H=N-\binom{2n}{n-2}=C-K.
\]

For every `n>=6`, one can choose `Q subset E(F)` with `|Q|=C` such that,
on the ordered edge lists of the child paths, `Q` consists of exactly `K`
maximal runs and every run has length at least two.

The lower-colour sequence and the upper-colour sequence along each child
path are themselves simple Johnson paths.  Consequently the consecutive
colour edges inside the `Q`-runs give, simultaneously on the two shores,

* a `K`-path forest on every lower anchor in `lower(Q)`; and
* a `K`-path forest on every upper anchor in `upper(Q)`.

Each auxiliary forest has exactly `C-K=H` edges and no isolated anchor.
These are the **unselected/direct** anchor covers in the tight-enumeration
reformulation, not the selected punctured-side forests.  Internal anchors
have degree two in these covers, so adjoining seams would violate the side
cap if one mistakenly used the covers as collar atoms.  The lemma solves
only the complementary edge-cover row inside that stronger Hamilton-cycle
scaffold.

This does **not** settle the collar.  The bank `Q` must also be a common
basis of the two strict direct-lift transversal systems.  On the chained
parameter-six child from the direct-edgewise recursion, a deterministic
run-bank furnished by the proof has zero-candidate extreme colours on both
shores.  Hence “make the runs first, match afterwards” is false.  Run
structure and direct incidence must be selected jointly.

## 1. Turn-colour paths

Write a child path as

\[
             T_0,T_1,\ldots,T_s
\]

and let

\[
 L_i=T_{i-1}\cap T_i,\qquad U_i=T_{i-1}\cup T_i
 \quad(1\le i\le s).
\]

### Lemma 1.1

Both `(L_1,...,L_s)` in `J(2n,n-1)` and `(U_1,...,U_s)` in
`J(2n,n+1)` are simple paths.

### Proof

At the common middle vertex `T_i`, write

\[
 L_i=T_i-a_i,\qquad L_{i+1}=T_i-b_i.
\]

If `a_i=b_i`, the two lower colours coincide, contradicting the lower
palette bijection of `F`; otherwise their symmetric difference is
`{a_i,b_i}`.  Thus they are distinct Johnson neighbours.  The upper case
is identical after writing

\[
 U_i=T_i+c_i,\qquad U_{i+1}=T_i+d_i
\]

and using the upper palette bijection.  `square`

## 2. The binary run lemma

Let the child path edge lengths be `ell_1,...,ell_K`, allowing zero, so

\[
                         \sum_i\ell_i=N=nK.          \tag{2.1}
\]

### Theorem 2.1

For `n>=6` there are binary words of lengths `ell_i` having in total
exactly `C` ones, exactly `K` one-runs, and no one-run shorter than two.

### Proof

A word of length `ell` can contain

\[
                         a(\ell)=\left\lfloor{\ell+1\over3}\right\rfloor
                                                               \tag{2.2}
\]

pairwise separated runs of length two.  Since

\[
 a(\ell)\ge {\ell-1\over3},
 \qquad \sum_i a(\ell_i)\ge{N-K\over3}
                         ={n-1\over3}K\ge K,          \tag{2.3}
\]

we may allocate exactly `K` runs.  Allocate at least one to every path
with `ell_i>=2`; this is possible because such a path has positive
capacity and the total capacity is at least `K`.

Let `t` and `u` be the numbers of paths of lengths one and zero.  With all
usable paths occupied, the maximum number of selected positions compatible
with the allocated run counts is

\[
                         N-2t-u.                     \tag{2.4}

Indeed each of the `K` runs costs one separating zero except that the first
run on a used path does not, while a length-one unused path costs its sole
position.  Since `t+u<=K-1`,

\[
                         2t+u\le2K-2.                \tag{2.5}

On the other hand

\[
 R=N-C={n^2-2n-2\over n+2}K\ge2K-2                 \tag{2.6}

for `n>=6`.  Hence the maximum in (2.4) is at least `C`.  The minimum is
`2K`, and

\[
                         C=\left(4-{6\over n+2}\right)K\ge2K.  \tag{2.7}

For fixed run counts, every integer between the minimum and maximum is
obtained by lengthening the runs one position at a time.  Choose total
length `C`.  `square`

### Corollary 2.2 (simultaneous anchor covers)

Let `Q` be the child edges at the one-positions.  Inside every `Q`-run,
join consecutive lower colours and consecutive upper colours.  Lemma 1.1
makes both collections linear forests.  There are `C` vertices and

\[
                   \sum_{\text{runs}}(|\text{run}|-1)=C-K=H  \tag{2.8}

edges on each shore.  Since every run has length at least two, their vertex
supports are exactly `lower(Q)` and `upper(Q)`.

These are precisely the auxiliary anchor-supported direct-edge covers
appearing in the tight-enumeration reformulation.  They solve that
complementary geometric row but neither the selected diagonal palettes nor
the collar side-degree row by themselves.

## 3. Exact coupling failure of the naive bank

Apply the constructive allocation in Theorem 2.1 to the parameter-six
forest produced by the chained strict recursion in

```text
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n5_20260731.witness.json
```

Here

```text
K=132, N=792, C=429, R=363.
```

The algorithm gives 132 runs, all of length at least two, and the two
anchor covers of Corollary 2.2.  Nevertheless, after deleting the inherited
tail bank `T(Q)`, one rank-eight upper extreme has no remaining direct-lift
candidate; dually one lower extreme has no remaining candidate after the
head deletion.  Thus this particular `Q` fails both strict direct
transversal bases before physical topology is considered.

The correct strengthened target is therefore:

> choose a size-`C` common direct basis whose edge indicator has `K`
> nontrivial runs (or another physically realizable anchor-cover state),
> and choose its two representatives and contracted topology jointly.

The theorem does not claim that the run normal form is necessary, nor that
such a jointly feasible run bank exists in every dimension.

## 4. Audit

The standard-library replay

```text
scratch/audit_catalan_contiguous_q_run_bank_20260731.py
```

checks the exact Catalan identities and inequalities, constructs the bank
on the chained parameter-six child, verifies both global anchor palettes
and every consecutive Johnson edge, and independently reproduces the two
zero-candidate direct-incidence failures.
