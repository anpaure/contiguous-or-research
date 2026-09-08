# Dense top rows have a delayed-intersection normal form, realized by the weight-\(d+1\) block queue

**Date:** 2026-08-07  
**Method:** coordinate run decomposition, consecutive deletion banks, and
the weighted rolling block queue  
**Status:** unconditional exact normal form and explicit cyclic local
factor.  It closes the literal common-history, flat-owner, local \(q1\),
residence, and regeneration rows for one dense top component.  It does not
factor the complete rank-\((t-1)\) target layer, realize the lower SCD
flags, cover the full upper deck, fuse all owner components, or supply the
terminal compiler.

## 1. Setup

Put

\[
 q=d+1,\qquad r=t-1=m-d-1=m-q,
\tag{1.1}
\]

and let

\[
 S_e\in {[n]\choose r}\qquad(e\in\mathbb Z_L)
\tag{1.2}
\]

be a cyclic sequence with one top target at every endpoint.  Define its
maximal delayed atoms and central owners by

\[
 B_p:=\bigcap_{j=0}^{d-1}S_{p+j},
 \qquad
 O_e:=S_{e-1}\cup S_e.
\tag{1.3}
\]

For two equal-rank sets, write

\[
 d_J(X,Y)=|X\setminus Y|=|Y\setminus X|.
\tag{1.4}
\]

All indices below are cyclic.

## 2. Exact necessary and sufficient conditions

### Theorem 2.1 (dense top-row normal form)

The delayed atoms realize every top target,

\[
 \boxed{S_e=\bigcup_{p=e-d+1}^{e}B_p\quad(e\in\mathbb Z_L),}
\tag{2.1}
\]

if and only if every cyclic positive run in every coordinate-membership
word

\[
 \bigl({\bf1}_{x\in S_e}\bigr)_{e\in\mathbb Z_L}
\tag{2.2}
\]

has length at least \(d\).

When (2.1) holds, the \((d+1)\)-window union of the atom word is exactly

\[
 \bigcup_{p=e-d}^{e}B_p
 =S_{e-1}\cup S_e=O_e.
\tag{2.3}
\]

Moreover, the owners all have rank \(m\) if and only if

\[
 \boxed{d_J(S_{e-1},S_e)=q=d+1\quad\text{for every }e.}
\tag{2.4}
\]

Assume (2.4), and put

\[
 L_e=S_{e-1}\setminus S_e,
 \qquad
 R_e=S_{e+1}\setminus S_e.
\tag{2.5}
\]

Thus \(|L_e|=|R_e|=q\).  Consecutive owners are distinct Johnson
neighbours if and only if

\[
 \boxed{|L_e\cap R_e|=q-1=d\quad\text{for every }e.}
\tag{2.6}
\]

The owner cycle is simple if and only if, in addition,

\[
 e\longmapsto S_{e-1}\cup S_e
\tag{2.7}
\]

is injective.  Local Johnson adjacency alone does not exclude a
nonconsecutive repeated owner.

#### Proof

For a coordinate \(x\), one has \(x\in B_p\) precisely when the length-
\(d\) window starting at \(p\) is all one in (2.2).  Hence an occurrence
\(x\in S_e\) lies in the right side of (2.1) precisely when its positive
run contains a length-\(d\) window containing \(e\).  This holds at every
positive occurrence exactly when every positive run has length at least
\(d\).  This proves the first assertion.  Taking the union of the two
adjacent identities in (2.1) gives (2.3).

Since both targets in (1.3) have rank \(r\),

\[
 |O_e|=|S_{e-1}\cup S_e|=r+d_J(S_{e-1},S_e).
\]

Together with \(m-r=q\), this proves (2.4).  Finally

\[
 O_e=S_e\mathbin{\dot\cup}L_e,
 \qquad
 O_{e+1}=S_e\mathbin{\dot\cup}R_e,
\]

so

\[
 d_J(O_e,O_{e+1})
 =|L_e\setminus R_e|
 =q-|L_e\cap R_e|.
\]

This equals one exactly in (2.6).  Equation (2.7) is exactly global owner
distinctness. \(\square\)

Thus the complete set-theoretic test is: positive \(d\)-residence for
literal reconstruction, distance \(q\) for owner rank, the triple-overlap
identity (2.6) for owner adjacency, and global injectivity (2.7) for a
simple owner cycle.

