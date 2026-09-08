# Promotion rings at the critical annulus: a paired quotient-chain theorem, the block-factor depth barrier, and the lower-projection collapse of the amplified triangle

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web input is used.

## 0. Exact outcome

Write

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 \lambda_q={W\over N_q},\qquad q_0=\lceil m^{1/4}\rceil .
 \tag{0.1}
\]

For the literal covering calculation it is important not to choose the
outer radius only up to an unspecified additive constant.  In this note
the radius is the covering-side integer

\[
 H=\max\{0\le h<m:\lambda_h\le m+h\},\qquad M=m+H,
 \tag{0.2}
\]

and all assertions are for sufficiently large \(m\).  Then

\[
 H=(1+o(1))\sqrt{m\log m},
 \quad MN_H=W+E,
 \quad 0\le E=O(WH/m)=o(W),
 \tag{0.3}
\]

\[
 N_H=(1+o(1)){W\over m}=o(W/H),\qquad
 2HN_H=o(W).
 \tag{0.4}
\]

The conclusions are as follows.

1. There is a genuinely two-sided common-history theorem.  If, on a
   set of physical phase occurrences, the paired lower/upper trace maps

   \[
      \Theta_q(e)=(\Phi_q^-(e),\Phi_q^+(e))
   \]

   form a quotient chain and the two coordinate projections of every
   paired image are injective, then there are nested integral phase sets
   which simultaneously cover both signed images at every depth.  The
   proof is an elementary representative-extension argument; it is not
   a collection of separate Hall matchings.

2. This theorem plugs literally into the factor-blind OR compiler.  A
   one-frame-per-root atlas satisfying the paired quotient hypotheses,
   middle collision excess \(o(W)\), weighted shallow defect \(o(W)\),
   and aggregate paired deep defect \(o(W)\), gives a word of length
   \(W+o(W)\).  The exact finite upper bound is (4.5) below.  It includes
   every collar, shallow singleton, middle overload, and product-SCD
   tail term.

3. A natural promotion macro is already an exact local instance of this
   theorem.  Put \(s=m-H\), so \(M=s+2H\).  The natural \(2s\)-ring
   scaffold has exactly one distinguished bad phase in every ring.
   Deleting these \(2s\) phases makes every proper signed trace
   collision-free.  At lower depth \(q\), every deleted trace has a
   unique retained copy, so the deletion loses no raw lower image at any
   \(0\le q\le H\).  With arbitrary stopping tags and at most one
   depth-\(H\) tag per ring, the cemetery-valued paired maps form an
   exact quotient chain.  Thus the local integrality problem is solved.

4. Under uniform individual-frame marginals, the block-factor hole
   theorem prevents these local solutions from being assembled by small
   independent components.  A natural macro meets the root star of any
   middle target in at most \(H+1\) roots.  Consequently an independent
   dependency block containing at most \(g\) natural macros has, when
   \(g(H+1)p<1\), expected middle holes at least

   \[
      W\exp\!\left(-{\theta\over1-g(H+1)p}\right),
      \qquad
      p={M\over\binom MH},\quad
      \theta=\binom mH p={MN_H\over W}=1+o(1).
      \tag{0.5}
   \]

   A good symmetrized product law therefore needs

   \[
      g\ge {1-o(1)\over p(H+1)}.
      \tag{0.6}
   \]

   In any hierarchy with branching at most \(2m\), this forces depth

   \[
      d\ge
      {\log(1/p)-\log(H+1)\over\log(2m)}
      =\left({1\over2}-o(1)\right)H.
      \tag{0.7}
   \]

   A naive endpoint-capped realization paying a fresh uncancelled
   promotion-ring cut at every such level has collar at least
   \((\tfrac12-o(1))W\log m\), and is impossible for coefficient one.
   Any positive recursion must be globally correlated and must
   cross-splice or recycle its cuts so that its final number of physical
   components is still \(O(N_H)\).

5. There is a literal lower-trace determinant-two triangle repeated
   through all depths \(q_0,\ldots,H\), in three owner-disjoint
   promotion rings.  It excludes a universal total-unimodularity or
   lower-quotient-core theorem.
   It does **not** by itself amplify to a global obstruction.  After one
   of its three histories is retained, all missing displayed lower cells
   have inclusion-poset width exactly two.  In the unrestricted
   nested-history cover
   projection, two outside physical **lower** erosion histories cover
   them all and the exact fractional cover/dual value is two.  The
   apparent \(\Theta(H)\) lower-incidence obstruction therefore has only
   a two-history restricted cover before upper traces, rooted frame
   grouping, owner collisions, and collar costs are imposed.

The rigorous boundary is consequently sharp.  Local morphology and
local history integrality are available, and independent or shallow
composition is ruled out.  The standard amplified triangle is
repairable only in its unrestricted lower-history projection; its paired
upper collateral and rooted packing remain open.  The remaining theorem
is a globally correlated one-frame-per-root selection whose paired trace
fibres are suffix-closed and whose physical cuts are recycled.  No such
global selection, and no global integer-hull obstruction to it, is
proved here.

## 1. Covering-side calibration

The exact product formula is

\[
 \lambda_q=\prod_{j=1}^q{m+j\over m-j+1}.
 \tag{1.1}
\]

Writing each factor as
\[
 {m+j\over m-j+1}
 =1+{2j-1\over m-j+1}
\]
and using
\[
 {x\over1+x}\le\log(1+x)\le x
\]
gives the nonasymptotic bounds
\[
 \boxed{
 {q^2\over m+q}\le\log\lambda_q
 \le {q^2\over m-q+1}}\qquad(0\le q<m).
 \tag{1.2}
\]

Since \(\lambda_H\le m+H\le2m\), the lower bound in (1.2) first gives
\[
 H^2\le(m+H)\log(2m),
\]
and hence \(H=O(\sqrt{m\log m})=o(m)\).  In particular \(H\le m-2\)
for large \(m\), so \(\lambda_{H+1}\) is defined and maximality in
(0.2) implies \(\lambda_{H+1}>m+H+1\).

Uniformly for \(q=O(\sqrt{m\log m})\), Taylor expansion term by term
gives

\[
 \log\lambda_q={q^2\over m}+O(q^3/m^2+q/m^2).
 \tag{1.3}
\]

