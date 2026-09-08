# Monotone-release cyclic completion and the exact tail-area gate

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver, or
long-running computation is used.

## 0. Result

The common exceptional-set criterion can be sharpened without weakening any
cyclic compatibility condition.  An owner need not be released at depth one.
It may keep its already constructed canonical prefix and become free only at a
later transition.

Let

\[
 \varnothing=E_0\subseteq E_1\subseteq\cdots\subseteq E_K
 \tag{0.1}
\]

be a monotone family of released owners.  At transition \(q\), impose the
audited survival and directed crossing inequalities with the set \(E_q\), not
with one common set used at every depth.  These conditions are necessary and
sufficient for one balanced nested resolution satisfying

\[
 P_q(X)=\Gamma_q(X)\qquad(X\notin E_q).
 \tag{0.2}
\]

The point requiring proof is consistency when \(E_q\) grows.  If
\(D_q=E_q\setminus E_{q-1}\), every owner in \(D_q\) is still at its canonical
parent \(\Gamma_{q-1}(X)\).  The previously released paths, together with
these new canonical parent copies, have multiplicity exactly

\[
 r_{q-1}^{E_q}=b_{q-1}-\ell_{q-1}+a_{q-1}^{E_q}.
\]

Thus Hall at transition \(q\) extends the already constructed prefixes; it
does not reroute any earlier layer.

Consequently the following is a single sufficient quantitative gate for
fixed-window cyclic alignment:

\[
 \boxed{
 \sum_{q=1}^K\frac{|E_q|}{c_q}=o(W).}
 \tag{0.3}
\]

Equivalently, one may choose an exact packet cover \(D_q\) separately at each
transition and require

\[
 \boxed{
 \sum_{t=1}^K\frac{\left|\bigcup_{q\le t}D_q\right|}{c_t}=o(W).}
 \tag{0.4}
\]

This is strictly more flexible as a certificate than releasing one common
set \(E\) from depth one, whose cost is
\(|E|\sum_{q\le K}1/c_q\).  Formula (0.4) is the exact least scalar gate in
the monotone-release architecture: it charges a common owner only from the
first transition at which it is needed.

The weighted common-owner overload incidence is sandwiched below this
tail-area exactly.  Hence any certificate satisfying (0.3) also satisfies the
audited pointed-extraction premise, with the full signed spill bounded by an
explicit multiple of (0.3).  The unproved step is now the construction of
packet covers satisfying (0.4), rather than the stronger
\(o(W/\sqrt m)\)-cardinality common cover.

## 1. Exact notation, including all floors

Fix \(A>0\), and put

\[
 n=2m+1,\qquad W=\binom nm,\qquad
 K=\lceil A\sqrt m\rceil\le m-1,
 \tag{1.1}
\]

where the final inequality holds for all sufficiently large \(m\).  Write

\[
 V_q=\binom{[n]}{m-q}\qquad(0\le q\le K).
\]

Fix one oriented exact wreath factor \(F\).  For its middle owner
\(X\in V_0\), let

\[
 X=\Gamma_0(X)\supset\Gamma_1(X)\supset\cdots\supset\Gamma_K(X)
 \tag{1.2}
\]

be the literal same-start cyclic flag, and define

\[
 \ell_q(S)=|\{X:\Gamma_q(X)=S\}|.
 \tag{1.3}
\]

At every depth retain the exact division

\[
 W=c_q|V_q|+\rho_q,
 \qquad
 c_q=\left\lfloor\frac{W}{|V_q|}\right\rfloor,
 \qquad 0\le\rho_q<|V_q|.
 \tag{1.4}
\]

For \(0\le q\le K\le m-1\), one has \(c_q\ge1\).

A balanced load vector has the exact form

\[
 b_0(X)=1,
 \qquad H_0=\varnothing,
 \qquad
 b_q(S)=c_q+\mathbf 1_{H_q}(S),
 \qquad |H_q|=\rho_q
 \quad(1\le q\le K).
 \tag{1.5}
\]

No independent feasibility of the high sets \(H_q\) is assumed.  The packet
conditions below themselves characterize whether these vectors are realized
by the required common resolution.

For \(E\subseteq V_0\) and any depth \(j\), set

\[
 a_j^E(S)=|\{X\in E:\Gamma_j(X)=S\}|,
 \qquad
 r_j^E(S)=b_j(S)-\ell_j(S)+a_j^E(S).
 \tag{1.6}
\]

Then

