# A squarefree three-top promotion conveyor (with a symmetric six-top realization): exact middle ownership and toll-free all-depth floor motion

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,
\]

and assume \(M\ge 8H\), \(H\ge2\). There is an explicit exchange of
six actual cyclic frames on six distinct rank-\(M\) tops with all of the
following properties.

1. Each shore contains one frame on each of the same six tops.
2. Each shore is squarefree at the middle row: its \(6M\) physical
   middle targets are all distinct.
3. The two middle supports are identical. Thus the exchange preserves
   literal exact middle ownership, not merely the middle load vector.
4. At every positive depth \(1\le q\le H\), its direct
   \((m-q)\)-derivative, and equivalently its root-form complement, has
   exactly \(8q\) coefficients \(+1\), \(8q\) coefficients \(-1\), and

   \[
                         \|\Delta_q\|_2^2=16q.       \tag{0.1}
   \]

   The complete support is given by the context formula (4.5).
5. The two six-frame shores are coordinate-conjugate. For the exact
   integer-floor energy at any controlled layer and every fixed external
   load \(R_q\),

   \[
    \boxed{
    \mathcal E_q(R_q+\Gamma_q^1)
       -\mathcal E_q(R_q+\Gamma_q^0)
       =\langle R_q,\Delta_q\rangle .}              \tag{0.2}
   \]

   Hence the move has no quadratic self-toll and no hidden floor-baseline
   term.

The construction uses two open three-edge placeholder conveyors. Their
cyclic bases interchange the two radius-\(H\) placeholder neighbourhoods,
so their middle derivatives cancel. The bases do not interchange the
next \(H\) collar coordinates. This makes the cancellation fail in a
controlled way at every larger complementary radius \(H+q\).

This is a genuine non-load-neutral all-depth exchange while retaining an
exact middle factor. It is a local primitive, not a packed contraction or
a proof of coefficient one.

Section 9 shows that the same derivative has a squarefree **three-top**
realization. The six-top form is retained because its two equal-length
paths make the geometry and conjugacy completely symmetric. Three tops
are minimal within the distinct-top two-path conveyor model; no absolute
two-top no-go is claimed.

## 1. Interval and context notation

Let \(C\) be a set of size \(M-2\), and let \(A,B\) be positional
placeholders. A cyclic positional word \(\theta\) on
\(C\cup\{A,B\}\), filled by distinct labels \(x,y\notin C\), gives

\[
 \theta^+(x,y): A\mapsto x,\ B\mapsto y,
 \qquad
 \theta^-(x,y): A\mapsto y,\ B\mapsto x.           \tag{1.1}
\]

For a cyclic order \(\pi\), let \(c_\pi^h\) be the incidence vector of
all cyclic length-\(h\) intervals. Put

\[
 d_h(\theta;x,y)
 :=c_{\theta^-(x,y)}^h-c_{\theta^+(x,y)}^h.         \tag{1.2}
\]

For a placeholder \(Z\in\{A,B\}\), let
\(\operatorname {Pred}_t^\theta(Z)\) and
\(\operatorname {Succ}_t^\theta(Z)\) denote the sets of the nearest
\(t\) positional labels immediately before and after \(Z\). Define the
context family

\[
 \mathcal F_Z^h(\theta)
 =\left\{
 K_{Z,t}^\theta(h):=
 \operatorname {Pred}_t^\theta(Z)
 \cup\operatorname {Succ}_{h-1-t}^\theta(Z):
 0\le t\le h-1
 \right\}.                                         \tag{1.3}
\]

### Lemma 1.1 (far-placeholder derivative)

Suppose both cyclic distances between \(A\) and \(B\) exceed \(h\).
Then

\[
\begin{aligned}
 d_h(\theta;x,y)
  ={}&\sum_{t=0}^{h-1}
       \left(e_{K_{A,t}^\theta(h)\cup\{y\}}
             -e_{K_{A,t}^\theta(h)\cup\{x\}}\right)\\
    &-\sum_{t=0}^{h-1}
       \left(e_{K_{B,t}^\theta(h)\cup\{y\}}
             -e_{K_{B,t}^\theta(h)\cup\{x\}}\right).
                                                               \tag{1.4}
\end{aligned}
\]