The error is \(o(1)\) at the relevant scale.  Apply (1.3) at \(H\) and
\(H+1\).  The inequalities
\(\lambda_H\le m+H<\lambda_{H+1}\), together with
\(\log(m+H)=\log m+o(1)\), therefore give

\[
                         H^2/m=\log m+o(\log m),
 \tag{1.4}
\]

which proves the first assertion of (0.3).

Since \(\lambda_H\le M\), one has \(MN_H\ge W\).  On the other hand,
maximality gives

\[
 \lambda_{H+1}>M+1,\qquad
 {\lambda_{H+1}\over\lambda_H}={m+H+1\over m-H}={M+1\over m-H},
\]

and hence

\[
                         m-H<\lambda_H\le m+H.
 \tag{1.5}
\]

It follows that

\[
 1\le {MN_H\over W}={M\over\lambda_H}
 <{m+H\over m-H}=1+O(H/m).
 \tag{1.6}
\]

This proves (0.3), and (1.5) also proves (0.4).

At the inner cutoff, the sharper small-\(q\) expansion gives

\[
 W-N_{q_0}=Wm^{-1/2}+O(Wm^{-3/4}).
 \tag{1.7}
\]

Moreover, uniformly for \(q<q_0\),

\[
 {N_q\over W}=1-{q^2\over m}+O(m^{-1}),
\]

with a summable error at this range.  Therefore

\[
 2\sum_{q=1}^{q_0-1}(N_q-N_{q_0})
 =\left({4\over3}+o(1)\right){Wq_0^3\over m}
 =O(Wm^{-1/4})=o(W).
 \tag{1.8}
\]

This is the exact two-sign shallow baseline used below.

## 2. Physical promotion-ring morphology

Let \(U\) be an \(M\)-set with cyclic order

\[
                         \pi=(u_0,\ldots,u_{M-1}).
\]

All subscripts in this section are modulo \(M\).  Put

\[
 X_j=I_\pi(j,m)=\{u_j,u_{j+1},\ldots,u_{j+m-1}\}.
 \tag{2.1}
\]

Then

\[
 X_{j+1}=X_j-u_j+u_{j+m}.
 \tag{2.2}
\]

Every coordinate of \(U\) has one positive run of exactly \(m\)
consecutive phases and one zero run of exactly \(H\) consecutive phases.
Coordinates outside \(U\) are constantly zero.  Thus no coordinate can
leave and return in any protected window of at most \(H+1\) consecutive
states.

For \(0\le q\le H\), define the physical lower and upper traces

\[
 \Phi_q^-(j)=\bigcap_{t=0}^qX_{j+t},
 \qquad
 \Phi_q^+(j)=\bigcup_{t=0}^qX_{j+t}.
 \tag{2.3}
\]

Directly from (2.1),

\[
 \boxed{
 \Phi_q^-(j)=I_\pi(j+q,m-q),\qquad
 \Phi_q^+(j)=I_\pi(j,m+q).}
 \tag{2.4}
\]

These are literal Boolean masks of ranks \(m-q\) and \(m+q\).  Notice
the endpoint phenomenon

\[
                         \Phi_H^+(j)=U
 \tag{2.5}
\]

for every phase in the ring.  Thus a two-sided depth-\(H\) selection may
use at most one phase from one ring.

For completeness, the standard delay-factor identity is also literal
here.  On a linearized ring path put

\[
 B_j=\bigcap_{t=0}^{H}X_{j-t}.
\]

The no-return property gives, throughout the protected interior,

\[
 X_i=\bigcup_{j=i}^{i+H}B_j,
 \tag{2.6}
\]

\[
 \bigcap_{t=0}^qX_{i+t}=\bigcup_{j=i+q}^{i+H}B_j,
 \qquad
 \bigcup_{t=0}^qX_{i+t}=\bigcup_{j=i}^{i+q+H}B_j.
 \tag{2.7}
\]

Write the resulting \(B\)-letters in cyclic order, cut once, and append
the first \(2H\) \(B\)-letters.  Equations (2.6)--(2.7) then turn all
the masks in (2.3) into literal contiguous OR blocks.  The block has
exact length \(M+2H\), so its seam cost is \(2H\) letters per ring.
Repetition of a coordinate after the protected window is irrelevant.

## 3. The paired quotient-chain theorem

Let \(E\) be any finite set of physical phase occurrences.  At every
depth \(q\) in an interval \([a,b]\), suppose there are maps

\[
 \Phi_q^-:E\to\mathcal L_q^-,\qquad
 \Phi_q^+:E\to\mathcal L_q^+,
\]

where in the Boolean application

\[
 |\mathcal L_q^-|=|\mathcal L_q^+|=N_q.
\]

Put

\[
 \Theta_q(e)=(\Phi_q^-(e),\Phi_q^+(e)),\qquad
 I_q=\Theta_q(E).
 \tag{3.1}
\]

### Theorem 3.1 (paired quotient-chain integrality)

Assume:

1. for every \(a\le q<b\), there is a map

   \[
       F_q:I_q\longrightarrow I_{q+1}
       \quad\hbox{such that}\quad
       \Theta_{q+1}=F_q\circ\Theta_q;
       \tag{3.2}
   \]

2. for every \(q\), both coordinate projections

   \[
       I_q\to\mathcal L_q^-,\qquad I_q\to\mathcal L_q^+
       \tag{3.3}
   \]

   are injective.

Then there are nested sets

\[
                         A_b\subseteq A_{b-1}\subseteq\cdots\subseteq A_a\subseteq E
 \tag{3.4}
\]

such that \(\Theta_q|_{A_q}\) is a bijection from \(A_q\) to \(I_q\)
for every \(q\).  Consequently each of
\(\Phi_q^-|_{A_q}\) and \(\Phi_q^+|_{A_q}\) is a bijection onto its
image, and the total signed target deficiency is exactly

\[
                         2\sum_{q=a}^b(N_q-|I_q|).
 \tag{3.5}
\]

#### Proof

Choose one representative in \(E\) of every fibre of \(\Theta_b\), and
call the resulting set \(A_b\).  Suppose \(A_{q+1}\) has been chosen.
Two distinct members of \(A_{q+1}\) cannot have the same \(\Theta_q\)
value: by (3.2) they would then have the same \(\Theta_{q+1}\) value,
contrary to the representative property.  Thus \(A_{q+1}\) is already
a partial system of distinct representatives for the \(\Theta_q\)
fibres.  Add one arbitrary representative from every as-yet unrepresented
\(\Theta_q\) fibre.  This gives \(A_q\), and downward induction proves
(3.4).