\[
 \sum_{S\in V_j}r_j^E(S)=|E|.
 \tag{1.7}
\]

For \(\mathcal A\subseteq V_q\), define

\[
 N_q(\mathcal A)
 =\{R\in V_{q-1}:S\subset R\text{ for some }S\in\mathcal A\},
 \tag{1.8}
\]

\[
 \mathcal C_q(\mathcal A)
 =\{X:\Gamma_{q-1}(X)\in N_q(\mathcal A),\ 
          \Gamma_q(X)\notin\mathcal A\},
 \tag{1.9}
\]

and the exact collar

\[
 \begin{aligned}
 \kappa_q^b(\mathcal A)
 &=b_{q-1}(N_q(\mathcal A))-b_q(\mathcal A)\\
 &=c_{q-1}|N_q(\mathcal A)|-c_q|\mathcal A|\\
 &\quad+|H_{q-1}\cap N_q(\mathcal A)|
       -|H_q\cap\mathcal A|.
 \end{aligned}
 \tag{1.10}
\]

There is no proportional or asymptotic replacement in (1.10).

## 2. Exact monotone-release completion theorem

### Theorem 2.1 — growing release sets glue without retroactive changes

Fix \(F\), the balanced integer vectors \(b_0,\ldots,b_K\), and a
monotone release profile (0.1).  There exists one integral nested resolution
\(P\) with load vector \(b_q\) at depth \(q\) and satisfying (0.2) if and
only if, for every \(1\le q\le K\), the following two systems hold:

\[
 \boxed{
 |E_q\cap\mathcal O_q(S)|\ge \ell_q(S)-b_q(S)
 \qquad(S\in V_q),}
 \tag{S_q}
\]

where \(\mathcal O_q(S)=\{X:\Gamma_q(X)=S\}\), and

\[
 \boxed{
 |E_q\cap\mathcal C_q(\mathcal A)|
 \ge |\mathcal C_q(\mathcal A)|-\kappa_q^b(\mathcal A)
 \qquad(\mathcal A\subseteq V_q).}
 \tag{H_q}
\]

A negative collar is handled literally: then the right side in
\((H_q)\) can exceed the entire crossing set, correctly making the system
infeasible.

#### Proof: necessity

Suppose first that \(P\) exists.  Fix \(q\), and write

\[
 D_q=E_q\setminus E_{q-1}.
\]

Every newly released owner has its already constructed canonical prefix:

\[
 P_{q-1}(X)=\Gamma_{q-1}(X)\qquad(X\in D_q),
 \tag{2.1}
\]

because \(X\notin E_{q-1}\).  More generally, since
\(E_{q-1}\subseteq E_q\), every owner outside \(E_q\) is outside
\(E_{q-1}\) and is canonical at both adjacent depths.

The multiplicity of the actual depth-\((q-1)\) positions of owners in
\(E_q\) is therefore

\[
 \begin{aligned}
 p_{q-1}^{E_q}(R)
 &:=|\{X\in E_q:P_{q-1}(X)=R\}|\\
 &=b_{q-1}(R)
   -|\{X\notin E_q:P_{q-1}(X)=R\}|\\
 &=b_{q-1}(R)-\bigl(\ell_{q-1}(R)-a_{q-1}^{E_q}(R)\bigr)\\
 &=r_{q-1}^{E_q}(R).
 \end{aligned}
 \tag{2.2}
\]

At depth \(q\), (0.2) gives in the same way

\[
 |\{X\in E_q:P_q(X)=S\}|=r_q^{E_q}(S).
 \tag{2.3}
\]

Equation (2.3) implies \(r_q^{E_q}(S)\ge0\), which is exactly
\((S_q)\) by (1.6).

Nestedness of the paths in \(E_q\) gives, for every child family
\(\mathcal A\),

\[
 r_q^{E_q}(\mathcal A)
 \le r_{q-1}^{E_q}(N_q(\mathcal A)).
 \tag{2.4}
\]

The two canonical counting identities are

\[
 |\mathcal C_q(\mathcal A)|
 =\ell_{q-1}(N_q(\mathcal A))-\ell_q(\mathcal A),
 \tag{2.5}
\]

\[
 |E_q\cap\mathcal C_q(\mathcal A)|
 =a_{q-1}^{E_q}(N_q(\mathcal A))-a_q^{E_q}(\mathcal A).
 \tag{2.6}
\]

Substitution gives the exact defect identity

