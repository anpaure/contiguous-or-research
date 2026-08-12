# Rank-twisted macroblocks: audited owner tiling and exact Hall ledger

Date: 2026-07-26

Method: pure mathematics only.  No computation, solver, probabilistic
matching theorem, or web input is used.

## 0. Outcome

This note independently audits
\`MATH_THEOREM_RANK_TWISTED_MACROBLOCK_PACKET_TILING_20260726.md\`
and derives the exact source/target compatibility object left open there.

The conclusions are:

1. The owner construction is valid.  Rank-dependent status cells
   partition every local layer; their products partition the middle
   owners; every product cube of dimension at least \(r\) splits exactly
   into parallel \(Q_r\)'s; and the low-dimension leave is
   \(2^{m+o(m)}=o(W/H)\).
2. Two harmless corrections are needed.  One has
   \(db=m-O(d)\), not \(m+O(d)\).  Also, to compare literally with a
   quartet partition refining every macroblock half, choose \(d\)
   divisible by \(4\).
3. Every selected packet has \(r\) cross-half axes.  Hence the owner and
   dense-crossing gates are genuinely closed.
4. For a lower target \(T\), the exact number of compatible sources in
   the *complete* rank-twisted status atlas is

   \[
   \boxed{
   D_q^-(T)=[z^q]\prod_j
      \left(\sum_{\ell=0}^d
        2^\ell\binom{e_{t_j+\ell}(T_j)}{\ell}z^\ell\right),} \tag{0.1}
   \]

   where \(t_j=|T_j|\) and \(e_k(T_j)\) is the number of edges of
   \(M_{j,k}\) disjoint from \(T_j\).  The upper formula is

   \[
   \boxed{
   D_q^+(U)=[z^q]\prod_j
      \left(\sum_{\ell=0}^d
        2^\ell\binom{f_{u_j-\ell}(U_j)}{\ell}z^\ell\right),} \tag{0.2}
   \]

   where \(f_k(U_j)\) counts \(M_{j,k}\)-edges contained in \(U_j\).
5. For a fixed block allocation \(\ell\), the exact local
   source/target profile ratio is

   \[
   \boxed{
   R_d(t,\ell,h)
    =2^\ell
      {\binom{d-h}{t+\ell-2h}\over
       \binom{d-h}{t-2h}}
    =2^\ell{(d-t+h)_{\underline\ell}\over
                 (t-2h+1)_{\overline\ell}}.}         \tag{0.3}
   \]

   Thus the rank twist has no automatic coefficient-one sign.  At the
   balanced profile \(t=d,h=d/4\),

   \[
       \log R_d(d,\ell,d/4)
          =-{3\ell^2-\ell\over d}
             +O(\ell^3/d^2),                         \tag{0.4}
   \]

   while after summing over the double-pair profile, moving a rank
   \(d-\ell\) target block to rank \(d\) has ratio

   \[
       {\binom{2d}d\over\binom{2d}{d-\ell}}
          =\exp\!\left({\ell^2\over d}
             +O(\ell/d+\ell^3/d^2)\right).           \tag{0.5}
   \]

   The two signs show that the allocation must correlate additions with
   local rank and status; density of crossing axes alone proves neither
   Hall nor a Hall obstruction.
6. The complete candidate graph has enormous average degree, computable
   exactly, but degree abundance is not Hall.  The remaining theorem is
   an integral matching/flow statement for the source *unions* defined by
   (0.1)--(0.2), followed by restriction to the selected \(r\) axes and
   one common compiler order.

## 1. Audit of the owner tiling

Write one macroblock as

\[
 B=A\mathbin{\dot\cup}C,\qquad |A|=|C|=d.           \tag{1.1}
\]

At local rank \(k\), fix the cyclic perfect matching

\[
 M_k=\{a_i c_{i+k}:i\in\mathbb Z_d\}.               \tag{1.2}
\]

For a \(k\)-set \(X\), classify each matching edge as empty, singleton,
or double.  Holding the empty and double edges fixed and allowing every
singleton edge to flip gives a physical cube of dimension equal to the
number of singleton edges.  The statuses determine one cell uniquely,
and every flip preserves rank \(k\).  Thus the cells partition the
rank-\(k\) layer.  Since distinct ranks are disjoint, allowing \(M_k\)
to depend on \(k\) creates no owner overlap.

Tensor the cells over

\[
                       b=\lfloor m/d\rfloor          \tag{1.3}
\]

macroblocks and freeze the fewer than \(2d\) residual coordinates.  A
product cell with \(S\) singleton axes is a literal \(Q_S\).  If
\(S\ge r\), retain any deterministic \(r\)-subset of its axes and freeze
the other \(S-r\) coordinates in every orientation.  The resulting
\(2^{S-r}\) parallel \(Q_r\)'s partition that cell exactly.

For a fixed local-rank vector, all block matchings are fixed.  Under an
unconditioned subset, each of the

\[
                         db=m-O(d)                   \tag{1.4}
\]

matching edges is singleton with probability \(1/2\), independently.
Hence \(S\sim\operatorname{Bin}(db,1/2)\), and, for \(r=o(m)\),

\[
              \#\{X:S<r\}\le
              2^{2db}\Pr(\operatorname{Bin}(db,1/2)<r)
              =2^{m+o(m)}                            \tag{1.5}
\]

for that vector.  There are at most

\[
 (2d+1)^b
   =\exp\!\left(O\!\left({m\log d\over d}\right)\right)
   =2^{o(m)}                                         \tag{1.6}
\]

rank vectors, and the residual coordinates add only \(2^{O(d)}\).
The union bound therefore preserves (1.5).  Restricting to rank \(m\)
can only reduce the leave.  Since \(W=2^{2m-o(m)}\), it is
\(o(W/H)\) for every \(H\le m\).

Every selected axis is an \(A\)-to-\(C\) edge.  Taking \(d\) divisible
by \(4\) permits the old quartet partition to refine every \(A\)- and
\(C\)-half exactly; every selected packet then has

\[
                              s(P)=r.                \tag{1.7}
\]

Finally, as \(k\bmod d\) ranges over \(\mathbb Z_d\), (1.2) exhausts
all edges of \(K_{d,d}\).  The claimed frame union is therefore exact.

## 2. Exact lower compatibility

Let \(T\) be a lower target of rank \(m-q\), and put

\[
                       T_j=T\cap B_j,\qquad
                       t_j=|T_j|.                    \tag{2.1}
\]

Suppose a compatible source adds \(\ell_j\) elements in block \(j\), so
its local rank is

\[
                       k_j=t_j+\ell_j,\qquad
                       \sum_j\ell_j=q.               \tag{2.2}
\]

The relevant status matching is \(M_{j,k_j}\), not \(M_{j,t_j}\).
Define

\[
 e_k(T_j)=|\{e\in M_{j,k}:e\cap T_j=\varnothing\}|. \tag{2.3}
\]

Every deleted source element must lie on one of \(\ell_j\) distinct
edges counted by (2.3).  On each selected empty edge either endpoint may
be the source element; the opposite endpoint is inserted later by the
cube direction.  Conversely every such choice gives a unique compatible
source.  Therefore the local number is exactly

\[
                    2^{\ell_j}
                    \binom{e_{t_j+\ell_j}(T_j)}{\ell_j}. \tag{2.4}
\]

Multiplication over blocks and summation over (2.2) proves (0.1).
Residual frozen coordinates can be included as one bounded exceptional
factor; for \(d=o(\sqrt m)\) they do not change the Gaussian scale.

Formula (0.1) is an upper envelope for the actual packet compiler.  It
allows every singleton axis in the complete product cell.  The physical
tiling retains only \(r\) axes, and one cyclic compiler chooses one
ordered \(q\)-window from each source.

## 3. Exact upper compatibility

Let \(U\) have rank \(m+q\), put \(u_j=|U\cap B_j|\), and suppose the
source omits \(\ell_j\) elements of \(U_j\).  Its local rank is
\(k_j=u_j-\ell_j\).  Define

\[
 f_k(U_j)=|\{e\in M_{j,k}:e\subseteq U_j\}|.         \tag{3.1}
\]

Choose \(\ell_j\) full matching edges and, on each, choose which endpoint
is absent from the source and inserted along the window.  This gives

\[
                    2^{\ell_j}
                    \binom{f_{u_j-\ell_j}(U_j)}{\ell_j}. \tag{3.2}
\]

Summing over \(\sum_j\ell_j=q\) proves (0.2).  Complementation exchanges
(2.3) and (3.1), so lower and upper have the same aggregate asymptotic
scale, but their literal floor choices remain coupled by the common
compiler chronology.

## 4. The exact fixed-allocation profile ratio

Fix one block, a target rank \(t\), an allocation \(\ell\), and put
\(k=t+\ell\).  Evaluate both target and source in the common matching
\(M_k\).  Let \(h\) be the number of double edges.  A target with
\(h\) doubles has \(t-2h\) singleton edges, so its profile count is

\[
 N_t(h)=\binom dh\binom{d-h}{t-2h}2^{t-2h}.         \tag{4.1}
\]

A source in the same preserved-double profile has count

\[
 N_k(h)=\binom dh\binom{d-h}{t+\ell-2h}
                           2^{t+\ell-2h}.            \tag{4.2}
\]

Their ratio is exactly (0.3).  The incidence is biregular: a target has
degree

\[
               2^\ell\binom{d-t+h}{\ell},           \tag{4.3}
\]

and a source has degree

\[
                    \binom{t+\ell-2h}{\ell}.         \tag{4.4}
\]

The identity \(N_t(h)(4.3)=N_k(h)(4.4)\) independently checks (0.3).

At \(t=d,h=d/4\), expand the falling and rising factorials in (0.3).
For \(\ell=o(d^{2/3})\),

\[
\begin{aligned}
 \log R_d
 &=\ell\log2+
   \sum_{a=0}^{\ell-1}\log(d/4-a)
   -\sum_{a=1}^{\ell}\log(d/2+a)\\
 &=-{3\ell^2-\ell\over d}+O(\ell^3/d^2),
\end{aligned}                                       \tag{4.5}
\]

which proves (0.4).  On the other hand, summing (4.1)--(4.2) over \(h\)
recovers the full rank layers.  Taking \(t=d-\ell,k=d\) and applying
Stirling gives (0.5).

Therefore a fixed balanced \(h\)-profile can be source-deficient even
when the rank-summed, center-moving transport is source-rich.  Any
positive proof must move mass between \(h\)-profiles while it centers the
local ranks.  Any negative proof must survive that freedom; freezing
\(h\) and then summing its deficit is invalid because other allocations
use other frames \(M_{t+\ell}\).

## 5. Exact cyclic-frame identities

Write

\[
 I_A=\{i:a_i\in T_j\},\qquad I_C=\{i:c_i\in T_j\},
\]

and let \(\alpha=|I_A|\), \(\gamma=|I_C|\).  If

\[
 h_s(T_j)=|\{i:i\in I_A,\ i+s\in I_C\}|,            \tag{5.1}
\]

then

\[
 e_s(T_j)=d-\alpha-\gamma+h_s(T_j).                 \tag{5.2}
\]

Every ordered occupied \(A\)-\(C\) pair appears at exactly one cyclic
shift.  Hence

\[
 \sum_{s\in\mathbb Z_d}h_s(T_j)=\alpha\gamma,\qquad
 \sum_{s\in\mathbb Z_d}e_s(T_j)=(d-\alpha)(d-\gamma). \tag{5.3}
\]

These identities are the exact quotient structure supplied by the
rank twist.  They show that varying \(\ell\) samples the full cyclic
correlation profile, but they give only an average empty-edge capacity.
They do not make the individual values
\(e_{t+\ell}(T_j)\) independent.

## 6. Global candidate degrees

For a middle source \(X\), let \(S(X)\) be its total number of singleton
status edges in its intrinsic rank-twisted frames.  Selecting any \(q\)
of them produces one candidate lower target and one candidate upper
target.  Thus the complete-atlas degree on either sign is

\[
                              \binom{S(X)}q.          \tag{6.1}
\]

Although the frame depends on the local ranks, the distribution of
\(S(X)\) is the same as for one fixed perfect matching.  Indeed, on one
block,

\[
 \sum_{k=0}^{2d}y^k\sum_{|X|=k}z^{S(X)}
                         =(1+2zy+y^2)^d,             \tag{6.2}
\]

because the status enumerator at a fixed rank is independent of the
particular perfect matching.  Tensoring gives the \(m\)-pair enumerator
when residual coordinates are absent.

The \(q\)-th binomial moment is therefore

\[
 {1\over W}\sum_{|X|=m}\binom{S(X)}q
  =\binom mq2^q{\binom{2m-2q}{m-q}\over W}.          \tag{6.3}
\]

To see this directly, choose the \(q\) matching edges, choose one of two
orientations on each, and complete the remaining middle rank on the
other \(2m-2q\) coordinates.

For \(q=A\sqrt m+O(1)\), (6.3) becomes

\[
 {1\over W}\sum_X\binom{S(X)}q
   =(e^{A^2/2}+o(1))\binom{m/2}q.                   \tag{6.4}
\]

Since

\[
 {W\over\binom{2m}{m-q}}\longrightarrow e^{A^2},   \tag{6.5}
\]

the mean target-side candidate degree is

\[
      (e^{3A^2/2}+o(1))\binom{m/2}q.                \tag{6.6}
\]

This is vast potential multiplicity.  It is not a matching theorem:
many targets may use the same source, and a source supplies only one
cyclic start at a fixed signed depth.

## 7. Exact remaining Hall gate

Let \(\mathcal S\) be the middle owners retained by the \(Q_r\)-tiling,
and let \(\mathcal T_q^\pm\) be the signed target layers.  Define the
complete-atlas compatibility graph by (2.4) and (3.2).  For a target
family \(\mathcal A\), write

\[
 N^\pm(\mathcal A)
   =\{X\in\mathcal S:\text{\(X\) is compatible with at least one
      target in \(\mathcal A\)}\}.                   \tag{7.1}
\]

The quota-one Hall condition is

\[
                         |N^\pm(\mathcal A)|
                            \ge|\mathcal A|           \tag{7.2}
\]

for every \(\mathcal A\).  Floor/ceiling quotas replace the right side
by the required total multiplicity.  Equations (0.1)--(0.2) count
incidences; they do not compute the union (7.1).

Even (7.2) is only the atlas gate.  The literal packet theorem still
must prove all three of:

1. enough compatible edges survive the deterministic choice of \(r\)
   axes in every product cell;
2. one cyclic direction order chooses the required edges simultaneously
   for every \(q\le H\); and
3. lower and upper choices obey the common run vector and the
   three-shore coupling from the quartet trade atlas.

The rank-twisted construction therefore resolves the owner and
dense-cross-axis tolls, but not the Gaussian Hall gate.  The exact next
mathematical target is a cut theorem for (7.1), exploiting the cyclic
correlation identities (5.3) and the rank-centering surplus (0.5).
