# A compressed two-star obstruction to arbitrary named bulk lifting

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional counterexample to the proposed automatic
per-rank named-lift theorem.  The obstruction uses distinct singleton
chunk tops strictly below the collar, not duplicated request labels.  It
does not obstruct a co-chosen spread naming.

## 0. The proposed automatic statement

Work in `B_(2r)` and fix `u<=r`.  Let

\[
 \mathcal B_{u-1}\longleftrightarrow\mathcal B_u
\tag{0.1}
\]

be the Boolean inclusion graph.  Add request vertices `x_i`, each adjacent
to every rank-`u` set containing a prescribed distinct top `S_i` of rank
at most `u-1`.  The tempting assertion was:

> if the number of requests is at most
> `H_u=C_u-C_(u-1)`, then the augmented graph always has a matching
> saturating `mathcal B_(u-1)` and all requests.

Equivalently, arbitrary distinct named chunk tops would always admit
independent representatives in the dual collar-start matroid.

That assertion is false already at `u=r`.

## 1. Exact two-star counts

Fix a two-set

\[
                         A=\{1,2\}.
\tag{1.1}
\]

Let

\[
 \mathcal Y={Y\in\mathcal B_{r-1}:A\subset Y\},
 \qquad
 \mathcal U={U\in\mathcal B_r:A\subset U\}.
\tag{1.2}
\]

Every rank-`r` superset of a member of `mathcal Y` contains `A`, and every
member of `mathcal U` contains a rank-`r-1` set containing `A`.  Therefore

\[
                         N(\mathcal Y)=\mathcal U.
\tag{1.3}
\]

Their sizes are

\[
 |\mathcal Y|=\binom{2r-2}{r-3},
 \qquad
 |\mathcal U|=\binom{2r-2}{r-2}.
\tag{1.4}
\]

Since

\[
 { |\mathcal Y|\over|\mathcal U|}={r-2\over r+1},
\]

the available ordinary-Hall surplus inside the two-star is

\[
 |\mathcal U|-|\mathcal Y|
 ={3\over r+1}|\mathcal U|.
\tag{1.5}
\]

Put `W=C_r=binom(2r,r)`.  The complete collar-start budget at rank `r` is

\[
                         H_r={W\over r+1}.
\tag{1.6}
\]

Also

\[
 { |\mathcal U|\over W}
 ={r-1\over2(2r-1)}.
\tag{1.7}
\]

Combining (1.5)--(1.7),

\[
 H_r-(|\mathcal U|-|\mathcal Y|)
 ={W\over2(2r-1)}
 ={1\over r}\binom{2r-2}{r-1}
 =\operatorname{Cat}_{r-1}>0.
\tag{1.8}
\]

Thus the two-star has exactly `Cat_(r-1)` fewer spare right vertices than
the complete rank-`r` start budget.

The two-coordinate star is the first member of this family which obstructs
the full budget.  For a fixed `a`-set `A`, the star surplus divided by
`H_r` is

\[
 (a+1){\binom{2r-a}{r-a}\overinom{2r}r}.
\tag{1.9}
\]

At `a=1` this ratio is exactly one; at `a=2` it is strictly below one by
(1.8).

## 2. There are enough legal low-rank request tops

Let `D=Theta(sqrt(r))` be the old coefficient-one depth and let the new
collar bottom be

\[
                         b=r-D-1.
\tag{2.1}
\]

Take singleton residual chunks whose tops have rank

\[
                         s=b-1=r-D-2.
\tag{2.2}
\]

The number of distinct such tops containing `A` is

\[
                         \binom{2r-2}{s-2}
                         =\binom{2r-2}{r-D-4}.
\tag{2.3}
\]

This is `Theta(W)`.  Indeed, relative to the central coefficient of
`B_(2r-2)`, its ratio is

\[
 \prod_{j=0}^{D+2}{r-1-j\over r+j}.
\tag{2.4}
\]