Condition (3.3) turns the paired-image bijection into simultaneous
bijections in both coordinates.  Each signed layer has \(N_q\) targets,
so its two coordinate images omit exactly \(2(N_q-|I_q|)\) targets.
Summing proves (3.5). \(\square\)

This is a common-history theorem, not a separate matching theorem at
each depth.  The complete prefix state \(\Theta_q(e)\), and not merely
its current lower or upper target, controls whether an already chosen
deep representative is extendible.

### Lemma 3.2 (cemetery quotient)

Suppose every occurrence \(e\in E\) is given a stopping depth
\(d(e)\in\{0,\ldots,H\}\).  Define

\[
 \widehat\Theta_q(e)=
 \begin{cases}
   (\Phi_q^-(e),\Phi_q^+(e)),&q\le d(e),\\
   \bot,&q>d(e).
 \end{cases}
 \tag{3.6}
\]

If, at every \(q\), the two signed trace maps are injective on the active
set \(\{e:d(e)\ge q\}\), then the maps \(\widehat\Theta_q\) form a
quotient chain.

#### Proof

At depth \(q\), every active fibre is a singleton, while all inactive
occurrences form the single fibre \(\widehat\Theta_q^{-1}(\bot)\).
An active singleton either remains a singleton at depth \(q+1\) or joins
the cemetery fibre.  An inactive occurrence stays inactive.  Thus every
depth-\(q\) fibre lies in one depth-\((q+1)\) fibre, which is exactly
(3.2). \(\square\)

The cemetery lemma is the precise reason that a collision-free tagged
promotion packet is an integral common-history block.

## 4. Exact factor-blind plug-in theorem

For every root

\[
                         A\in\binom{[2m]}{m-H},
\]

let \(U_A=[2m]\setminus A\), choose one cyclic frame on \(U_A\), and
take all \(M\) physical phases of that frame.  Let \(\mathcal E\) be the
resulting occurrence set.  Thus

\[
                         |\mathcal E|=MN_H=W+E.
 \tag{4.1}
\]

For a middle mask \(D\), let \(L_D\) be its occurrence load, and put

\[
 C_0=\sum_{D\in\binom{[2m]}m}(L_D-1)_+.
 \tag{4.2}
\]