### Corollary 2.2 (the exact local \(q1\) colours)

Under (2.4)--(2.6), put \(C_e=L_e\cap R_e\).  The immediate lower and
upper colours on the owner edge \(O_eO_{e+1}\) are

\[
 \boxed{
 Q^-_e=O_e\cap O_{e+1}=S_e\mathbin{\dot\cup}C_e,
 \qquad |Q^-_e|=m-1,
 }
\tag{2.8}
\]

and

\[
 \boxed{
 Q^+_e=O_e\cup O_{e+1}
       =S_e\mathbin{\dot\cup}(L_e\cup R_e),
 \qquad |Q^+_e|=m+1.
 }
\tag{2.9}
\]

Consequently the two local \(q1\) palettes are simple exactly when the
two maps \(e\mapsto Q^-_e\) and \(e\mapsto Q^+_e\) are injective.  Neither
injectivity follows merely from (2.4)--(2.7).

## 3. Residence forces the atom rank

The normal form has a useful rigidity which is absent from the bare
top-row equivalence.

### Theorem 3.1 (forced atom rank and sharp positivity obstruction)

Assume the positive-run condition of Theorem 2.1 and the distance
condition (2.4).  Then every delayed atom has the same rank

\[
 \boxed{|B_p|=r-(d-1)q=m-d(d+1).}
\tag{3.1}
\]

In particular, a nonempty literal delayed-atom realization satisfying the
flat rank-\(m\) owner condition can exist only if

\[
 \boxed{m>d(d+1).}
\tag{3.2}
\]

#### Proof

At the transition \(S_{i-1}\to S_i\), let

\[
 D_i=S_{i-1}\setminus S_i.
\]

By (2.4), \(|D_i|=q\).  Consider
\(D_{p+1},\ldots,D_{p+d-1}\).  Every member of \(D_{p+j}\) lies in
\(S_p\): its positive run ends at \(p+j-1\), and residence says that this
run contains the preceding \(d\) target positions, including \(p\).

These \(d-1\) deletion sets are pairwise disjoint.  Indeed, if one
coordinate were deleted at two of these transitions, then after its first
absence its next positive run would end at the second deletion in fewer
than \(d\) positions, contradicting residence.  A coordinate of \(S_p\)
survives all of \(S_p,\ldots,S_{p+d-1}\) exactly when it belongs to none
of these deletion sets.  Therefore

\[
 B_p
 =S_p\setminus\bigcup_{j=1}^{d-1}D_{p+j},
\]

and (3.1) follows.  If the value in (3.1) is negative, the hypotheses are
already inconsistent.  If it is zero, every maximal atom is empty, so
(2.1) cannot reconstruct the nonempty rank-\(r\) targets.  This proves
the strict inequality (3.2). \(\square\)

Equation (3.1) is stronger than an average incidence bound: it fixes the
rank of every literal source letter in this normal form.

## 4. The explicit weight-\(d+1\) block queue

The general weighted block queue in
`MATH_THEOREM_RANK2_BLOCK_QUEUE_FLAT_OWNER_RESET_20260807.md` contains an
exact dense-top specialization which was not used by its rank-two
application.

Assume

\[
 q^2=(d+1)^2\le m.
\tag{4.1}
\]

Choose pairwise disjoint sets

\[
 K,F_0,F_1,\ldots,F_{q-1}
\tag{4.2}
\]

with

\[
 |K|=m-q^2,
 \qquad
 F_a=\{x_{a,0},x_{a,1},\ldots,x_{a,q}\}.
\tag{4.3}
\]

The construction uses \(m+q\le n\) coordinates.  For

\[
 i=uq+a,\qquad 0\le a<q,\quad u\in\mathbb Z_{q+1},
\]

define a cyclic atom word of length

\[
 \ell=q(q+1)=(d+1)(d+2)
\tag{4.4}
\]

by

\[
 \boxed{B_i=K\cup(F_a\setminus\{x_{a,u}\}).}
\tag{4.5}
\]

Define the top targets and owners literally from this word:

\[
 S_e=\bigcup_{p=e-d+1}^{e}B_p,
 \qquad
 O_e=\bigcup_{p=e-d}^{e}B_p.
\tag{4.6}
\]

