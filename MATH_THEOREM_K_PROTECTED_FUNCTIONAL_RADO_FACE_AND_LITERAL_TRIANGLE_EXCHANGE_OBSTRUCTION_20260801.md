# Protected functional attachments: the exact Rado face and the first literal exchange obstruction

**Date:** 2026-08-01  
**Lane:** K, common protected flag/owner chronology  
**Status:** unconditional exact Rado theorem on the tail-invariant menu face,
an exact phase-only corollary valid after arbitrary protected contractions,
and a smallest-dimension literal proof that the unrestricted joint flag
projection is not a matroid.  This does not prove that the all-dimensional
Boolean menus satisfy the tail-invariance hypothesis, and it does not close
the `k=17` rolling-reset instance.

## 0. Outcome

Fix a bijective functional attachment

\[
                         \theta:Q\longrightarrow O.           \tag{0.1}
\]

If the complete flag table is fixed, but every head may choose among
several aligned physical columns of `theta(q)`, then the simultaneous
phase choice and predecessor matching is exactly one Rado transversal:

\[
 r_{M_P}\!\left(\bigcup_{q\in Y}{\cal A}_\theta(q)\right)
                         \ge |Y|\qquad(Y\subseteq Q).         \tag{0.2}
\]

Here `M_P` is the legal-predecessor transversal matroid.  The same theorem
holds after fixing any resource-disjoint turn bank: delete its used tails,
heads, and owners, and use the residual predecessor matroid.  In particular,
it applies verbatim to the opened seven-turn `k=17` rolling reset once a
functional owner extension `theta` is fixed.

There is one genuine joint-flag extension.  At every head root, allow a
menu of flag/attachment options which all carry the same marked-chain
resources.  If changing the option at a tail root never changes which head
options it can precede, then exact target selection plus chronology is again
the Rado system (0.2).  This is a direct two-matroid face:
partition by head roots, intersect with the predecessor transversal
matroid.

The tail-invariance hypothesis cannot simply be dropped.  At the first
literal depth-two case, `k=5`, feasible flag tables are the regular
tournaments.  Two regular tournaments which differ by reversing one
directed triangle share seven protected flags.  After contracting those
seven flags, the two residual feasible triples violate matroid basis
exchange: changing any one flag destroys state balance.  Thus even a large
protected contraction does not turn the unrestricted joint flag problem
into one matroid.

This is a structural obstruction, not an existence no-go.  Both endpoints
are valid owner-exact chronologies, and the complete `k=5` fractional face
is integral.  For `k=17`, the authenticated independent selector has a
much stronger fixed-table failure (`850/1423` after the opened reset and
`406` universally dead tails), but that remains evidence about one table,
not an all-face obstruction.

## 1. Protected functional setup

Let `P,Q` be labelled copies of one common root set, let `O` be the owner
shore, and assume

\[
                         |P|=|Q|=|O|.                         \tag{1.0}
\]

Let

\[
 {\cal S}=\{(p_i,q_i,o_i):1\le i\le h\}                     \tag{1.1}
\]

be a prescribed matching of literal turns: its tails, heads, and owners are
separately distinct.  The underlying flags at every root touched by the bank
are also prescribed consistently.  Delete the used resources and write

\[
 P'=P-\{p_i\},\qquad Q'=Q-\{q_i\},\qquad O'=O-\{o_i\}.       \tag{1.2}
\]

Fix a bijection

\[
                         \theta:Q'\longrightarrow O'         \tag{1.3}
\]

using legal aligned containments.  Thus owner exactness is already built
into the residual head choices.

First fix a complete literal flag table `F` extending the prescribed flags.
For each residual head `q`, let

\[
                         {\cal A}_\theta(q)                    \tag{1.4}
\]

be the set of all retained aligned columns at `q` whose owner is
`theta(q)`.  Parallel physical phases remain separate.  A column `a` has a
residual predecessor list

\[
 P_F^{\cal S}(a)=P_F(a)-\{p_1,\ldots,p_h\}\subseteq P'.     \tag{1.5}
\]

Let `M_P^S` be the transversal matroid on

