# Coatom lower-exposure ladders: exact endpoint defect and the local common-cap obstruction

Date: 2026-08-01  
Lane: K, additive-constant compiler regeneration  
Status: exact local erosion theorem and exact abstract serial-ladder theorem.
The physical exterior ladders and packet cell are not yet constructed, so no
unconditional regenerative recurrence or additive-constant bound is claimed.

## 0. Result

The zero-owner mixed coatom packet, with union screens at zero-based
transitions

\[
                              \{1,3,5,7\},                       \tag{0.1}
\]

has no owner sidecar.  Its remaining local lower damage consists, at depths
\(2\le q\le d\), of two strict nested chains.  Reindexing by
\(h=d-q+1\), they are

\[
\begin{aligned}
 P_h&=K\cup\{\infty,b,c\}\cup\{f_1,\ldots,f_h\},\\
 S_h&=K\cup\{\infty,a,c\}\cup
                  \{f_{d+1-h},\ldots,f_d\},
 \qquad 1\le h\le d-1.                              \tag{0.2}
\end{aligned}
\]

The new-only chains swap \(a\) and \(b\).

There are two complementary conclusions.

1. The planted maximal-erosion cells realizing (0.2) are **phase
   exclusive**.  Their two exact common-cap domains are disjoint.  Thus
   nesting alone does not supply a phase-common repair ladder.
2. If an exterior phase-common bank supplies one literal path ladder for
   each chain, the \(2(d-1)\) exposed targets have only endpoint defect.
   Complete ladders absorb the packet task with defect zero; two tight
   ladders have exact soft-target defect one.  If only the two endpoint cells
   of each ladder may fail, the sharp bound is three, or two when the packet
   has a private external cell.

This gives a concrete local birth constant, but only under a literal
exterior-ladder certificate.  The current Thread-D packet export has
\(A_\tau=\varnothing\).  In a typed model where packet tasks are mandatory,
that is structural infeasibility, not a finite appendable deficiency.

## 1. Typed compiler deficiency

Let

\[
       G=(\mathcal L\mathbin{\dot\cup}\mathcal T,\mathcal C;E) \tag{1.1}
\]

be the edgewise phase-common, trace-guarded compiler graph after deletion of
the genuine worst-frontier residence ideal.  Vertices in \(\mathcal L\) are
soft lower-target obligations: an unmatched one may be appended at a
terminal cost of one.  Vertices in \(\mathcal T\) are hard packet tasks and
must be assigned literal cells.  Define

\[
 \kappa_{\mathcal T}(G)=
 \min\bigl\{|\mathcal L\setminus V(M)|:
             M\text{ saturates }\mathcal T\bigr\},              \tag{1.2}
\]

with value \(+\infty\) if \(\mathcal T\) is not matchable.

If \(\mathcal T\) is matchable, transversal-matroid basis extension gives

\[
 \kappa_{\mathcal T}(G)
   =|\mathcal L|+|\mathcal T|-\nu(G).                            \tag{1.3}
\]

The distinction in (1.2) is load-bearing.  An isolated packet task gives
ordinary augmented-Hall deficiency one, but it cannot be repaired by
appending a lower target.  Thus it has typed value \(+\infty\).

## 2. Exact two-chain exposure

Put \(n=d+2\).  The old-only targets at depth \(q\) are

\[
\begin{aligned}
 A_q&=K\cup\{\infty,b,c\}\cup
                    \{f_1,\ldots,f_{n-q-1}\},\\
 B_q&=K\cup\{\infty,a,c\}\cup
                    \{f_q,\ldots,f_{n-2}\},
                    \qquad 2\le q\le d.              \tag{2.1}
\end{aligned}
\]

The new-only targets exchange \(a,b\).  Formula (0.2) is (2.1) under
\(h=d-q+1\).  In particular,

\[
 A_{q+1}=A_q-\{f_{d+1-q}\},\qquad
 B_{q+1}=B_q-\{f_q\}.                                  \tag{2.2}
\]

The schedule-optimality theorem proves that these two losses and two gains
per depth are the minimum in the planted twelve-owner fibre.  This remains
a local support statement: outside occurrences may repair the losses.

## 3. Symbolic maximal erosion

Use the maximal-envelope convention

\[
 E_p^\epsilon=\bigcap\{T_i^\epsilon:i\le p\le i+d\},
 \qquad \epsilon\in\{0,1\}.                              \tag{3.1}
\]

In connector row 1, the reversed union screen is between the active triples
\(Ibc\) and \(Ica\).  Its physical envelope index is

\[
              \sigma=5(d+3)+d+2=6d+17.                         \tag{3.2}
\]

For \(0\le t\le d\), the filler part of
\(E_{\sigma+t}\) is

\[
 \{f_1\},\quad \{f_t,f_{t+1}\}\ (1\le t\le d-1),
 \quad \{f_d\},                                      \tag{3.3}
\]