\[
 \boxed{
 r_q^{E_q}(\mathcal A)
 -r_{q-1}^{E_q}(N_q(\mathcal A))
 =|\mathcal C_q(\mathcal A)|
  -|E_q\cap\mathcal C_q(\mathcal A)|
  -\kappa_q^b(\mathcal A).}
 \tag{2.7}
\]

Thus (2.4) is exactly \((H_q)\).

#### Proof: sufficiency

Construct the paths in increasing depth, never altering an earlier layer.
At depth zero put \(P_0(X)=X\).  Suppose that layers through \(q-1\) have
been constructed, have their prescribed balanced loads, and satisfy (0.2)
at every completed depth.

The actual parent copies belonging to \(E_q\) have multiplicity
\(r_{q-1}^{E_q}\).  Indeed, (2.2) applies to the already constructed
layer.  Equivalently, the old active copies have multiplicity
\(r_{q-1}^{E_{q-1}}\), and (2.1) adds the canonical copies of \(D_q\):

\[
 r_{q-1}^{E_{q-1}}+a_{q-1}^{D_q}
 =r_{q-1}^{E_q}.
 \tag{2.8}
\]

This is the exact consistency identity for a growing release set.  It also
shows explicitly that release at depth \(q\) is not retroactive.

By \((S_q)\), the required child multiplicities \(r_q^{E_q}(S)\) are
nonnegative integers.  Both sides have total mass \(|E_q|\) by (1.7).
Clone each actual active parent copy according to its current value
\(P_{q-1}(X)\), clone each child \(S\) exactly \(r_q^{E_q}(S)\) times,
and join a parent copy at \(R\) to every clone of a child \(S\subset R\).

For any collection of child clones with support \(\mathcal A\), its size
is at most \(r_q^{E_q}(\mathcal A)\), while its parent-copy neighborhood
has size \(r_{q-1}^{E_q}(N_q(\mathcal A))\).  By (2.7) and \((H_q)\),
Hall's inequality holds.  Hence an integral matching assigns one child to
every active owner in \(E_q\).

Keep all owners outside \(E_q\) on the canonical edge
\(\Gamma_{q-1}(X)\supset\Gamma_q(X)\).  The matched active child load plus
the frozen canonical load is

\[
 r_q^{E_q}+\ell_q-a_q^{E_q}=b_q.
\]

The new edges extend the actual previously constructed parent copies and
do not change any ancestor.  This completes the induction.  The resulting
paths are integral, nested, have load \(b_q\), and satisfy (0.2) at every
depth.  \(\square\)

## 3. The single scalar inequality implying \((\mathrm{CA}_A)\)

For a monotone packet-feasible profile define its tail area

\[
 \mathsf R_A(F,b,\mathbf E)
 =\sum_{q=1}^K\frac{|E_q|}{c_q}.
 \tag{3.1}
\]

If

\[
 \tau(X)=\min\{q:X\in E_q\},
\]

with \(\tau(X)=\infty\) when the set is empty, then exactly

\[
 \mathsf R_A(F,b,\mathbf E)
 =\sum_{X:\tau(X)\le K}\ \sum_{q=\tau(X)}^K\frac1{c_q}.
 \tag{3.2}
\]

Thus an owner is charged only after its first release depth.

### Corollary 3.1 — monotone release implies fixed-window alignment

For every fixed \(A>0\), suppose that for all sufficiently large \(m\)
there exist \(F_m,b^{(m)},\mathbf E^{(m)}\) satisfying Theorem 2.1 and

\[
 \mathsf R_A(F_m,b^{(m)},\mathbf E^{(m)})=o_A(W).
 \tag{3.3}
\]

Then \((\mathrm{CA}_A)\) holds.

#### Proof

Use the resolution given by Theorem 2.1.  At depth \(q\), every mismatch
belongs to \(E_q\), so

\[
 e_q(F_m,P_m)\le |E_q|.
 \tag{3.4}
\]

Consequently

\[
 \sum_{q=1}^K\frac{e_q(F_m,P_m)}{c_q}
 \le \mathsf R_A(F_m,b^{(m)},\mathbf E^{(m)})
 =o_A(W),
\]

which is precisely \((\mathrm{CA}_A)\).  \(\square\)

Define the finite monotone-release number

\[
 \mathsf{MR}_A(m)
 =\min_{F,b,\mathbf E}
   \mathsf R_A(F,b,\mathbf E),
 \tag{3.5}
\]

