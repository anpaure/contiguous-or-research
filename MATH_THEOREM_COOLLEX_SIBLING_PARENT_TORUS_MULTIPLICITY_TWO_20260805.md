# One promoted torus carries at most two ports from a cool-lex sibling rail

**Date:** 2026-08-05  
**Method:** cyclic weak-composition bank multisets; no search  
**Status:** unconditional.  This rules out a long same-torus arithmetic
port orbit inside one sibling family and reduces the recursive directed
splice state to singleton and paired native port blocks.

## 1. The promoted sibling ports

At one cool-lex recursive call, the promoted marked ports have binary form

\[
 p_a=0^{s-1}1^a0001^{T-a}\gamma,
 \qquad 0\le a\le E-1,
\tag{1.1}

where `T=t-1` and `E` is the number of sibling edges in the call.  The
displayed `000` contains the inserted marked zero pair.

We are in the PBBS hook range `h>=3`, so the promoted vacancy count is
`Q=2h+1>=7`.  In particular at least one zero lies outside the displayed
triple.  The one-runs on the two sides of that triple therefore belong to
two distinct cyclic vacancy banks.

Pass from the binary word to its cyclic weak composition: each zero is a
vacancy slot, and its entry is the length of the one-run immediately after
it.  There are constants `L,R>=0`, depending only on the fixed exterior
word and on whether an exterior one-run merges cyclically into one of the
two displayed runs, such that the complete multiset of vacancy-bank counts
of `p_a` is

\[
                         \mathcal S\mathbin{\dot\cup}
                         \{L+a,\ R+T-a\}.
\tag{1.2}

Here `cal S` is independent of `a`.  Zero entries are retained, so (1.2)
also covers either endpoint where one displayed one-run is empty.

Indeed, moving the marked triple-zero block through the fixed one-run
changes only the bank immediately before the block and the bank immediately
after it.  Every other vacancy bank belongs to the fixed exterior word.

## 2. Multiplicity theorem

### Theorem 2.1

Fix one unmarked promoted PBBS torus.  Among the ports

\[
                         p_0,p_1,\ldots,p_{E-1},
\]

at most two lie on that torus.

More precisely, if `p_a` and `p_b` are cyclic rotations of the same weak
composition, then either

\[
                         b=a,
\tag{2.1}

or

\[
                         b=R+T-L-a.
\tag{2.2}

Thus a fixed `a` has at most one distinct same-torus partner.

### Proof

Cyclic rotation preserves the multiset of all vacancy-bank counts.
Equating (1.2) for `a` and `b` gives

\[
 \mathcal S\mathbin{\dot\cup}\{L+a,R+T-a\}
 =
 \mathcal S\mathbin{\dot\cup}\{L+b,R+T-b\}.
\tag{2.3}

Finite multisets form a cancellative commutative monoid, even when entries
repeat.  Cancelling `cal S` yields

\[
 \{L+a,R+T-a\}=\{L+b,R+T-b\}.
\tag{2.4}

Either the two terms agree in the displayed order, giving `a=b`, or they
are exchanged.  In the latter case

\[
 L+a=R+T-b,
 \qquad R+T-a=L+b,
\]

and both equations give (2.2).  There is only one such `b`.  `square`

### Corollary 2.2 (native port order is binary)

Within one sibling family, an original promoted factor component contains
either one demanded marked port or two.  A two-element cyclic order equals
its inverse, so the PBBS moment congruence

\[
                         Bs\equiv-3\pmod Q
\]

creates no orientation choice beyond naming which two cuts share the
component.

In particular, the abstract linear-cycle example obtained by putting an
entire long sibling label orbit on one arithmetic third-shore cycle cannot
arise from the ports of a single cool-lex sibling call.

### Corollary 2.3 (one global reflection)

The constants `L,R,T` are fixed throughout the sibling call.  Hence every
nontrivial same-torus pair belongs to the same partial reflection

\[
                         a\longleftrightarrow C-a,
 \qquad C=R+T-L.
\tag{2.5}

Consequently the native pairs are nested in the linear label order; they
cannot form a general crossing matching.  After identifying paired labels,
the simple quotient of the sibling label path is a folded path.  Reflected
path edges may become parallel, but no higher-valence chord quotient is
created.

## 3. Exact remaining splice state

Contract every promoted torus used by a sibling family to a block.  By
Theorem 2.1, the label set on each block has size one or two.  The physical
third-shore problem is therefore no longer an arbitrary cyclic order on
`E` labels.  It is:

1. a partial matching `M` contained in the one reflection (2.5), whose
   pairs are the two-port native tori;
2. singleton native tori on all other labels;
3. the positive three-step angle rails between consecutive labels; and
4. the orientations/cuts used to splice these singleton and pair blocks.

A sufficient recursive theorem may now be stated sharply.

> **Pair-block port-preserving splice lemma.**  Given the path of labels
> `1,...,E`, any native matching `M` arising from (2.2), together with the
> literal positive three-step rails between consecutive labels, can be
> rethreaded so that the resulting physical third-shore permutation has
> `O(1)` cycles after composition with `beta alpha`, while exporting only
> `O(1)` boundary sockets to the parent call.

Theorem 2.1 proves that no higher-arity native port block must be handled,
and Corollary 2.3 removes arbitrary chord crossing.  It does not prove the
pair-block splice lemma.  In particular, equality of the **unmarked**
parent tori does not force a conjugating rotation to carry the distinguished
triple-zero bank of one port to that of its reflected mate.  Without that
marked positional statement, the two reflected rail C6s are not yet proved
to be aligned copies on one grandparent triple.

## 4. Relation to the moment obstruction

The cyclic-moment theorem remains necessary for identifying the actual two
occurrences on a paired native torus.  Its abstract example
`gamma_2 beta alpha` with linearly many cycles showed that arbitrary
arithmetic orders cannot be ignored.  The present theorem proves that this
particular mechanism cannot repeat more than twice inside one sibling
family.

Thus the directed contour gate has genuinely narrowed:

\[
 \boxed{\text{arbitrary port permutation}
 \quad\longrightarrow\quad
 \text{recursive singleton/pair-block splice}.}
\]

No all-depth source decoration, upper, residence, common-cap, or all-`k`
claim is included.