Assume that a subset \(E'\subseteq\mathcal E\) satisfies Theorem 3.1
through depths \(q_0,\ldots,H\).  Let \(A_q\) be the resulting nested
sets and put

\[
 \delta_0=N_{q_0}-|I_{q_0}|,
 \qquad
 D_{\ge q_0}=2\sum_{q=q_0}^{H}(N_q-|I_q|).
 \tag{4.3}
\]

Give an occurrence in \(A_{q_0}\) the largest tag \(q\) for which it
lies in \(A_q\), and give every other occurrence tag zero.  For
\(1\le q<q_0\), let \(\mu_{q,T}^{\pm}\) be the multiplicity with which
the traces of \(A_{q_0}\) hit the signed target \(T\), and put

\[
 C_{<q_0}=
 \sum_{q=1}^{q_0-1}\left[
  \sum_{|T|=m-q}(\mu_{q,T}^--1)_+
 +\sum_{|T|=m+q}(\mu_{q,T}^+-1)_+
 \right].
 \tag{4.4}
\]

### Theorem 4.1 (literal paired-quotient compiler)

With the notation above,

\[
\boxed{
\begin{aligned}
 \nu(2m)\le{}&W+C_0+2HN_H+D_{\ge q_0}\\
 &+2\sum_{q=1}^{q_0-1}(N_q-N_{q_0})
 +2(q_0-1)\delta_0+C_{<q_0}\\
 &+L_m(m-H-1),
\end{aligned}}
 \tag{4.5}
\]

where \(L_m(m-H-1)\) is the established product-SCD exterior word and

\[
                         L_m(m-H-1)
 \le C_{\rm tail}e^{-H^2/(8m)}W=o(W)
 \tag{4.6}
\]

for an absolute constant \(C_{\rm tail}\).

In particular, the following conditions imply
\(\nu(2m)\le(1+o(1))W\):

\[
 C_0=o(W),\qquad D_{\ge q_0}=o(W),
 \qquad q_0\delta_0=o(W),\qquad C_{<q_0}=o(W).
 \tag{4.7}
\]

#### Proof

Keep every middle occurrence.  If \(Z_0\) middle targets are absent,
then mass conservation gives

\[
                         C_0-Z_0=|\mathcal E|-W=E.
\]

Cut each of the \(N_H\) physical rings once.  Equations (2.6)--(2.7)
compile its tagged traces into a literal contiguous-OR block with seam
cost exactly \(2H\).  Appending the \(Z_0\) missing middle targets as
singletons changes the middle-plus-owner contribution from

\[
 |\mathcal E|+Z_0=W+E+Z_0
\]

to \(W+C_0\).

At depth \(q\ge q_0\), Theorem 3.1 makes the two selected trace lists
injective, so the exact number of holes relative to this selected
subfamily is \(2(N_q-|I_q|)\).  Unselected raw ring traces can only
reduce the actual hole count.  The selected-subfamily bounds sum to
\(D_{\ge q_0}\).

At a shallower depth, every member of \(A_{q_0}\) is active.  Its
cardinality is

\[
                         |A_{q_0}|=N_{q_0}-\delta_0.
\]

For either sign, the elementary identity

\[
 \#\text{holes}=N_q-|A_{q_0}|+
                 \sum_T(\mu_{q,T}^{\pm}-1)_+
 \tag{4.8}
\]

gives the second line of (4.5) after summing the two signs.  Append one
singleton for every such missing target, and finally append the one
product-SCD exterior word.  Concatenation creates no extra seam.  This
proves (4.5).

Now use (0.4), (1.8), (4.6), and (4.7). \(\square\)

The exact statement exposes an often hidden loss.  Merely knowing
\(\delta_0=o(W)\) is insufficient if the same entrance deficit is paid
at all \(q_0\) shallow depths; the required condition is
\(q_0\delta_0=o(W)\), unless the shallow traces are repaired by another
mechanism.  In the exact entrance case \(\delta_0=0\), this issue
disappears.

## 5. The natural one-hole macro is an exact local quotient block

Put

\[
                         s=m-H,\qquad M=s+2H,
 \tag{5.1}
\]

and assume \(s>2H\).  Partition the ground set as

\[
 [2m]=Q\mathbin{\dot\cup}V,\qquad |Q|=2H,\quad |V|=2s.
 \tag{5.2}
\]

Fix an order on \(Q\), cyclically write

\[
                         V=(v_0,\ldots,v_{2s-1}),
\]

and put

\[
 T_i=\{v_i,v_{i+1},\ldots,v_{i+s-1}\},\qquad
 U_i=Q\cup T_i
 \tag{5.3}
\]

for \(i\in\mathbb Z/(2s)\).  Give \(U_i\) the natural cyclic frame
\((Q,T_i)\).  Let \(D_i\) be the phase whose omitted intervals end at
\(v_{i+s-1}\); equivalently, at every proper rank its omitted interval
is a suffix of \(T_i\).

### Theorem 5.1 (exact collision classification and one-hole repair)

At a signed rank \(m+r\), put

\[
                         \ell=H-r\in\{0,\ldots,2H\}.
 \tag{5.4}
\]

For \(\ell>0\), every cross-ring collision is uniquely of the form

\[
 U_i\setminus\operatorname{prefix}_{\ell}(T_i)
 =U_{i+\ell}\setminus
   \operatorname{suffix}_{\ell}(T_{i+\ell}).
 \tag{5.5}
\]

The second occurrence in (5.5) lies on \(D_{i+\ell}\).  There are no
other cross-ring collisions.  At \(\ell=0\), the masks are the distinct
tops \(U_i\).

Consequently, after deleting \(D_i\) from every ring:

1. all retained masks are pairwise distinct at every proper signed rank;
2. at depth \(H\), the upper masks are distinct provided at most one
   phase per ring is active;
3. for every lower depth \(0\le q\le H\), the retained lower map is
   injective and has exactly the same image as the full raw lower map.

More explicitly, with \(\ell=H+q\),

\[
 \Phi_q^-(D_j)=
 \Phi_q^-(P_{j-\ell,q}),
 \tag{5.6}
\]

where \(P_{j-\ell,q}\) is the retained phase of ring \(j-\ell\) whose
omitted interval is \(\operatorname{prefix}_{\ell}(T_{j-\ell})\).

#### Proof

Suppose two masks in rings \(i\) and \(i+t\), with
\(1\le t\le s\), are equal after omitting cyclic intervals \(I,J\) of
the common length \(\ell\le2H<s\).  The two tops differ on the two
\(t\)-blocks

\[
 \{v_i,\ldots,v_{i+t-1}\},\qquad
 \{v_{i+s},\ldots,v_{i+s+t-1}\}.
\]

Equality forces the first block into \(I\), the second into \(J\), and
therefore \(t\le\ell\).  Since an omitted interval has length less than
\(s\), the only possible forms are

\[
 I=\operatorname{suffix}_a(Q)\cup
   \operatorname{prefix}_b(T_i),\qquad
 J=\operatorname{suffix}_c(T_{i+t})\cup
   \operatorname{prefix}_d(Q),
\]

where \(a+b=c+d=\ell\), \(b,c\ge t\).  Equality on the common
\(Q\)-coordinates says that a suffix of the ordered set \(Q\) equals a
prefix.  If these are proper, distinctness of the coordinates forces
both to be empty.  At the endpoint \(\ell=2H=|Q|\), the only additional
formal possibility is that both equal all of \(Q\); then the remaining
masks are \(T_i\) and \(T_{i+t}\), which are distinct for \(t\ne0\), so
this is not a collision.  Hence every collision has \(a=d=0\), and
\(I\) is a prefix of \(T_i\) while \(J\) is a suffix of \(T_{i+t}\).

After the forced \(t\)-blocks are removed, equality of the remaining
proper cyclic intervals would, if \(\ell>t\), force \(\ell=s\).  This
is impossible because \(\ell\le2H<s\).  Thus \(\ell=t\), proving
(5.5).  The converse equality is immediate by displaying the common
remaining \(v\)-interval.

For fixed second ring \(j=i+\ell\), all the suffixes in (5.5) belong to
the single phase \(D_j\).  Deleting every \(D_j\) therefore removes one
member of every collision and no collision-free retained member.
Within one ring, distinct proper cyclic intervals give distinct masks.
At upper depth \(H\), (2.5) explains the one-active-phase condition.

At lower depth \(q\), \(\ell=H+q\).  The deleted suffix occurrence has
the retained prefix partner in (5.5), which is not a \(D\)-phase because
\(\ell<s\).  This proves (5.6), injectivity, and equality of the full
and retained lower images. \(\square\)

### Corollary 5.2 (local paired common-history integrality)

Give arbitrary stopping depths \(d(e)\in\{0,\ldots,H\}\) to the
retained phases, with at most one depth-\(H\) phase in every ring.  Then
the active lower and upper masks are pairwise distinct at every depth,
and the cemetery-valued paired maps (3.6) form a quotient chain.

The macro contains exactly

\[
                         2s(M-1)
 \tag{5.7}
\]

retained middle occurrences and is covered by exactly \(2s\) physical
promotion paths.

#### Proof

Theorem 5.1 gives injectivity at every proper signed rank and the stated
condition handles the upper endpoint.  Lemma 3.2 gives the quotient
chain.  Deleting one vertex from each promotion cycle leaves one path,
proving the count. \(\square\)

There is also no local tag-capacity loss.  Across all \(N_H\) roots,
reserve one retained phase per root for tag \(H\).  The number of other
slots available through depth \(q_0\) is \((M-2)N_H\), while the demand
is \(N_{q_0}-N_H\).  From the covering-side calibration,

\[
 (M-1)N_H\ge W-N_H\ge N_{q_0}
 \tag{5.8}
\]

for large \(m\).  Hence the exact census

\[
 \#\{d=q\}=N_q-N_{q+1}\quad(q_0\le q<H),
 \qquad \#\{d=H\}=N_H
 \tag{5.9}
\]

fits in the repaired rings.  Tags may be assigned arbitrarily inside a
macro, so (5.9) is an arithmetic fact, not yet a global collision-free
selection.

If the complete root set could be partitioned into such macros, the
one-hole repair would delete exactly one phase per root, namely
\[
                         N_H=o(W/H)
\]
middle occurrences, while leaving exactly \(N_H\) promotion paths.
Thus its owner, image, and seam ledgers are all locally admissible.
The existence of that globally compatible macro partition and of the
required cross-macro frame selection is precisely what is not supplied
by the local theorem.

## 6. The exact one-frame-per-root entrance normal form

It is useful to take complements of the middle owners.  A root is

\[
                         A\in\binom{[2m]}{m-H},
\]

its top is \(U_A=A^c\), and a cyclic frame on \(U_A\) supplies the
middle deck

\[
 \mathscr D(A,\pi)=
 \{A\cup J:J\text{ is a cyclic }H\text{-window of }\pi\}.
 \tag{6.1}
\]

For a middle target \(D\), the possible roots are exactly

\[
 \mathcal R(D)=\{A\subset D:|A|=m-H\},\qquad
 |\mathcal R(D)|=R:=\binom mH.
 \tag{6.2}
\]

Choose one frame at every root and let \(L_D\) be the resulting deck
load.  Put

\[
 Z=|\{D:L_D=0\}|,\qquad
 C=\sum_D(L_D-1)_+.
 \tag{6.3}
\]

### Proposition 6.1 (exact load conservation)

One has

\[
 \boxed{C-Z=MN_H-W=E.}
 \tag{6.4}
\]

Thus, at the covering-side calibration,

\[
                         Z=o(W)\quad\Longleftrightarrow\quad C=o(W).
 \tag{6.5}
\]

Removing all but one occurrence of every covered target produces a
partial selector

\[
                         \sigma(D)\in\mathcal R(D)
 \tag{6.6}
\]

on \(W-Z\) targets, and every fibre \(\sigma^{-1}(A)\) is contained in
the single cyclic deck \(\mathscr D(A,\pi_A)\).  Conversely any such
selector leaves exactly \(E+Z\) unused deck occurrences.

#### Proof

Since every root deck has \(M\) members,

\[
 \sum_D(L_D-1)=MN_H-W.
\]

The positive terms on the left sum to \(C\), while every zero load
contributes \(-1\).  This proves (6.4).  The remaining statements are
immediate. \(\square\)

The all-depth problem is strictly stronger than (6.6).  Every selected
occurrence comes with the entire physical trace history (2.4), the sets
active at successive depths must be nested, both signs must be balanced,
and all occurrences assigned to one root must use its one common cyclic
frame.  Proposition 6.1 is only the entrance normal form.  Theorem 3.1
identifies one sufficient global structure: the paired trace fibres must
coarsen through depth.

Arbitrarily deleting duplicate phases from (6.1) can create \(C\)
additional path fragments.  A fully wrapped cyclic fragment has the
conservative \(2H\) collar used in Theorem 4.1.  A standard open
delay-\(H\) path has initialization toll \(H\) and total endpoint toll
\(H+\sigma\), \(0\le\sigma\le H\), with omitted crossing windows charged
separately.  Thus \(C=o(W)\) alone does not justify arbitrary deletion,
while \(C=o(W/H)\) is a support-blind sufficient fragmentation bound.
The safe compiler instead keeps the overloaded cycles and pays the exact
middle excess \(C\).

## 7. The block-factor barrier for natural macros

Define

\[
 L=\binom MH,\qquad p={M\over L},\qquad
 \theta=Rp={MN_H\over W}=1+O(H/m).
 \tag{7.1}
\]

A uniform random cyclic frame at one root selects a fixed compatible
middle target with probability \(p\).

### Theorem 7.1 (block-factor hole floor)

Partition the roots into blocks of size at most \(b\).  Allow arbitrary
dependence of the frame choices inside a block, assume different blocks
are independent, and assume every individual root frame has the uniform
cyclic-frame marginal.  If \(bp\le\alpha<1\), then the expected number
of middle holes satisfies

\[
 \boxed{
                         \mathbb EZ\ge
 W\exp\!\left(-{\theta\over1-\alpha}\right).}
 \tag{7.2}
\]

More precisely, for a target \(D\), if

\[
 \alpha_D=p\max_j|\mathcal B_j\cap\mathcal R(D)|<1,
\]

then

\[
 \Pr(D\text{ is missed})
 \ge\exp\!\left(-{\theta\over1-\alpha_D}\right).
 \tag{7.3}
\]

#### Proof

For block \(j\), let \(Y_{j,D}\) be the number of its roots whose frame
selects \(D\), and write

\[
 \mu_{j,D}=\mathbb EY_{j,D}
 =p|\mathcal B_j\cap\mathcal R(D)|.
\]

Markov's inequality gives

\[
 \Pr(Y_{j,D}=0)\ge1-\mu_{j,D}.
\]

Block independence and
\(\log(1-x)\ge-x/(1-x)\) give

\[
 \Pr(D\text{ is missed})
 \ge\prod_j(1-\mu_{j,D})
 \ge\exp\!\left(-{\sum_j\mu_{j,D}\over1-\alpha_D}\right).
\]

Finally \(\sum_j\mu_{j,D}=Rp=\theta\).  This proves (7.3), and summing
over \(D\) proves (7.2). \(\square\)

The following geometric observation makes this sharper for the exact
macro of Section 5.

### Lemma 7.2 (a macro sees at most \(H+1\) roots of one star)

Let \(\mathcal B\) be the \(2s\)-root family underlying one natural
macro.  Then for every middle target \(D\),

\[
 \boxed{|\mathcal B\cap\mathcal R(D)|\le H+1.}
 \tag{7.4}
\]

#### Proof

The complements of the tops (5.3) are the cyclic \(s\)-windows of
\(V\).  Such a root belongs to \(\mathcal R(D)\) precisely when that
\(s\)-window is contained in \(D\cap V\).  But

\[
 |D\cap V|\le |D|=m=s+H<2s.
\]

If a cyclic binary set of length \(2s\) contains an all-one
\(s\)-window, all its all-one \(s\)-windows lie in one cyclic run: two
distinct runs of length at least \(s\) would contain at least \(2s\)
ones.  A run of length at most \(s+H\) contains at most
\((s+H)-s+1=H+1\) different \(s\)-windows. \(\square\)

### Corollary 7.3 (independent macro hierarchy no-go)

Under the independence and uniform individual-frame marginal hypotheses
of Theorem 7.1, suppose every dependency block is a union of at most
\(g\) natural macros.  If \(g(H+1)p<1\), then

\[
 \boxed{
 \mathbb EZ\ge
 W\exp\!\left(-{\theta\over1-g(H+1)p}\right).}
 \tag{7.5}
\]

In particular, \(g(H+1)p=o(1)\) gives

\[
                         \mathbb EZ\ge(e^{-1}-o(1))W.
 \tag{7.6}
\]

Any sequence of such symmetrized product laws satisfying
\(\mathbb EZ=o(W)\) must satisfy

\[
                         g\ge{1-o(1)\over p(H+1)}.
 \tag{7.7}
\]

#### Proof

Lemma 7.2 gives
\(\alpha_D\le g(H+1)p\) for every target.  Apply (7.3).  If (7.7)
failed by a fixed factor along a subsequence, (7.5) would give a fixed
positive expected hole density, a contradiction. \(\square\)

Stirling's formula gives

\[
 \log{1\over p}
 =H\log{m\over H}+H-\log M
  +O(H^2/m+\log H).
 \tag{7.8}
\]

At the already calibrated critical scale,
\(\log M=O(\log H)\), so the term \(-\log M\) may be absorbed in the
displayed error.  Therefore

\[
 \log{1\over p}
 =\left({1\over2}+o(1)\right)H\log m
 =\left({1\over2}+o(1)\right)
   \sqrt m(\log m)^{3/2}.
 \tag{7.9}
\]

If a product hierarchy has branching at most \(2m\), a depth-\(d\)
block contains at most \((2m)^d\) leaf macros.  Equations (7.7)--(7.9)
give

\[
 d\ge{\log(1/p)-\log(H+1)+o(1)\over\log(2m)}
 =\left({1\over2}-o(1)\right)H,
 \tag{7.10}
\]

which is (0.7).

This is not only a probabilistic depth warning.  If a literal recursive
implementation pays one new uncancelled open-path initialization for
each root at each level, then its number of final paths is at least
\(dN_H\), and the standard endpoint-capped charge is at least

\[
 HdN_H
 \ge\left({1\over2}-o(1)\right)H^2N_H
 =\left({1\over2}-o(1)\right)W\log m.
 \tag{7.11}
\]

If every component is instead fully cyclically wrapped, its charge is
\(2H\) and the constant in (7.11) doubles.  The displayed lower bound is
conditional on the stated standard endpoint-capped implementation; no
architecture-independent seam lower bound is asserted.  It identifies
exactly what a positive \(\Theta(H)\)-depth construction must do:
correlate across nearly whole root stars while cross-splicing all
intermediate cuts into only \(O(N_H)\) final components.

The uniform-marginal and block-independence hypotheses in Theorem 7.1
must be retained.  A single deterministic good selection, averaged under
one global coordinate permutation, has uniform marginals but global
dependence and is not excluded.  Thus (7.10) closes small independent
component schemes, not globally correlated design.

## 8. A signed-marginal full-configuration packet dual

Scalar entrance Hall cuts and the ordinary frame LP are already exact at
their fractional floor.  The correct nonlocal columns are whole rooted
frame-and-tag configurations.

Let \(\mathscr P_A\) be the finite set of all allowed configurations at
root \(A\): one cyclic frame, a stopping tag in
\(\{0,\ldots,H\}\) or a blank on every phase, and at most one nonblank
tag \(H\).  Let \(\mathcal T\) be any chosen collection of signed
target-depth cells, and let

\[
                         \Gamma(P)\subseteq\mathcal T
 \tag{8.1}
\]

be the cells supplied by configuration \(P\).  Write \(n_d(P)\) for its
number of tags \(d\), and prescribe a global tag census \(\gamma_d\).
A blank contributes no \(n_d\) and no positive-depth cell.  It is
different from tag zero, which is a retained middle phase but has no
positive-depth trace.  The program below models signed marginal
coverage and the tag census only; it has no middle-owner, paired-fibre,
injectivity, or component constraint.

For nonnegative cell weights \(w_c\), the exact fractional
maximum-coverage program is

\[
\begin{array}{ll}
\text{maximize}&\displaystyle\sum_{c\in\mathcal T}w_cy_c\\
\text{subject to}
 &0\le y_c\le1,\\
 &\displaystyle y_c\le
   \sum_A\sum_{P\in\mathscr P_A:c\in\Gamma(P)}x_{A,P},\\
 &\displaystyle\sum_{P\in\mathscr P_A}x_{A,P}=1\quad(A),\\
 &\displaystyle\sum_A\sum_Pn_d(P)x_{A,P}=\gamma_d\quad(d),\\
 &x_{A,P}\ge0.
\end{array}
 \tag{8.2}
\]

### Proposition 8.1 (exact rooted-configuration LP dual)

Assume the census equations in (8.2) are feasible.  Then the value of
(8.2) equals

\[
\boxed{
\min_{\substack{a_c\ge0\\ \eta_d\in\mathbb R}}
\left\{
 \sum_c(w_c-a_c)_+
 +\sum_A\max_{P\in\mathscr P_A}
       \left(\sum_{c\in\Gamma(P)}a_c-\sum_d\eta_dn_d(P)\right)
 +\sum_d\eta_d\gamma_d
\right\}.}
 \tag{8.3}
\]

#### Proof

Give the coverage inequality for cell \(c\) a multiplier \(a_c\ge0\),
the cap \(y_c\le1\) a multiplier \(b_c\ge0\), the root equality a free
multiplier \(z_A\), and the census equality a free multiplier \(\eta_d\).
The coefficient of \(y_c\) is bounded above exactly when
\(a_c+b_c\ge w_c\), and the coefficient of every \(x_{A,P}\) is bounded
above exactly when

\[
 z_A+\sum_d\eta_dn_d(P)
 \ge\sum_{c\in\Gamma(P)}a_c.
\]

Minimizing first in \(b_c\) and then in \(z_A\) gives
\(b_c=(w_c-a_c)_+\) and the maximum in (8.3).  Finite-dimensional LP
duality proves equality. \(\square\)

The maximum in (8.3) ranges over a complete cyclic frame and its complete
history profile.  Thus (8.3) is a higher-order packet dual, not a scalar
Hall cut on one target layer.

It does not by itself produce a negative theorem.  For the exact SCD
census, averaging all rooted frames and the exact fractional tag
configurations gives unit load at every signed target in the census
range.  For the truncated \(q_0\)-census it gives unit load at every
depth \(q_0\le q\le H\), with the already quantified one-baseline load
at shallower depths.  Hence the corresponding census-range version of
(8.2) has full fractional coverage.  Within this signed-target/tag-census
relaxation, no linear dual separates the symmetric point.  A linear
obstruction may still arise after adding middle-owner, paired-quotient,
projection-injectivity, or physical-component constraints.  The next
section computes one natural one-sign history residual dual and shows
that it is too small.

## 9. A physical depth-\(H\) lower triangle and its restricted two-chain cover

Put

\[
                         L=H-q_0,
 \tag{9.1}
\]

and assume \(L\ge3\).  Choose pairwise disjoint sets and coordinates

\[
 |C|=m-H-1,\qquad
 D=\{d_0,d_1,\ldots,d_L\},\qquad e\notin C\cup D.
 \tag{9.2}
\]

For \(0\le j\le L\), define rank-\((m-q_0-j)\) targets

\[
 T_j=C\cup\{d_j,d_{j+1},\ldots,d_L\},
 \tag{9.3}
\]

\[
 O_0=C\cup\{e,d_1,\ldots,d_L\},
 \tag{9.4}
\]

and, for \(j\ge1\),

\[
 O_j=C\cup\{d_{j-1},d_{j+1},\ldots,d_L\}.
 \tag{9.5}
\]

Define three histories \(A,B,C'\) by the table

\[
\begin{array}{c|c|c}
 j\pmod3&\text{two histories attaining }T_j&
          \text{history attaining }O_j\\ \hline
 0&A,B&C'\\
 1&A,C'&B\\
 2&B,C'&A.
\end{array}
 \tag{9.6}
\]

### Lemma 9.1 (the three columns are physical nested histories)

Every column in (9.6) is a one-deletion history.  Moreover, when

\[
                         m\ge3H+2q_0+1,
 \tag{9.7}
\]

the three histories occur at one designated phase in three
owner-disjoint ordinary promotion rings, with no unintended occurrence
of any displayed \(T_j\) or \(O_j\) inside those three rings.

#### Proof

The transition identities are

\[
 T_j\setminus T_{j+1}=\{d_j\},
 \tag{9.8}
\]

\[
 T_j\setminus O_{j+1}=\{d_{j+1}\},
 \tag{9.8a}
\]

\[
 O_0\setminus T_1=\{e\},\qquad
 O_j\setminus T_{j+1}=\{d_{j-1}\}\quad(j\ge1).
 \tag{9.9}
\]

At a row where a history remains in the equal pair it uses (9.8); when
it leaves the pair it uses (9.8a); and when it enters the pair it uses
(9.9).  Thus each column deletes exactly one coordinate per step.

For history \(i\), choose a private \(q_0\)-set \(P_i\) and a private
\(H\)-set \(B_i\).  Order the first \(m\) entries of its frame as

\[
 P_i,\quad\text{the forced deletions in (9.6)},\quad
 \text{the final undeleted variable},\quad C,
 \tag{9.10}
\]

and follow them by \(B_i\).  The first \(m\) entries are the middle
owner, and (2.4) gives the prescribed history from depth \(q_0\) through
depth \(H\).  The total number of coordinates needed is

\[
 (m-q_0+1)+3q_0+3H=m+2q_0+3H+1,
\]

so (9.7) suffices.

Every owner in ring \(i\) contains a coordinate from the private set
\(P_i\cup B_i\), whose size \(q_0+H>H\); hence owners from different
rings cannot coincide.  A displayed lower target contains all of the
terminal block \(C\) and none of \(B_i\).  Any interval inside these
three rings realizing it must therefore end immediately before \(B_i\),
which forces the designated phase and proves the stated
no-unintended-occurrence assertion.  Occurrences in external rings are
not excluded. \(\square\)

The construction prescribes only the lower traces.  Its private insertion
blocks generally make the corresponding upper traces different, so no
paired merge/split or signed-ledger cancellation is asserted.

At every three consecutive rows, the incidence of the common target
\(T_j\) on the three histories is

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix},
 \qquad \det=-2.
 \tag{9.11}
\]