where the minimum ranges over one exact factor, exact balanced vectors
(1.5), and profiles satisfying every \((S_q)\) and \((H_q)\).  The minimum
is nonempty: take any common balanced nested resolution for \(b\), put
\(E_0=\varnothing\), and put \(E_q=V_0\) for \(q\ge1\).  Therefore the
single quantitative assertion

\[
 \boxed{\mathsf{MR}_A(m)=o_A(W)}
 \tag{MR_A}
\]

is well-defined and implies \((\mathrm{CA}_A)\).

This is the least tail-area assertion inside the monotone-release packet
architecture.  It is not asserted to be logically necessary for every
possible proof of \((\mathrm{CA}_A)\), since a path can leave and later
return to its canonical flag.

## 4. Equivalent common-owner cover form

Call \(D_q\subseteq V_0\) a transition-\(q\) cover if it satisfies
\((S_q)\) and \((H_q)\) with \(D_q\) in place of \(E_q\), for the same
fixed pair \((F,b)\).  Given arbitrary transition covers, put

\[
 E_t=\bigcup_{q\le t}D_q.
 \tag{4.1}
\]

For fixed quotas, both packet systems are monotone under enlarging the
owner set.  Hence \(E_t\supseteq D_t\) is a valid transition-\(t\) cover,
and Theorem 2.1 applies.  Its tail area is exactly

\[
 \boxed{
 \mathsf U_A(F,b;D_1,\ldots,D_K)
 =\sum_{t=1}^K
   \frac{\left|\bigcup_{q\le t}D_q\right|}{c_t}.}
 \tag{4.2}
\]

Conversely, every monotone release profile is obtained by taking
\(D_q=E_q\).  Consequently

\[
 \boxed{
 \mathsf{MR}_A(m)
 =\min_{F,b,D_1,\ldots,D_K}\mathsf U_A(F,b;D_1,\ldots,D_K),}
 \tag{4.3}
\]

where each \(D_q\) is an exact transition cover.  Formula (4.3) is the
precise common-owner incidence form: reuse of one owner at several depths
is retained inside the cumulative unions, and late first use is charged
only on the remaining suffix.

For comparison, the elementary bound

\[
 \mathsf U_A(F,b;D_1,\ldots,D_K)
 \le\sum_{q=1}^K |D_q|\sum_{t=q}^K\frac1{c_t}
 \tag{4.4}
\]

is sometimes useful, but (4.2), not (4.4), is the weaker exact target
because it preserves common-owner overlap.

## 5. Exact relation to weighted overload incidence and extraction

For the fixed common vectors \(b_q\), put

\[
 O_q^b(F)=\sum_{S\in V_q}(\ell_q(S)-b_q(S))_+,
 \tag{5.1}
\]

and define the monotone-release overload incidence

\[
 J_q^\uparrow(F,b;E_q)
 =\sum_{\ell_q(S)>b_q(S)}a_q^{E_q}(S).
 \tag{5.2}
\]

When \(E_q=E\) is constant for all \(q\), (5.2) is exactly the
depth-\(q\) weighted common-owner incidence \(J_q(F,b;E)\) from the
audited H bridge.  Thus (5.2) is its transitionwise extension, not a new
rankwise quota optimization.

The survival inequalities give the exact finite sandwich

\[
 \boxed{
 O_q(F)\le O_q^b(F)
 \le J_q^\uparrow(F,b;E_q)
 \le |E_q|.}
 \tag{5.3}
\]

Here \(O_q(F)\) is the independently optimized balanced spill used in the
audited extraction theorem; no common feasibility is attributed to its
minimizing quota.  After weighting,

\[
 \boxed{
 \sum_{q=1}^K\frac{O_q(F)}{c_q}
 \le\sum_{q=1}^K\frac{J_q^\uparrow(F,b;E_q)}{c_q}
 \le\mathsf R_A(F,b,\mathbf E).}
 \tag{5.4}
\]

Let

\[
 \Delta_A(m)=\max_{q\le K}
 \left\lceil\frac{W}{|V_q|}\right\rceil.
 \tag{5.5}
\]

This is bounded by a constant depending only on fixed \(A\), and
\(c_q\le\Delta_A(m)\) exactly.  In particular the transitionwise version
of H's common-owner incidence obeys the exact finite estimate

\[
 \boxed{
 2\sum_{q=1}^KJ_q^\uparrow(F,b;E_q)
 \le2\sum_{q=1}^K|E_q|
 \le2\Delta_A(m)\,\mathsf R_A(F,b,\mathbf E).}
 \tag{5.5a}
\]

For the full noncentral signed flag, write