### Theorem 4.1 (explicit dense top component)

The word (4.5) has all of the following properties.

1. Its letters have the forced rank

   \[
   |B_i|=m-d(d+1)>0.
   \tag{4.7}
   \]

2. Every top target has rank \(r=m-d-1\), all \(\ell\) top targets are
   distinct, and the maximal delayed intersection of the target sequence
   is exactly the original letter (4.5).

3. Every owner has rank \(m\), the \(\ell\) owners are distinct, and they
   form a simple Johnson cycle.

4. Both immediate \(q1\) palettes \((Q^-_e)\) and \((Q^+_e)\) are
   simple.

5. Every positive run in the top-target membership words has length at
   least \(d\).  Thus (4.5) is a literal common-history realization, not
   merely an abstract owner cycle.

6. In the owner sequence, every noncore coordinate has one gap of length
   \(q=d+1\) and one run of length \(q^2\).  Hence the owners are
   bi-resident through depth \(d\).  The complete omission and age state
   regenerates after \(\ell\) positions.

#### Proof

A top window in (4.6) has length \(d=q-1\).  It meets \(q-1\) different
phase supports and contains a \(q\)-set from each, so

\[
 |S_e|=|K|+(q-1)q=m-q=r.
\]

An owner window has length \(q\).  It meets every phase once, and hence

\[
 |O_e|=|K|+q^2=m.
\]

Moving the owner window updates one phase from
\(F_a-x_{a,u-1}\) to \(F_a-x_{a,u}\), one Johnson exchange.  Before
\(q(q+1)\) updates at least one phase omission has not returned, which
proves owner simplicity and regeneration.  The missing phase of a proper
top window recovers its endpoint residue modulo \(q\), and the visible
omissions recover \(u\); hence the top targets are also distinct.

At an owner edge, the lower colour has two omissions in the updated phase
and one in every other phase.  The upper colour has the entire updated
phase and one omission in every other phase.  These patterns recover the
updated phase and rotor time, proving simplicity of both palettes.

Every target is, by definition, the union of the \(d\) indicated letters,
so its positive coordinate runs have length at least \(d\).  Theorem 3.1
and (4.7) then show that the maximal intersection atom has the same rank as
the contained letter \(B_i\), and therefore equals it.  Finally, one
omission state of a phase persists for \(q\) owner positions; the other
\(q\) omission states persist for \(q^2\) positions.  This gives the
claimed owner residence. \(\square\)

This is exactly Theorem 2.1 of the weighted block-queue note with

\[
 p=d+1,\qquad h=d+1.
\tag{4.8}
\]

The earlier rank-two use took \(h=2\).  At \(h=2\), the depth-\(d\)
suffix has rank \(m-2\), not \(m-d-1\); it therefore does not instantiate
the dense top row.  The single-bulge and moving-bank single-bulge
constructions likewise have depth-\(d\) maximum rank \(m-1\) and a
triangular mixed-rank profile.  They satisfy valuable local owner and
reset statements but are not instances of (1.2).

## 5. Exact closed and open rows

Theorem 4.1 closes, for one cyclic component:

* nonempty source letters equal to the maximal delayed atoms;
* exact realization of every selected rank-\((t-1)\) top target;
* a flat simple rank-\(m\) owner row;
* simple immediate lower and upper \(q1\) palettes;
* top positive residence, owner bi-residence, and literal regeneration.

It does **not** prove a factor of the complete target layer

\[
 {[n]\choose t-1}.
\tag{5.1}
\]

One queue ring contains only \((d+1)(d+2)\) specially structured targets.
Selecting target-disjoint labelled rings covering every required top
target, coupling their shorter suffix unions to the prescribed lower SCD
flags, and fusing their owner cycles are new occurrence-level problems.
Also, local simplicity of (2.8)--(2.9) is not global \(q1\) surjectivity,
and none of the arbitrary-width upper deck or terminal compiler follows.

Thus the dense top-row architecture is locally constructible and has no
rank, adjacency, residence, or immediate-palette obstruction in the
triangular regime, where (4.1) holds eventually.  The exact remaining
theorem is a simultaneous labelled block-queue factor and residual SCD
completion, not another local source-word identity.