Thus residence safety and physical promotion chronology do not imply
total unimodularity.  Also, a lower-trace full-depth quotient core
containing two of the three special histories is impossible: every pair
agrees at one row and splits at the next.  Equivalently, a paired core
satisfying Theorem 3.1's lower-coordinate injectivity cannot contain
both members of any such equal pair.  A full-depth core of either kind
contains at most one special history and therefore loses at least one of
the two displayed lower images at each of the \(L+1\) rows.  This does
not exclude a cemetery-valued selection which stops a history before a
later split.

This apparent amplification is not global.

### Theorem 9.2 (exact restricted two-chain lower-history cover)

Retain any one of the histories in (9.6), and let \(\mathcal M\) be the
set of the other local target required at every row.  Then the inclusion
poset \(\mathcal M\) has width exactly two and can be covered by two
physical nested lower-erosion histories.  Consequently the set-cover
number and its fractional dual both equal two when admissible columns are
individual nested lower histories.  This statement does not impose the
packet constraint that several repair histories assigned to one root
must belong to the same selected cyclic frame, and it does not constrain
their upper traces, tags, middle-owner collisions, or component ledger.

#### Proof

By cyclic symmetry, retain \(A\).  The missing sequence is

\[
 M_j=
 \begin{cases}
  O_j,&j\equiv0,1\pmod3,\\
  T_j,&j\equiv2\pmod3.
 \end{cases}
 \tag{9.12}
\]