\[
                         E=\bigcup_{q\in Q'}{\cal A}_\theta(q) \tag{1.6}
\]

represented by the bipartite graph `a--p` for
`p in P_F^S(a)`.  Let `M_Q` be the partition matroid with parts
`${\cal A}_\theta(q)`, each of capacity one.

## 2. Exact phase-Rado theorem

### Theorem 2.1 (protected aligned-column Rado criterion)

The fixed table `F` has a literal owner-exact directed cycle cover
containing `S` and using the functional attachment `theta` if and only if

\[
 r_{M_P^{\cal S}}\!\left(
       \bigcup_{q\in Y}{\cal A}_\theta(q)
                         \right)\ge |Y|
                  \qquad(Y\subseteq Q').                    \tag{2.1}
\]

Equivalently, `M_Q` and `M_P^S` have a common independent set of size
`|Q'|`.  The selected set chooses one physical attachment column at every
head and has a distinct legal predecessor at every residual tail.

#### Proof

Rado's independent-transversal theorem applied to the family of sets
`${\cal A}_\theta(q)`, `q in Q'`, in matroid `M_P^S` gives precisely the
equivalence between (2.1) and a choice

\[
                         a_q\in{\cal A}_\theta(q)             \tag{2.2}
\]

which is independent in `M_P^S`.  A transversal representation of that
independent set supplies distinct tails

\[
                         p_q\in P_F^{\cal S}(a_q).            \tag{2.3}
\]

There are `|Q'|=|P'|` such tails, so all residual tails occur.  The triples

\[
                         (p_q,q,\theta(q))                    \tag{2.4}
\]

therefore use every residual tail, head, and owner exactly once.  Add the
protected turns `S`.

Conversely, remove `S` from a cycle cover using `theta`.  Its selected
aligned columns give one member of every set (1.4), and the actual distinct
predecessor tails represent an independent transversal.  Rado's rank
inequalities follow.  \(\square\)

The theorem improves the order of quantifiers over “choose one alignment,
then test Hall”: it chooses all phases and predecessor representatives
simultaneously.  It is nevertheless an ordinary two-matroid theorem because
`theta` and `F` have already been fixed.

### Corollary 2.2 (cut form)

Condition (2.1) is equivalent to the existence of nonnegative variables
`x_(a,p)` satisfying

\[
\begin{aligned}
 \sum_{a\in{\cal A}_\theta(q)}\sum_{p\in P_F^{\cal S}(a)}x_{a,p}&=1
                                                   &&(q\in Q'),\\
 \sum_q\sum_{a\in{\cal A}_\theta(q)}x_{a,p}&=1    &&(p\in P'),\\
 \sum_{p\in P_F^{\cal S}(a)}x_{a,p}&\le1          &&(a\in E),
\end{aligned}                                                   \tag{2.5}
\]

and the polytope is integral.  This is simply the bipartite matching
polytope after the intermediate alignment columns are split; eliminating
the columns gives the Rado ranks (2.1).

Parallel aligned columns are important in (2.5).  Collapsing phases before
the predecessor lists are compared can change the rank.

## 3. A joint flag-menu Rado subclass

The preceding theorem freezes `F`.  The following condition permits the
flags and their functional columns to be chosen jointly without reintroducing
the third matroid.

For every residual head root `q`, let `${\cal L}_q` be a nonempty menu of
pairs

\[
                         c=(f_c,a_c),                          \tag{3.1}
\]

where `f_c` is a literal flag rooted at `q` and `a_c` is an aligned column
from `q` to `theta(q)`.  If a prescribed root remains on the residual head
shore, every option in its menu uses that one bank-consistent fixed flag
(although several aligned columns may remain).  If a prescribed root
remains only on the residual tail shore, retain its fixed flag as a
singleton tail menu.  This includes the two opened-reset endpoint flags.
Thus every residual tail root `p` has a tail menu

\[
 \widehat{\cal L}_p=
 \begin{cases}
  {\cal L}_p,&p\in Q',\\
  \{\text{its prescribed flag}\},&p\notin Q'.
 \end{cases}                                                 \tag{3.1a}
\]

Call the menu system **suffix-neutral** if every option in `${\cal L}_q`
has the same declared marked suffixes, and these declarations together with
the protected bank cover every required named target exactly once.

Call it **tail-invariant** if for every residual tail root `p`, every two
options `c,c' in \widehat{\cal L}_p`, and every head option `d`,

\[
 f_c\text{ can literally precede }d\text{ through }a_d
 \quad\Longleftrightarrow\quad
 f_{c'}\text{ can literally precede }d\text{ through }a_d.  \tag{3.2}
\]

For a head option `d`, equation (3.2) defines an unambiguous predecessor
root set $P(d)\subseteq P'$.

### Theorem 3.1 (tail-invariant protected flag Rado theorem)

For a suffix-neutral, tail-invariant menu system, there is a choice of one
option at every residual head which, together with `S`, gives

* the exact declared marked-chain selector;
* every root flag once;
* the functional owner attachment `theta`; and
* a literal directed cycle cover

if and only if

\[
 r_M\!\left(\bigcup_{q\in Y}{\cal L}_q\right)
                         \ge |Y|
                 \qquad(Y\subseteq Q'),                     \tag{3.3}
\]

where `M` is the transversal matroid on the option ground set represented
by `d--p` for `p in P(d)`.

#### Proof

Rado gives options `d_q in {\cal L}_q` with distinct predecessor roots
`p_q`.
Choose the corresponding flag at every residual head.  Every unprotected
root which also occurs as a tail has therefore chosen one of its menu
flags.  Tail-invariance (3.2) says that the selected flag at `p_q`, whatever
its chosen option, can precede `d_q`; hence the SDR edges are simultaneous
literal turns of the one selected table.  Cardinality saturates every
residual tail.  Functional bijectivity of `theta` supplies every owner once,
and suffix-neutrality supplies the exact marked targets.  Adding `S` gives
the stated object.

Conversely, read the selected head option and its actual predecessor from
any such object.  They form an independent transversal, so Rado gives
(3.3).  \(\square\)

This is an exact joint flag theorem, not merely a fractional statement.
Its strong hypothesis is exposed explicitly.  In ordinary literal flags,
changing the deletion word at a root usually changes its outgoing survivor
compatibility, so (3.2) is not automatic.  The phase-only family of
Theorem 2.1 is the canonical nontrivial example: its flag is fixed while its
aligned owner column varies.

### Proposition 3.2 (the complete literal host separates tail flags)

Let `2<=d<=m`, and retain the complete physical catalogue of possible head
flags and owner attachments.  Two distinct depth-`d` flags rooted at the
same rank-`m` set have different legal-successor sets.  Consequently every
tail-invariant menu relative to the complete head catalogue is a singleton.

#### Proof

Write the two flags as

\[
 f=(p;z_1,\ldots,z_{d-1}),\qquad
 f'=(p;z'_1,\ldots,z'_{d-1}).                                \tag{3.4}
\]

If `z_1!=z'_1`, choose any `beta` outside `p`, choose
`gamma in B(f)`, and let `g` have root

\[
                         q=p-\{z_1\}+\{\beta\}               \tag{3.5}
\]

and deletion word

\[
                         (z_2,\ldots,z_{d-1},\gamma).         \tag{3.6}
\]

This is a valid flag and a legal successor of `f`.  The unique element of
`p-q` is `z_1`, whereas every successor of `f'` must delete `z'_1`; hence it
is not a successor of `f'`.

If `z_1=z'_1`, let `j>=2` be the first differing deletion position and use
the same construction.  Every successor of `f` has rail prefix
`(z_2,...,z_(d-1))`, while every successor of `f'` has the primed prefix.
They differ at position `j-1`, so the constructed head distinguishes them.
The bottom set is nonempty because `d<=m`, so `gamma` always exists.
\(\square\)

Thus Theorem 3.1 does not turn the unpruned Boolean atlas into a joint Rado
problem.  A nontrivial application must deliberately prune the head support
so that a family of different tail flags becomes behaviourally identical,
or must work with alignment/phase choices which leave the flag itself fixed.

## 4. The first literal joint-selection family is not a matroid

The failure of tail-invariance is already visible at `(k,m,d)=(5,2,2)`.
A complete flag table orients every edge of `K_5`; a literal turn is a
directed two-edge path.  As proved in the three-matroid note, statewise Hall
holds exactly for the regular tournaments, and owner exactness then forces
the unique diagonal matching in each of the five `K_(2,2)` state blocks.

Label the cyclic regular tournament `T` on `Z_5` by

\[
                         i\longrightarrow i+1,i+2.            \tag{4.1}
\]

The vertices `0,1,3` form the directed triangle

\[
                         0\longrightarrow1\longrightarrow3
                           \longrightarrow0.                  \tag{4.2}
\]

Reverse all three arrows in (4.2), leaving the other seven oriented edges
fixed, and call the result `T'`.  Reversing a directed cycle preserves every
indegree and outdegree, so `T'` is another regular tournament.  Therefore
both `T` and `T'` admit functional owner-exact chronologies.

### Theorem 4.1 (protected triangle exchange obstruction)

Let `B(T)` be the ten flag options selected by `T`, viewed as a subset of
the twenty oriented-edge flag options.  The family

\[
 \{B(F):F\text{ is a literal flag table admitting a functional
 owner-exact cycle cover}\}                                  \tag{4.3}
\]

is not the family of bases of a matroid.

More sharply, contract the seven common flags of `T` and `T'`.  The two
residual feasible triples

\[
 \{0\!\to\!1,1\!\to\!3,3\!\to\!0\},\qquad
 \{1\!\to\!0,3\!\to\!1,0\!\to\!3\}                       \tag{4.4}
\]

still violate basis exchange.

#### Proof

Take `e=(0->1)` in the first triple and outside the second.  After deleting
`e`, root exactness leaves the unoriented root `{0,1}` empty.  Of the three
elements in the second triple, only `1->0` can refill that root; either of
the other two duplicates a different root and leaves `{0,1}` empty.

Flipping only `0->1` to `1->0` changes the outdegrees of `0` and `1` from
`2,2` to `1,3`.  The state block at either vertex is unbalanced, so even a
fractional directed cycle cover is impossible.  Hence no exchange element
exists.  This contradicts the basis-exchange axiom, before and after
contracting the seven common flags.  \(\square\)

The obstruction is smallest in the literal depth hierarchy: `d=2` first
becomes nontrivial at `m=2`, and a degree-preserving orientation trade has
Eulerian symmetric difference, whose smallest nonempty component is a
directed triangle.  It is not a fractional/integral gap.  Both endpoints
are integral solutions, and the complete `k=5` fractional owner face is
integral.  What fails is the claim that all feasible **flag tables** form
one matroid to which Rado could be applied.

## 5. Exact scope at the opened `k=17` reset

For the authenticated depth-three rolling reset, open the eight-cycle at one
declared boundary.  The seven retained turns use distinct tail, head, and
owner necklace resources.  Exact quotient replay proves that their seven
head--owner columns extend to a bijection `theta` on the `1430` head and
owner necklaces.  After deleting the protected resources, Theorems 2.1 and
3.1 apply with residual shore size

\[
                              1430-7=1423.                    \tag{5.1}
\]

For the independently completed static selector `F_ind`, the unrestricted
residual predecessor matching has size only

\[
                                  850<1423                    \tag{5.2}
\]

and `406` residual tails are universally dead, before `theta` is fixed.
Thus every phase-Rado instance arising from that particular `F_ind` fails;
indeed the rank of the union of all its alignment classes is at most `850`.

This is not a reset-conditioned all-face no-go.  The exact selector/reset
coexistence theorem leaves many other quotient containment matchings and
physical phases.  The proved all-dimensional statement is only the Rado
criterion: once a tail-invariant menu or a fixed-table phase family is
constructed, (2.1)/(3.3) is necessary and sufficient and protected
contraction costs no additional integrality.

The smallest still-open positive theorem is therefore:

> Jointly construct a reset-compatible exact marked flag table and a
> functional owner attachment whose residual aligned-column menus satisfy
> (2.1), or construct a nontrivial suffix-neutral tail-invariant menu system
> satisfying (3.3).

Connectivity, quotient voltage, residence outside the reset bank,
arbitrary-width upper shadows, and the terminal compiler are later rows and
are not inferred here.