#### Proof

No length-\(h\) interval contains both placeholders. An interval
containing \(A\), with \(t\) predecessors and \(h-1-t\) successors,
changes from \(K_{A,t}\cup\{x\}\) to
\(K_{A,t}\cup\{y\}\). An interval containing \(B\) changes in the
opposite direction. Intervals containing neither placeholder are
unchanged. Summing proves (1.4). \(\square\)

## 2. Two bases with swapped inner neighbourhoods and unswapped collars

Choose eight pairwise disjoint ordered blocks in \(C\). Four inner arms
have length \(H-1\):

\[
 A^-,A^+,B^-,B^+,
\]

and four outer collar arms have length \(H\):

\[
 \widehat A^-,\widehat A^+,
 \widehat B^-,\widehat B^+.
\]

Every arm is written in nearest-to-farthest order relative to its named
placeholder. Let \(F_1,F_2\) be arbitrary ordered blocks partitioning
the remaining \(M-8H+2\) core labels. Write \(\overleftarrow Z\) for
the reversed order of a block \(Z\).

Define the two cyclic positional words

\[
\begin{aligned}
 \omega={}&(
 A, A^+,\widehat A^+,F_1,
 \overleftarrow{\widehat B^-},\overleftarrow{B^-},
 B, B^+,\widehat B^+,F_2,
 \overleftarrow{\widehat A^-},\overleftarrow{A^-}),\tag{2.1}\\
 \omega'={}&(
 A, B^+,\widehat A^+,F_1,
 \overleftarrow{\widehat B^-},\overleftarrow{A^-},
 B, A^+,\widehat B^+,F_2,
 \overleftarrow{\widehat A^-},\overleftarrow{B^-}).\tag{2.2}
\end{aligned}
\]

Both arcs between the placeholders have length at least \(4H-2\). Hence
no interval of length at most \(2H\) contains both placeholders.