Directly from (9.3)--(9.5), for \(k>j\),

\[
 T_k\subset T_j,
 \tag{9.13}
\]

\[
 T_k\subset O_j\quad(k\ge j+1),\qquad
 O_k\subset T_j\quad(k\ge j+1),
 \tag{9.14}
\]

and

\[
 O_k\subset O_j\quad(k\ge j+2).
 \tag{9.15}
\]

The only incomparable chronological pairs are \(O_j,O_{j+1}\).
The missing cells split explicitly into the two chains

\[
 O_0,T_2,O_3,T_5,O_6,T_8,\ldots
 \tag{9.16}
\]

and

\[
 O_1,O_4,O_7,\ldots .
 \tag{9.17}
\]

Whenever two targets at depths \(j<k\) in one of these lists are nested,
their cardinalities differ by exactly \(k-j\).  Ordering the elements of
their set difference fills all omitted intermediate ranks.  Adding
\(q_0\) initial deletions and then \(H\) insertion coordinates embeds
each completed chain in an ordinary promotion ring, exactly as in
Lemma 9.1.  The second list begins at depth \(q_0+1\); before this
interpolation choose any rank-\((m-q_0)\) superset of \(O_1\), which is
possible because the ground set has unused coordinates.  Thus two
individually physical outside lower histories cover all missing lower
cells in this projected subsystem.  Their simultaneous installation in the
already chosen atlas is not asserted.

