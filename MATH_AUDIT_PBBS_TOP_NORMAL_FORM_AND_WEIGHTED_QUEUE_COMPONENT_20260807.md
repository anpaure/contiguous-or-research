# Independent audit of the PBBS top normal form and the weight-\(d+1\) queue component

**Date:** 2026-08-07  
**Method:** disjoint deletion accounting under residence, followed by a
literal specialization of the weighted phase queue  
**Status:** the claimed rank formula and the local weighted-queue
construction are correct in the parameter ranges stated below. They close
one finite top-row component, not the complete SCD common-history gate.
No computation is used.

## 1. Forced intersection rank

Let

\[
 S_0,S_1,\ldots,S_{L-1}\in{[n]\choose\rho}
\tag{1.1}
\]

be a cyclic sequence with \(L\ge d\), \(d\ge1\), such that

\[
 d_J(S_i,S_{i+1})=d+1
\tag{1.2}
\]

for every \(i\). Assume every nonconstant positive coordinate run in the
cyclic membership trace has length at least \(d\). Put

\[
 B_p=\bigcap_{j=0}^{d-1}S_{p+j}.
\tag{1.3}
\]

### Theorem 1.1 (exact top-atom rank)

For every \(p\),

\[
 \boxed{|B_p|=\rho-(d-1)(d+1).}
\tag{1.4}
\]

In the PBBS top row,

\[
 \rho=m-d-1,
\tag{1.5}
\]

so

\[
 \boxed{|B_p|=m-d(d+1).}
\tag{1.6}
\]

#### Proof

For the \(d-1\) transitions inside the block
\(S_p,\ldots,S_{p+d-1}\), define

\[
 D_i=S_i\setminus S_{i+1}.
\]

Every \(D_i\) has size \(d+1\).

Each deleted coordinate belongs to \(S_p\). Otherwise its final positive
run before deletion would have started at an insertion during one of the
preceding transitions in the same block and would have length at most
\(d-2\), contradicting residence.

The deletion sets are pairwise disjoint. If one coordinate were deleted
twice, it would have to be reinserted between the two deletions, and its
new positive run would again have length at most \(d-2\).

Therefore a coordinate of \(S_p\) survives all \(d\) targets exactly when
it lies in none of the \(d-1\) disjoint deletion sets. Hence

\[
 |B_p|
 =|S_p|-\sum_{i=p}^{p+d-2}|D_i|
 =\rho-(d-1)(d+1).
\]

Substituting (1.5) gives (1.6). \(\square\)

The residence hypothesis is essential. For \(d\ge3\), alternate two
rank-\(\rho\) sets at Johnson distance \(d+1\). Every transition has the
required distance, but the intersection of \(d\) consecutive targets has
rank \(\rho-(d+1)\), not
\(\rho-(d-1)(d+1)\); the differing coordinates have positive runs of
length one.

The atoms are legal nonempty source letters only when

\[
 m>d(d+1).
\tag{1.7}
\]

At equality they are empty, so the set-theoretic top-row identity does
not yet give a literal nonempty source word.

## 2. Exact top-row realization

The positive-run condition also gives the coordinatewise identity

\[
 \boxed{
 S_e=\bigcup_{p=e-d+1}^{e}B_p.
 }
\tag{2.1}
\]

Indeed, every \(B_p\) in the displayed union is contained in \(S_e\). If
\(x\in S_e\), the positive run containing \(e\) has length at least
\(d\), and therefore contains a length-\(d\) all-\(x\) window containing
\(e\). The start of that window is one of the displayed \(p\)'s and puts
\(x\) in \(B_p\).

Thus (1.2) plus residence does more than force the atom rank: when
(1.7) holds, the delayed intersections are a literal top-row antecedent.

## 3. The explicit weighted queue

Put

\[
 p=d+1
\tag{3.1}
\]

and specialize the weighted rolling block queue to block weight

\[
 h=p.
\tag{3.2}
\]

This construction exists whenever

\[
 \boxed{p^2\le m.}
\tag{3.3}
\]

Choose a core \(K\) and \(p\) disjoint phase supports with

\[
 |K|=m-p^2,\qquad |T_a|=p+1.
\tag{3.4}
\]

At the phase-\(a\) source position in rotor round \(q\), use