At radius \(H\), only the inner arms enter (1.3). The inner
neighbourhood of \(A\) in \(\omega'\) is the inner neighbourhood of
\(B\) in \(\omega\), and conversely. Therefore, for every
\(0\le t\le H-1\),

\[
 K_{A,t}^{\omega'}(H)=K_{B,t}^{\omega}(H),
 \qquad
 K_{B,t}^{\omega'}(H)=K_{A,t}^{\omega}(H).          \tag{2.3}
\]

Lemma 1.1 gives the exact sign reversal

\[
                         d_H(\omega';x,y)
                          =-d_H(\omega;x,y).         \tag{2.4}
\]

The outer collars deliberately do not follow this interchange. Around
the positional placeholder \(A\), both bases use the
\(\widehat A^\pm\) collars; around positional \(B\), both use the
\(\widehat B^\pm\) collars.

## 3. The six actual frames

Choose six distinct labels outside \(C\), denoted

\[
                         x,a,b,y,c,d.                \tag{3.1}
\]

Use the two internally disjoint paths

\[
 \alpha=(x,a,b,y),\qquad \beta=(x,c,d,y).           \tag{3.2}
\]

Their six edges give six distinct tops

\[
 U_i=C\cup\{\alpha_i,\alpha_{i+1}\},\qquad
 V_i=C\cup\{\beta_i,\beta_{i+1}\}
 \quad(0\le i\le2).                                \tag{3.3}
\]

On the old shore use the plus frame on every edge:

\[
 \omega^+(\alpha_i,\alpha_{i+1})\text{ on }U_i,
 \qquad
 (\omega')^+(\beta_i,\beta_{i+1})\text{ on }V_i.   \tag{3.4}
\]

On the new shore use the corresponding six minus frames:

\[
 \omega^-(\alpha_i,\alpha_{i+1})\text{ on }U_i,
 \qquad
 (\omega')^-(\beta_i,\beta_{i+1})\text{ on }V_i.   \tag{3.5}
\]

Every object in (3.4)--(3.5) is a literal cyclic order of its displayed
top.

### Lemma 3.1 (two open conveyors)

For every interval length \(h\), the aggregate new-minus-old derivative
is

\[
 \boxed{
 \Delta_h=d_h(\omega;x,y)+d_h(\omega';x,y).}        \tag{3.6}
\]

#### Proof

Fix a positional interval. If it contains neither or both placeholders,
every edge derivative is zero. If it contains \(A\) but not \(B\), the
first path telescopes as

\[
 \sum_{i=0}^2
 \left(e_{K\cup\{\alpha_{i+1}\}}
       -e_{K\cup\{\alpha_i\}}\right)
 =e_{K\cup\{y\}}-e_{K\cup\{x\}}.
\]

The second path has the same orientation and gives the corresponding
endpoint difference for \(\omega'\). The \(B\)-only case reverses both
signs. This is (3.6), phase by phase. \(\square\)

Combining (2.4) and (3.6),

\[
                              \Delta_H=0.            \tag{3.7}
\]

## 4. Exact positive-depth support

Fix \(1\le q\le H\), put \(h=H+q\), and define

\[
 I_q=\{0,1,\ldots,q-1\}
       \cup\{H,H+1,\ldots,H+q-1\}.                 \tag{4.1}
\]

A context at \(A\) in \(\omega\) and one at \(B\) in \(\omega'\)
agree precisely while neither reaches an outer collar. In the index
notation of (1.3), this gives

\[
 K_{A,t}^{\omega}(h)=K_{B,t}^{\omega'}(h)
 \quad(q\le t\le H-1).                              \tag{4.2}
\]

Similarly,

\[
 K_{B,t}^{\omega}(h)=K_{A,t}^{\omega'}(h)
 \quad(q\le t\le H-1).                              \tag{4.3}
\]

The signs in (1.4) are opposite in each equality, so all these interior
contexts cancel in (3.6). Thus, with

\[
                         g(K)=e_{K\cup\{y\}}-e_{K\cup\{x\}}, \tag{4.4}
\]

the complete residual is

\[
\boxed{
 \Delta_{H+q}
  =\sum_{t\in I_q}\bigl(
       g(K_{A,t}^{\omega}(h))-g(K_{B,t}^{\omega}(h))
      +g(K_{A,t}^{\omega'}(h))-g(K_{B,t}^{\omega'}(h))
                         \bigr).}                   \tag{4.5}
\]

### Lemma 4.1 (literal support count)

The \(8q\) core contexts in (4.5) are pairwise distinct. Consequently
the \(16q\) target sets obtained by adjoining \(x\) or \(y\) are
pairwise distinct, and

\[
 \|\Delta_{H+q}\|_0=\|\Delta_{H+q}\|_2^2=16q.     \tag{4.6}
\]

#### Proof

Within one context family, the intersection with the union of its
predecessor inner and predecessor outer arms has size exactly \(t\).
Thus different \(t\)'s give different sets. Contexts of inner type \(A\)
and inner type \(B\) cannot agree because every boundary context contains
a complete inner arm of its own type, and the four inner arms are
disjoint.

It remains to compare the two occurrences of one inner type. For
successor-heavy indices \(0\le t<q\), the context reaches a successor
outer collar: the \(A\)-type pair uses respectively
\(\widehat A^+\) and \(\widehat B^+\), and the \(B\)-type pair uses them
in the opposite order. For predecessor-heavy indices
\(H\le t\le H+q-1\), the same argument uses the disjoint collars
\(\widehat A^-\) and \(\widehat B^-\). Hence no remaining pair agrees.
Adjoining different endpoint labels preserves distinctness and separates
the \(x\)-coordinates from the \(y\)-coordinates. Every coefficient in
(4.5) is therefore \(+1\) or \(-1\), proving (4.6). \(\square\)

In particular, (4.5) contains \(8q\) positive and \(8q\) negative
targets. This is the promised exact all-depth action.

## 5. Direct/root-form complementation and exact middle ownership

Both conveyors telescope to the same virtual endpoint top

\[
                         U_*=C\cup\{x,y\}.           \tag{5.1}
\]

Only after this telescoping do we complement. Let

\[
 \kappa_h^{U_*}e_T=e_{U_*\setminus T}.              \tag{5.2}
\]

Complements of the \(h\)-windows of a cyclic order on \(U_*\) are its
\((M-h)\)-windows. Hence

\[
 d_{M-h}(\theta;x,y)
   =\kappa_h^{U_*}d_h(\theta;x,y)
 \quad(\theta\in\{\omega,\omega'\}).               \tag{5.3}
\]

At \(h=H\), equations (3.7) and (5.3), with \(M-H=m\), give

\[
                              \Delta_m=0.             \tag{5.4}
\]

For a physical top \(U\) and root \(A_U=[n]\setminus U\), the middle
target \(A_U\cup I_H\) is the global complement of the direct
\(m\)-window \(U\setminus I_H\). Applying global complementation to
(5.4) shows that the two shores have identical physical middle incidence
vectors.

We now verify the stronger squarefree assertion.

### Lemma 5.1 (both middle shores are squarefree)

No physical middle target occurs twice on either side of (3.4)--(3.5).

#### Proof

It is equivalent to prove distinctness of the direct \(m\)-windows.
Complement such a window inside its own top. Because the placeholders
are more than \(H\) apart, the complementary \(H\)-window contains
zero or one placeholder, never both.

If it contains neither, the direct \(m\)-window contains both outside
labels of its top. That unordered outside pair identifies its edge among
the six distinct edges in (3.3).

If it contains exactly one placeholder, the direct window contains
exactly one outside label. Two such targets can agree only for two edges
sharing that outside label. Along one path, an internal label occurs once
in positional role \(A\) and once in role \(B\). Equality would require
an \((H-1)\)-context at \(A\) to equal one at \(B\), impossible because
the corresponding inner arms are disjoint.

The two paths share only \(x\) and \(y\). On the old plus shore, the two
occurrences of \(x\) are both in role \(A\), so equality would compare
\(\mathcal F_B^H(\omega)\) with
\(\mathcal F_B^H(\omega')=\mathcal F_A^H(\omega)\); these families are
disjoint. The two occurrences of \(y\) similarly compare
\(\mathcal F_A^H(\omega)\) with
\(\mathcal F_A^H(\omega')=\mathcal F_B^H(\omega)\).
On the new minus shore the positional roles reverse, giving the same two
disjoint comparisons. Thus no duplicate exists. \(\square\)

Since both middle incidence vectors are squarefree and equal, the two
shores partition one identical set of \(6M\) middle targets. The exchange
therefore preserves literal exact middle ownership.

For \(1\le q\le H\), put \(h=H+q\). Equations (4.6) and (5.3) give the
direct lower derivative

\[
 \Delta_q^{\rm dir}=\kappa_{H+q}^{U_*}\Delta_{H+q},
 \qquad \|\Delta_q^{\rm dir}\|_2^2=16q.            \tag{5.5}
\]

The root-form target \(A_U\cup I_{H+q}\) is the global complement of
the direct \((m-q)\)-window \(U\setminus I_{H+q}\). Its derivative is
therefore a coordinate-permutation copy of (5.5), with the same support
count and norm.

The opposite sign is exactly fixed. For every \(1\le h\le H\), the
radius-\(h\) context families in the two bases are interchanged just as
in (2.3), because no outer collar is reached. Hence

\[
 d_h(\omega';x,y)=-d_h(\omega;x,y),\qquad \Delta_h=0. \tag{5.6}
\]

The radius-zero endpoint is trivially fixed as well. After
complementation, this says that the direct \((m+q)\)-deck and the
root-form \((m-q)\)-deck have zero derivative for \(0\le q\le H\).
Thus the packet acts at every positive depth on the direct-lower / 
root-form-upper pair and preserves the opposite pair exactly. No
two-sign contraction is claimed.

### Protected deleted phase

The complete-deck theorem also has a repaired variant. In both bases the
arc between the inner \(A^+\) and inner predecessor block at \(B\)
contains the common consecutive segment

\[
                   \widehat A^+,F_1,\overleftarrow{\widehat B^-},
\]

of length at least \(2H\), containing neither placeholder. Choose the
deleted complementary short interval, and all its extensions through
length \(2H\), inside this segment. Its label set is unchanged by every
one of the six transpositions. Deleting the corresponding phase from
each frame therefore changes neither the middle identity nor any
derivative (5.5). Squarefreeness is inherited by deletion.

No arbitrary unsynchronised deleted phases are claimed.

## 6. Exact floor-corrected energy

Let \(\mathcal T\) be a controlled target layer. All admissible states
there have a common mass \(G\). Put

\[
 a=\left\lfloor {G\over|\mathcal T|}\right\rfloor,
 \qquad
 \mathcal E_a(L)={1\over2}\sum_{T\in\mathcal T}
                   (L_T-a)(L_T-a-1).                \tag{6.1}
\]

This is exactly zero on the floor/ceiling lattice. For every zero-sum
integer derivative \(\Delta\), direct expansion gives

\[
 \mathcal E_a(L+\Delta)-\mathcal E_a(L)
 =\langle L,\Delta\rangle+{1\over2}\|\Delta\|_2^2. \tag{6.2}
\]

The floor baseline \(a\) disappears only because \(\sum_T\Delta_T=0\).
For the doubled CPCR convention, every displayed energy derivative is
twice the one here.

Let \(\Gamma^0,\Gamma^1\) be the old and new six-frame packet vectors at
this layer, and \(\Delta=\Gamma^1-\Gamma^0\). Define the coordinate
involution

\[
 \rho:x\leftrightarrow y,qquad a\leftrightarrow b,qquad
 c\leftrightarrow d,qquad \rho|_C=\mathrm{id}.     \tag{6.3}
\]

It reverses each path and sends the old plus frame on every edge to the
new minus frame on the reversed edge, without changing its positional
base. It also sends each root to the root of that reversed edge. Thus at
every direct and root-form layer

\[
                         \rho\Gamma^0=\Gamma^1,
 \qquad \|\Gamma^0\|_2=\|\Gamma^1\|_2.             \tag{6.4}
\]

For an arbitrary fixed external load \(R\), (6.2)--(6.4) give

\[
\begin{aligned}
 \mathcal E_a(R+\Gamma^1)-\mathcal E_a(R+\Gamma^0)
 &=\langle R+\Gamma^0,\Delta\rangle
       +{1\over2}\|\Delta\|_2^2\\
 &=\langle R,\Delta\rangle
       +{1\over2}(\|\Gamma^1\|_2^2-\|\Gamma^0\|_2^2)\\
 &=\boxed{\langle R,\Delta\rangle}.                \tag{6.5}
\end{aligned}
\]

Therefore the old-to-new exchange descends exactly when the total
external load on its negative support exceeds the total external load on
its positive support. Equality is the exact flat case; there is no
unaccounted raw Gram gain.

For a nonnegative weighted all-depth objective, one common shore choice
has the exact derivative

\[
 \Delta\mathcal E
  =\sum_{q,\varepsilon}w_{q,\varepsilon}
       \langle R_{q,\varepsilon},
                    \Delta_{q,\varepsilon}\rangle. \tag{6.6}
\]

At the middle row the summand is zero by exact ownership preservation.

## 7. A squarefree physical descent witness

The signed direction is not floor-flat against every physical exterior.
Fix one depth \(1\le q\le H\), and choose one negative direct target
\(T_-\) from the complemented support in (5.5). Thus
\(|T_-|=m-q\) and \(T_-\subseteq U_*\).

Choose a fresh set \(Z\) of \(H+1\) labels and a set \(Y\) of
\(q-1\) further labels, all disjoint from
\(C\cup\{x,y,a,b,c,d\}\) and from one another. There is enough room
because the complement of this union has \(m-H-4\) labels, while
\(|Z\cup Y|=H+q\le2H\), and \(m\ge7H\). Put

\[
                         U_e=T_-\,\dot\cup\, Z\,\dot\cup\,Y.
                                                               \tag{7.1}
\]

Then \(|U_e|=M\). Make \(T_-\) one consecutive block in a cyclic order
\(\pi_e\) of \(U_e\). Put a label of \(Z\) immediately on each side
of that block, and arrange the remaining \(q-1\) labels of \(Y\)
among the remaining labels of \(Z\), with a \(Z\)-label separating
successive \(Y\)-labels. This is possible since \(q-1\le H-1\).

Every member of the packet derivative at this direct layer is contained
in \(U_*\), and therefore contains no label of \(Z\). In \(\pi_e\),
the only length-\((m-q)\) interval containing no label of \(Z\) is
the displayed block \(T_-\): outside that block every non-\(Z\) run
has length one, and a \(Z\)-label occurs at each boundary of the block.
Consequently

\[
                         \langle c_{\pi_e}^{m-q},
                                      \Delta_q^{\rm dir}\rangle=-1.
                                                               \tag{7.2}
\]

This exterior is also compatible with exact middle ownership. Every
direct middle \(m\)-window of \(\pi_e\) contains a label of \(Z\),
because its complementary \(H\)-window cannot contain all \(H+1\)
labels of \(Z\). No direct middle target of the six-frame packet
contains a label of \(Z\). Hence the \(M\) middle targets of
\(\pi_e\) are disjoint from the common squarefree packet support.
The seven frames therefore form a squarefree partial middle factor on
both shores.

Global complementation gives the identical score \(-1\) on the
corresponding root-form layer. Thus a literal exact-middle-compatible
physical exterior makes the exchange strictly descending by one
floor-energy unit at the prescribed depth, or by two in the doubled
convention.

This proves genuine physical floor descent. It does not assert that every
global state exposes the favorable exterior, nor that this seven-frame
partial factor always extends to a full resolution.

## 8. Exact boundary and accounting

The packet has

\[
 \Delta_0=0,
 \qquad
 \|\Delta_q\|_0=\|\Delta_q\|_2^2=16q
 \quad(1\le q\le H).                               \tag{8.1}
\]

Hence one sign has exact total moved support

\[
                         \sum_{q=1}^H16q=8H(H+1).   \tag{8.2}
\]

For \(H=O(\sqrt{m\log m})\), this is \(O(m\log m)=o(W)\), where
\(W=\binom{2m}{m}\).

Proved here:

1. six literal cyclic frames on each shore;
2. squarefree and identical middle support;
3. exact nonzero action at every positive depth;
4. exact direct/root-form and protected-deletion accounting;
5. exact floor-corrected descent with no self-toll; and
6. a physical exterior producing strict descent.

Not proved here:

1. a positive-density packing of the packets;
2. a charged-coverage inequality ensuring a favorable packet in every
   high-energy state;
3. an iterative contraction; or
4. coefficient one.

The next exact gate is a coverage theorem for the boundary-context
directions (4.5), subject to overlap of their three-top supports.

## 9. Three-top compression

The two length-three paths are not needed for existence. Let

\[
                         \gamma=(x,y),\qquad
                         \eta=(x,a,y),               \tag{9.1}
\]

and use the three distinct tops

\[
 C\cup\{x,y\},\qquad C\cup\{x,a\},\qquad
 C\cup\{a,y\}.                                     \tag{9.2}
\]

On the old shore put \(\omega^+(x,y)\) on the first top and put
\((\omega')^+(x,a)\), \((\omega')^+(a,y)\) on the other two. Replace
all three plus frames by their minus frames.

### Theorem 9.1 (squarefree three-top conveyor)

This three-top exchange has every conclusion of Sections 3--7, with
\(3M\) middle targets instead of \(6M\). In particular its two middle
supports are squarefree and identical, while at every \(1\le q\le H\)
its direct-lower/root-form-upper derivative is exactly (4.5) and has
squared norm \(16q\). Its floor derivative is (6.5).

#### Proof

The one-edge path contributes \(d_h(\omega;x,y)\). The two-edge path
telescopes to \(d_h(\omega';x,y)\). Thus their aggregate derivative is
again (3.6), and Sections 4--6 apply verbatim.

It remains only to check middle squarefreeness. The direct top
\(C\cup\{x,y\}\) and the first two-edge top share only \(x\). On the
plus shore, equality of one-outside-label middle targets would compare
\(\mathcal F_B^H(\omega)\) with
\(\mathcal F_B^H(\omega')=\mathcal F_A^H(\omega)\), which are disjoint.
The direct top and the terminal two-edge top share only \(y\), and the
comparison is
\(\mathcal F_A^H(\omega)\) versus
\(\mathcal F_A^H(\omega')=\mathcal F_B^H(\omega)\). The two path edges
share only \(a\), in opposite positional roles, and again compare the
disjoint \(A\)- and \(B\)-context families. Two-outside-label targets
identify their top edge, and there are no zero-outside-label middle
targets because no radius-\(H\) window contains both placeholders. This
proves squarefreeness on the plus shore. The minus shore merely reverses
all positional roles and gives the same comparisons.

The coordinate involution \(x\leftrightarrow y\), fixing \(a\) and
\(C\), sends the plus direct-edge frame to its minus frame and exchanges
the two plus path-edge frames with the two minus path-edge frames. Hence
the two packet norms agree, and (6.5) follows. \(\square\)

Within the model of two simple paths with common endpoints and pairwise
distinct edge tops, three touched tops are minimal. Indeed, two distinct
paths with at most two edges in total would both have length one, hence
would both be the same edge \(xy\) and the same top. This is only a
minimality statement for the conveyor architecture. An arbitrary
two-top exact frame trade is not ruled out here.

## 10. Absolute one-top no-go and the remaining two-top gap

The three-top result is close to minimal in an unconditional sense: one
top can never work.

### Proposition 10.1 (one-top middle rigidity)

Let \(2\le H<M/2\). If two cyclic frames on one fixed rank-\(M\) top
have the same middle deck, then their cyclic orders differ only by
rotation or reversal. Consequently all of their interval decks agree,
so every one-top exact-middle exchange is load-neutral at every depth.

#### Proof

Complementing the common middle deck inside the fixed top gives the same
family \(\mathcal D\) of cyclic \(H\)-windows for both orders. Form a
graph on \(\mathcal D\), joining two windows when their intersection has
size \(H-1\). In a cyclic order with \(M>2H\), two distinct
\(H\)-windows have intersection size \(H-1\) exactly when their starting
positions are consecutive. Thus this graph is the frame's cycle
\(C_M\), determined solely by \(\mathcal D\).

The cyclic sequence of window sets is therefore determined up to reversal
and rotation. After choosing one orientation, the singleton differences

\[
                         S_{i+1}\setminus S_i

\]

recover, in cyclic order, the label entering at every step. Hence the
underlying cyclic label order is determined up to the same dihedral
ambiguity. Rotation and reversal preserve every unphased interval deck,
which proves the claim. \(\square\)

Therefore the absolute support size of a nonneutral exact-middle frame
exchange lies in \(\{2,3,\ldots\}\), and Theorem 9.1 gives the upper
bound three. Whether an arbitrary squarefree two-top exchange exists is
not settled here. The exact minimal-degree boundary is

\[
                         2\le d_{\min}\le3.          \tag{10.1}
\]