respectively.  Its active part is the left triple at \(t=0\),
\(\{\infty,c\}\) internally, and the right triple at \(t=d\).  Phase zero
has endpoint triples \((Ibc,Ica)\); phase one has \((Ica,Ibc)\).

For \(h=d-q+1\), define the two proper-prefix cells

\[
 c_q^L=[\sigma,\sigma+h),\qquad
 c_q^R=[\sigma+q,\sigma+d+1).                         \tag{3.4}
\]

For a cell \(c\), let \(\Gamma^\epsilon(c)\) be its exact
allowed/mandatory/minimal-hit maximal-erosion domain.

### Theorem 3.1 (the planted chain cells are phase exclusive)

For every \(2\le q\le d\),

\[
\begin{aligned}
 \Gamma^0(c_q^L)
  &=\{K\cup P_q\cup\{b\}\cup Z:Z\subseteq\{\infty,c\}\},\\
 \Gamma^1(c_q^L)
  &=\{K\cup P_q\cup\{a\}\cup Z:Z\subseteq\{\infty,c\}\},\\
 \Gamma^0(c_q^R)
  &=\{K\cup S_q\cup\{a\}\cup Z:Z\subseteq\{\infty,c\}\},\\
 \Gamma^1(c_q^R)
  &=\{K\cup S_q\cup\{b\}\cup Z:Z\subseteq\{\infty,c\}\}, \tag{3.5}
\end{aligned}
\]

where \(P_q=\{f_1,\ldots,f_{d+1-q}\}\) and
\(S_q=\{f_q,\ldots,f_d\}\).  Hence

\[
       \Gamma^0(c_q^L)\cap\Gamma^1(c_q^L)
       =\Gamma^0(c_q^R)\cap\Gamma^1(c_q^R)=\varnothing.        \tag{3.6}
\]

Rows 3 and 5 satisfy the same statement after relabelling.

#### Proof

Unioning (3.3) over the left cell gives allowed set
\(K\cup P_q\cup Ibc\) in phase zero and
\(K\cup P_q\cup Ica\) in phase one.  The occurrence carriers make
\(K\cup P_q\cup\{b\}\), respectively
\(K\cup P_q\cup\{a\}\), mandatory.  Every envelope already meets that
mandatory set, so the only optional active bits are \(\infty,c\).  This is
the first two rows of (3.5).  The right cell is identical with the endpoint
triples reversed, giving the last two rows.  One phase forbids the active bit
mandatory in the other, proving (3.6).  \(\square\)

Thus the local phase-common graph contributes no neighbour to the
\(2(d-1)\) exposed chain targets.  If a common compiler has soft deficiency
at most \(b\), Hall applied to their union forces at least

\[
                         2(d-1)-b                              \tag{3.7}
\]

distinct exterior phase-common neighbours.  With one packet task \(\tau\),
Thread D's second augmented-Hall row sharpens this to

\[
 |N_{\rm ext}(X_d)\cup A_\tau|
       \ge 2(d-1)+1-b,
 \quad X_d=\{A_q,B_q:2\le q\le d\}.                    \tag{3.8}
\]

Therefore \(O(1)\) endpoint *deficiency* still requires \(\Theta(d)\)
exterior cells.  It cannot follow from a constant number of sockets.

## 4. The exact serial-ladder theorem

Let one chain have targets \(x_1,\ldots,x_\ell\) and pairwise distinct safe
cells \(c_0,\ldots,c_\ell\), with guarded common edges

\[
                         x_i\sim c_{i-1},c_i.                   \tag{4.1}
\]

Suppose \(e\) cells are unavailable and \(s\) further distinct surviving
cells are reserved for hard tasks.

### Lemma 4.1 (uniform path transversal)

The exact number of unmatched soft targets is

\[
                              (e+s-1)^+.                         \tag{4.2}
\]

#### Proof

Every proper subset of \(\{c_0,\ldots,c_\ell\}\) matches injectively into
the path edges \(x_1,\ldots,x_\ell\).  Indeed, every proper consecutive
cell block has at least as many incident path edges as cells, and summing
over its components proves Hall.  Equivalently, to leave \(c_j\) unused,
match

\[
 x_i\mapsto c_{i-1}\ (i\le j),\qquad
 x_i\mapsto c_i\ (i>j).                               \tag{4.3}
\]

After the \(e+s\) cells are removed, the remaining cells therefore match
\(\min\{\ell,\ell+1-e-s\}\) targets, proving (4.2). \(\square\)

For disjoint ladders \(j\), hard-task representatives form an SDR.  If
\(s_j(f)\) tasks are assigned to ladder \(j\), the exact serial defect is

\[
 B_{\rm ser}=min_f\sum_j(e_j+s_j(f)-1)^+,                     \tag{4.4}
\]

with \(+\infty\) when no hard-task SDR exists.

For the two coatom chains, \(\ell=d-1\).  In particular:

* two complete \(d\)-cell ladders plus one task give \(B_{\rm ser}=0\);
* two tight \((d-1)\)-cell ladders give \(B_{\rm ser}=1\);
* if each ladder has lost two cells, a task forced into a ladder gives the
  sharp value \(3\), while a private external task cell gives \(2\); and
* an empty task list gives \(+\infty\).

This is exactly Thread D's augmented-Hall phenomenon.  A complete ladder
makes every one of its cells non-coloop: the free cell can be moved to the
chosen packet address by (4.3).  A tight ladder has one tight shore, and
reserving a ladder cell leaves exactly one soft target unmatched.

## 5. The literal exterior-ladder certificate

For nested masks \(S'\subset S\), a physical cell \(c\) supports both in
both phases exactly when, for \(\epsilon=0,1\),

\[
 M_c^\epsilon\subseteq S',\qquad
 S\subseteq A_c^\epsilon,qquad
 S'\cap E_p^\epsilon\ne\varnothing\quad(p\in c),               \tag{5.1}
\]

together with the rank, residence-frontier, and trace-guard requirements.
Thus a literal ladder certificate consists of \(d\) distinct safe cells per
chain, each internal cell passing (5.1) for one consecutive pair, plus a
nonempty packet list and a joint common-cap replay.

For any fixed exterior cell, its neighbours on either chain form an interval
in the chain order.  The mandatory condition in (5.1) is monotone in one
direction, the allowed condition in the other, and the hit conditions are
monotone with target inclusion.  Hence the missing exterior repair is a
convex/serial matching problem.  Convexity alone does not bound deficiency:
the empty exterior bank realizes the linear lower bound (3.7).

## 6. Concrete recurrence constants

Suppose a separate regeneration mechanism controls inherited compiler debt
by

\[
             \kappa_{m+1}^{\rm out}
                  \le \rho_0\kappa_m+\beta_0,qquad \rho_0<1.  \tag{6.1}
\]

If the new coatom exposure is repaired by a ladder bank with exact value
\(B_a\), then

\[
             \boxed{\kappa_{m+1}
               \le\rho_0\kappa_m+\beta_0+B_a.}                 \tag{6.2}
\]

Thus the local birth constant is concrete:

\[
 B_a=0\text{ for complete ladders},\quad
 B_a=1\text{ for two tight ladders},                            \tag{6.3}
\]

with the endpoint variants above.  If the ladder resets every exposed
source, then \((\rho,\beta)=(0,B_a)\).  If it repairs only newborn chains
and inherited debt is merely transported, the bound is
\(\kappa_{m+1}\le\kappa_m+B_a\); a positive \(B_a\) then does not prove a
uniform additive constant.

For (6.2), put

\[
 E=\max\left\{\kappa_{m_0},
          {\beta_0+B_a\over1-\rho_0}\right\}.                   \tag{6.4}
\]

If parity-\(p\) terminal readout has charge
\(c_p+a_p\kappa_m+B_p\), the resulting conditional additive constant is

\[
 C=\max\left\{C_{\rm fin},
   \left\lceil c_o+a_oE+B_o\right\rceil,
   \left\lceil c_e+a_eE+B_e\right\rceil\right\}.               \tag{6.5}
\]

For many packets, (4.4), not a per-packet slogan, is the correct birth
constant.  Private complete ladders and one private task per packet give
zero total birth for arbitrarily many packets.  A one-unit loss per packet
is unbounded.  Nonempty task lists separately do not imply a global SDR.

## 7. Exact boundary

Proved:

* zero owner sidecar and exact two-chain lower exposure;
* the all-\(d\) phase-exclusive maximal-erosion formulas (3.5);
* the exterior-cell lower bound (3.7)--(3.8);
* the exact serial-ladder defect formula (4.4); and
* the concrete conditional birth constants (6.3).

Open:

* an exterior phase-common \(d\)-cell ladder for each chain;
* a nonempty physically certified packet-cell list;
* joint maximal-cap/trace-guard replay and cross-packet SDR; and
* regeneration of inherited compiler debt and both terminal parities.

The weaker serial-safe-search route does not require a common compiler at
intermediate packet phases.  On that route, (0.2) describes a deterministic
hole-routing action, and the remaining theorem is bounded terminal compiler
reachability.  The local obstruction (3.6) does not refute that route.

Dependencies:

* `MATH_THEOREM_COATOM_SCREEN_TENSOR_RESIDENT_ECO_PACKET_20260801.md`;
* `MATH_AUDIT_MIXED_SCREEN_LOWER_DAMAGE_OPTIMALITY_20260801.md`;
* `MATH_THEOREM_THREAD_D_COATOM_TENSOR_COMPILER_PREFIX_AUGMENTED_HALL_GATE_20260801.md`;
* `MATH_THEOREM_INDEPENDENT_COATOM_TENSOR_DMAC_PROFILE_AND_PREFIX_COMPILER_20260801.md`; and
* `MATH_THEOREM_SERIAL_COATOM_SAFE_SEARCH_AND_FINAL_COMPILER_REDUCTION_20260801.md`.