\[
 A_{q p+a}=K\cup(T_a\setminus\{x_{a,q}\}),
 \qquad q\in\mathbb Z_{p+1}.
\tag{3.5}
\]

The period is

\[
 L=p(p+1).
\tag{3.6}
\]

### Theorem 3.1 (exact local top component)

The word (3.5) has all of the following properties.

1. Every \(p=d+1\) consecutive source letters have union rank \(m\).
   These owners are distinct, form a simple Johnson cycle, and have
   simple immediate lower and upper palettes.
2. Every bank coordinate has owner gap \(p\) and owner run \(p^2\);
   every core coordinate is permanent. The complete literal state
   regenerates after \(p(p+1)\) positions.
3. Every \(d=p-1\) consecutive source letters form a distinct top target
   of rank
   \[
   (m-p^2)+(p-1)p=m-p=m-d-1=\rho.
   \tag{3.7}
   \]
4. Consecutive top targets have Johnson distance
   \[
   p=d+1.
   \tag{3.8}
   \]
5. Every nonconstant positive coordinate run in the top-target trace has
   length exactly \(d\).
6. The delayed intersection atoms of the top targets are exactly the
   original source letters:
   \[
   \bigcap_{j=0}^{d-1}S_{u+j}=A_u,
   \qquad
   |A_u|=m-d(d+1).
   \tag{3.9}
   \]

#### Proof

A \(p\)-source owner window contains one \(p\)-block from every phase, so
its rank is \(|K|+p^2=m\). Shifting it replaces one \(p\)-block by the
next \(p\)-block in that phase, a one-coordinate Johnson move. The
standard weighted-queue argument gives owner simplicity, both q1
palettes, gap/run residence, and regeneration.

A \(d=p-1\) source window meets \(p-1\) different phases and hence has
rank (3.7). On shifting, it drops a \(p\)-block from one phase and adds a
disjoint \(p\)-block from the unique formerly inactive phase. This proves
(3.8).

A bank coordinate is present at \(p\) of the \(p+1\) source updates of
its phase. One present source occurrence belongs to exactly \(d=p-1\)
consecutive top windows. Consecutive occurrences of that phase are
separated by \(p\) source positions, so their length-\(d\) top-window
supports are separated by one zero position. Thus every positive top run
has length exactly \(d\). Core coordinates are constant.

Finally, \(A_u\) lies in each of the \(d\) top targets ending at
\(u,\ldots,u+d-1\). Their intersection has rank
\(m-d(d+1)=|A_u|\) by Theorem 1.1, so the containment is equality. This
proves (3.9). \(\square\)

The used ground set has size

\[
 |K|+p(p+1)=m+p\le2m+1,
\tag{3.10}
\]

which follows from (3.3). Equality \(m=p^2\) is allowed: the core is
empty but every source atom still has rank \(p>0\).

At triangular depth,

\[
 \frac{p^2}{m}\longrightarrow\frac{\pi}{4}<1,
\tag{3.11}
\]

so (3.3) holds for all sufficiently large dimensions.

## 4. What the component does not prove

The construction is **dense only inside its own component**: every one of
its \(p(p+1)\) endpoints carries a valid top target. It does not order the
complete top layer

\[
 { [n]\choose m-d-1},
\tag{4.1}
\]

whose size is exponential in \(n\). No theorem here packs
coordinate-labelled copies of the component target-disjointly, joins
them into one chronology, or assigns the shorter members of all SCD
pieces.

For a shorter interval of \(q<d\) consecutive queue atoms, the literal
union is

\[
 K\cup\bigcup_{\text{\(q\) active phases}}
       (T_a\setminus\{x_{a,\cdot}\}),
\qquad
 \left|\bigcup A\right|=m-p^2+qp.
\tag{4.2}
\]

Each active phase block has its own physical atom, so these particular
shorter values have exact private allowed points. But their ranks advance
in steps of \(p=d+1\), not in the unit steps of a saturated SCD chain.
They therefore do not realize the arbitrary shorter SCD targets required
by the global common-history theorem.

The proof-safe conclusion is

\[
 \boxed{
 \text{the top normal form and the weight-\(d+1\) queue close one local
 top component, not the complete literal common-history gate}.}
\tag{4.3}
\]