They are necessary because \(O_0\) and \(O_1\) are incomparable, and no
erosion history can contain both.  For the fractional dual, put weight
one on \(O_0\) and one on \(O_1\), and zero elsewhere.  Every admissible
nested history has weight at most one, so the dual value is at least two;
the two-chain cover makes it at most two. \(\square\)

The same conclusion holds after retaining \(B\) or \(C'\), by shifting
the residues.  Hence the exact unrestricted lower-history set-cover
value of the \(\Theta(H)\)-row ladder is \(2\), not \(\Theta(H)\).
This is not an equality of complete paired trace ledgers: the interpolated
lower rows and every upper row are collateral and have not been shown to
cancel.

For \(W/H\) owner-disjoint local copies, the projected repair demand has
cardinality only \(2W/H=o(W)\).  This is not yet an \(o(W)\)-cost physical
repair: installing one isolated history by choosing a fresh root frame
also brings \(M-1\) other phases, and treating every history as a separate
path pays a fatal collar.  The upper traces, tag census, middle-owner
loads, common-frame compatibility, and quotient collateral of these
repairs are all unchecked.  The triangle proves neither a bundled repair
nor an obstruction to one.  Therefore the lower incidence ladder alone
is not a coefficient-one obstruction.  A negative theorem would have to
prove a new grouped-frame packing deficiency which prevents the
two-chain repairs on \(\Omega(W/H)\) ladders; a positive theorem must
install them in already-paid frames with cut recycling.  No such grouped
theorem is proved.

## 10. BTK/SCD scope and the surviving global theorem

An abstract symmetric-chain decomposition already has perfect common
history.  If \(A_q\) is the set of chains of radius at least \(q\), then

\[
                         A_H\subseteq\cdots\subseteq A_0,
 \tag{10.1}
\]

and the lower and upper rank-\(q\) members of \(A_q\) are bijections onto
the two Boolean layers.  This is exact abstract integrality.

It is not a physical one-frame-per-root theorem.  To import BTK or a
promotion SCD, one must assign its middle chains to the phase occurrences
of one cyclic frame at each root so that **the same occurrence histories**
supply both signs through every depth.  Separate lower and upper
matchings, separate depth matchings, or a fixed BTK-chain count do not
establish that assignment.

The natural macro of Section 5 proves this compatibility locally.  The
block-factor theorem proves that independent local compatibility cannot
be globalized at subcritical correlation scale.  Theorem 9.2 shows only
that the displayed triangle supplies no growing one-sided nested-history
set-cover dual.  Any obstruction may still come from grouped-frame,
paired-sign, owner-load, tag-census, or component incompatibility.

Thus the exact surviving sufficient theorem is the following.

> **Global paired entrance target.**  Choose one cyclic frame at every
> root.  On its physical phase occurrences find a set \(E'\) such that:
>
> 1. the paired maps \(\Theta_{q_0},\ldots,\Theta_H\) form a quotient
>    chain;
> 2. both coordinate projections of every paired image are injective;
> 3. the middle collision excess, the aggregate paired deep deficit, the
>    weighted entrance deficit \(q_0\delta_0\), and the shallow collision
>    excess are all \(o(W)\); and
> 4. the physical ring cuts are cross-spliced so that the final number
>    of components is \(O(N_H)\), or more generally \(o(W/H)\).

Theorem 4.1 proves that this target implies the coefficient-one Boolean
OR bound, integrally and inside literal physical histories.

What is now rigorously excluded, under the stated hypotheses, is any
proof of this target by:

* independent root choices with uniform cyclic-frame marginals;
* uniform-marginal independent root blocks of size \(b=o(1/p)\);
* uniform-marginal independent natural-macro blocks with
  \(g<(1-o(1))/[p(H+1)]\), in particular a hierarchy of such macros of
  depth \(o(H)\); or
* such a forced-depth independent macro hierarchy when its literal
  implementation pays a fresh uncancelled cut at every root and level.

The existing scalar entrance cuts and signed-marginal LPs do not
obstruct the symmetric fractional point.  What remains open is a global
correlated construction, or a stronger integer-hull obstruction, for
one-frame-per-root paired histories with cut recycling.

## 11. Audited boundary

Proved in this report:

1. the covering-side constants and all asymptotic seam and shallow terms;
2. the paired quotient-chain theorem and its exact defective form;
3. the literal factor-blind implication (4.5);
4. the natural macro collision classification, lossless lower deletion,
   and tagged paired quotient property;
5. the exact one-frame load conservation law;
6. the block-factor macro intersection bound, depth lower bound, and the
   conditional \(W\log m\) fresh-cut obstruction;
7. the exact signed-marginal rooted-configuration fractional LP dual;
   and
8. the physical lower-trace depth-\(H\) triangle together with its exact
   unrestricted two-chain lower set-cover value.

Not proved:

1. a deterministic globally correlated one-frame-per-root atlas with
   \(o(W)\) middle and paired history defect;
2. a \(\Theta(H)\)-depth transverse macro recursion with exact cut
   recycling;
3. a grouped-frame integer-hull inequality forcing linear defect;
4. simultaneous packing of the two lower repair chains from Theorem 9.2
   into the chosen paired atlas with controlled middle load, tag census,
   upper traces, and components; or
5. a direct BTK-to-promotion-frame common-history matching.

The block-factor result is a theorem only under its stated independent
block and uniform-marginal hypotheses.  The \(W\log m\) collar lower
bound is a theorem only for implementations paying one new uncancelled
cut per root per level.  Neither statement is a universal nonexistence
theorem.  Conversely, the local macro and the abstract BTK flag do not
claim global one-frame compatibility.  These qualifications are the
precise proved/conditional boundary.