\[
 \mathcal D_K^{\mathrm{sign}}
 =\{-K,\ldots,-1,2,\ldots,K+1\}.
\]

Its audited spill is therefore bounded by

\[
 \boxed{
 \mathcal E_{\mathcal D_K^{\mathrm{sign}}}(F)
 =2\sum_{q=1}^K O_q(F)
 \le2\Delta_A(m)\,\mathsf R_A(F,b,\mathbf E).}
 \tag{5.6}
\]

Suppose the imported audited shoulder family satisfies its exact supply
hypothesis

\[
 S_{\mathcal T}\ge\gamma_AKW
 \tag{5.7}
\]

for fixed \(\gamma_A>0\).  Under (3.3), (5.6) gives

\[
 S_{\mathcal T}-\mathcal E_{D_K}(F)
 \ge\gamma_AKW-o_A(W)
 \ge\frac{\gamma_A}{2}KW
 \tag{5.8}
\]

for all sufficiently large \(m\).  Thus the audited pointed cyclic-flag
extraction theorem applies to the same literal exact factor.  In
particular, the monotone-release certificate simultaneously proves
\((\mathrm{CA}_A)\) and supplies the audited pointed endpoint witnesses;
there is no separate floor loss or factor change in combining the two
packages.

Equation (5.3) also fixes the precise role of weighted common-owner
incidence: it is a necessary charged part of the tail area.  The
construction-enabling scalar still to be proved is the full common-owner
union cost (4.2), because transition Hall covers may contain owners whose
canonical depth-\(q\) fibre is not overloaded.

## 6. Exact proved and conditional boundary

Theorem 2.1 is unconditional.  It proves that growing release sets create
no hidden Hall-integrality, path-concatenation, or ancestor-consistency
condition.  Newly released owners retain their canonical ancestors, and
the exact parent-multiplicity identity (2.8) is what permits induction.

The theorem-level quantitative advance is that the former sufficient
condition

\[
 |E|\sum_{q=1}^K\frac1{c_q}=o(W)
\]

may be replaced by the strictly more flexible tail-area condition (0.3),
or equivalently by the common-owner union inequality (0.4).  All floor
baselines and high-quota intersections remain those in (1.10).

The remaining fixed-\(A\) assertion in this lane is exactly
\((\mathrm{MR}_A)\): construct one exact factor, one common system of
balanced vectors, and exact transition covers whose cumulative weighted
union is \(o(W)\).  Once that one scalar inequality is proved, Theorem 2.1,
Corollary 3.1, and (5.8) give fixed-window cyclic alignment and the audited
pointed endpoint extraction on the same literal word.  If
\((\mathrm{MR}_A)\) is proved for every fixed \(A>0\), the already audited
slow diagonal from the family \((\mathrm{CA}_A)\) gives labelled
synchronization and hence the constant-one contiguous-OR theorem.

## 7. Adversarial audit of the gluing step

The following possible failures were checked independently.

1. **No retroactive release.**  An owner entering
   \(D_q=E_q\setminus E_{q-1}\) is outside \(E_{q-1}\), so its actual
   depth-\((q-1)\) position is exactly \(\Gamma_{q-1}(X)\).  Hence (2.8)
   counts actual parent copies, not merely canonical labels.
2. **Hall is tested on partial clone sets.**  A partial collection of child
   clones with support \(\mathcal A\) has size at most
   \(r_q^{E_q}(\mathcal A)\), while its full parent-copy neighborhood has
   size \(r_{q-1}^{E_q}(N_q(\mathcal A))\).  Thus \((H_q)\) proves Hall for
   every partial clone set, not only unions of complete fibres.
3. **Owner labels concatenate.**  Each matched parent copy is an actual
   owner copy inherited from the constructed depth-\((q-1)\) layer.  Giving
   that copy a contained child extends that same owner path; the matching
   does not identify or permute roots retrospectively.
4. **The scalar is only sufficient.**  A path may leave and later rejoin
   its canonical flag, whereas a monotone release profile continues to
   charge it.  Therefore \((\mathrm{MR}_A)\) is the least scalar within this
   monotone-release architecture, but is not claimed equivalent to
   \((\mathrm{CA}_A)\).
5. **Weighted incidence alone is not the tail area.**  The inequality
   \(J_q^\uparrow\le |E_q|\) is one-way.  Owners needed solely for a Hall
   crossing can have zero overloaded-fibre charge.  No estimate of
   \(\mathsf R_A\) from the \(J_q^\uparrow\) alone is asserted.