Since `D=Theta(sqrt(r))`, the logarithm of (2.4) is `-O(D^2/r)=O(1)`;
the product is bounded below by a positive absolute constant for all
sufficiently large `r`.  The central coefficient of `B_(2r-2)` is itself
`Theta(W)`.  Hence (2.3) exceeds

\[
                         H_r={W\over r+1}
\tag{2.5}
\]

eventually.

Choose exactly `H_r` distinct rank-`s` sets containing `A`, and make each
one the top of a length-one residual chunk assigned to a rank-`r` collar
socket.  These are pairwise target-disjoint legal chunks: `s<b`, and the
rank-`r` socket has new capacity `D+1>=1`.

## 3. Exact augmented-Hall failure

Let `mathcal X` be the `H_r` request vertices just chosen.  Every request
neighbour is a rank-`r` superset of its top and therefore belongs to
`mathcal U`.  Together with (1.3),

\[
 N(\mathcal Y\cup\mathcal X)=\mathcal U.
\tag{3.1}
\]

But (1.8) gives

\[
 |\mathcal Y|+|\mathcal X|-|\mathcal U|
 =\operatorname{Cat}_{r-1}>0.
\tag{3.2}
\]

So Hall fails.  There is no matching saturating the complete
rank-`r-1` shore together with these requests.

Equivalently, if `mathsf K_r` is the dual Boolean inclusion-transversal
start matroid and

\[
 N(\mathcal X)=
 \bigcup_{S\in\mathcal X}{T\in\mathcal B_r:S\subset T\},
\]

then

\[
                         r_{\mathsf K_r}(N(\mathcal X))<H_r
                         =|\mathcal X|.
\tag{3.3}
\]

Thus the exact Rado cut fails although all chunk tops are distinct and lie
`D+2` ranks below the owner layer.

## 4. Maximal orbit extraction and the `+1` reserve do not create slack

The obstruction persists after reserving any polynomial-size exceptional
bank.  Let `p<=r` rank-`r` starts be reserved in advance, and choose

\[
                         m=H_r-p
\tag{4.1}
\]

distinct rank-`s` request tops containing `A`.  The same Hall witness has
deficiency

\[
 |\mathcal Y|+m-|\mathcal U|
 =\operatorname{Cat}_{r-1}-p>0
\tag{4.2}
\]

for all sufficiently large `r`.

There is also no complete-layer orbit batch to extract from this class.
Its top rank has

\[
 C_s=\binom{2r}{r-D-2}=\Theta(W),
 \qquad
 m<H_r={W\over r+1}<C_s.
\tag{4.3}
\]

Hence the maximal number `floor(m/C_s)` of complete rank-`s` batches is
zero.  The entire class remains a partial remainder.  Relative to the
unreserved rank-`r` start bank, its count is

\[
                         m=H_r-p,
\tag{4.4}

\]

so it is exactly saturated and has no fixed positive slack.

In particular, the vanishing-singleton insurance theorem reserves fewer
than `r` maximum starts for its rounding residue.  Taking `p` equal to that
reserve leaves the compressed partial class obstructed by (4.2).  Thus the
`+1` shift solves the exceptional bank but does not, by arithmetic alone,
place every remaining partial class in the fixed-relative-slack regime of
the random spread theorem.

## 5. Scope and consequence

This counterexample proves that no direct rank lower bound depending only
on

* distinctness of the chunk tops;
* the request count `m<=H_u`;
* the legal load inequality; and
* ordinary normalized matching of the Boolean lattice

can close arbitrary fixed namings.  Compression does not remove the
problem: the compressed two-star is itself the obstruction.

It does **not** show that the anonymous interval schedule lacks a good
named lift.  The interval Boolean theorem is free to choose which literal
sets occupy its rows.  A co-chosen spread naming can avoid concentrating a
full socket class inside one small coordinate star.  The surviving bulk
target is therefore a balanced-naming theorem, not an automatic theorem
for every fixed naming.
