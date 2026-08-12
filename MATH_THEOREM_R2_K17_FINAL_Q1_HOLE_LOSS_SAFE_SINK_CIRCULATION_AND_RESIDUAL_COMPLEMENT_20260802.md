# R2 theorem: the final K17 q1 hole has a loss-safe sink circulation

**Date:** 2026-08-02  
**Status:** exact factor-circulation criterion, authenticated support-seven
completion of the necessary non-`D` rank-ten palette, and exact residual
complement theorem. This does not assert residence, the 36 `D`-containing
rank-ten targets, deeper-upper coverage, source, compiler, opening, exterior
windows, or a word.

## 1. Exact sink-circulation formulation

Let `F` be an h1 incidence factor on ordinary rank-eight roots `L` and
rank-nine owners `T`. For an ordinary root whose selected owners are
`{P_L,T^-}`, replacing `T^-` by an unselected owner `T^+` is the contracted
owner arc

\[
 a=(T^-\longrightarrow T^+;L,P_L).
\]

Its old and new q1 colours are

\[
 o(a)=P_L\cup T^-,\qquad n(a)=P_L\cup T^+ .       \tag{1.1}
\]

For binary arc variables `xi_a`, a root-simple alternating circulation obeys

\[
 \sum_{a:T^-(a)=T}\xi_a=
 \sum_{a:T^+(a)=T}\xi_a
 \qquad(T\text{ an owner}),                        \tag{1.2}
\]

\[
 \sum_{a:L(a)=L}\xi_a\le1
 \qquad(L\text{ an ordinary root}),                \tag{1.3}
\]

together with selected/unselected incidence bounds, the fixed `M,D,B`
boundary, all protected and frozen-clause guards, and a literal final
connectivity replay. Equation (1.2) is exactly owner-degree preservation;
(1.3) makes each touched root lose and gain one incidence.

If `m_F(R)` is the current multiplicity of any rank-ten colour, define

\[
 \Delta_\xi(R)=\sum_a\xi_a
 \bigl(\mathbf1_{n(a)=R}-\mathbf1_{o(a)=R}\bigr).  \tag{1.4}
\]

### Theorem 1 (loss-safe sink criterion)

A guarded root-simple circulation is q1 loss-safe exactly when

\[
 \boxed{m_F(R)+\Delta_\xi(R)\ge1
        \quad(R\in\mathcal U_{\neg D}).}            \tag{1.5}
\]

For the one-hole factor with

\[
 R_\star=32058=\mathtt{0x7d3a},
\]

this includes `Delta_xi(R_star)>=1`; every promised incumbent singleton must
have nonnegative net delta. Summed over all rank-ten colours, including the
36 deferred `D`-containing colours,

\[
             \sum_{R\in\mathcal U_{10}}\Delta_\xi(R)=0, \tag{1.6}
\]

so some colour has negative net delta. If loss safety is imposed on that
donor colour as well, its incumbent multiplicity must be at least two. Under
the present necessary non-`D` scope, an unpromised `D`-containing singleton
may instead donate.

#### Proof

Each touched root replaces exactly one q1 occurrence by one occurrence.
Equation (1.4) is therefore the literal multiplicity change, giving (1.5),
while summing it over the complete rank-ten universe gives (1.6). The
circulation and root rows preserve the factor degrees; the remaining guards
are independent hard conditions. \(\square\)

The exact target row in the unrestricted factor-option master has 45 terms.
For every unordered pair `{a,b}` in `R_star`, put

\[
 L_{ab}=R_\star-\{a,b\},\quad
 T_a=R_\star-\{a\},\quad T_b=R_\star-\{b\}.
\]

Then

\[
 \boxed{
 \sum_{\{a,b\}\in{R_\star\choose2}}
 y_{L_{ab},\{T_a,T_b\}}\ge1 .}                     \tag{1.7}
\]

This option row remains complete even if a successful repair changes both
incidences at one root. The smaller arc formulation is complete only for its
declared root-simple move space.

## 2. Exact support-seven construction

The independently replayed one-hole input is

```text
/home/amodo/or15/work/root_k17_q1_targeted_static_20260802/
  transport3_2.best.model
SHA-256 be00a9d0b2470cd334a0b51476185c2ef61c99d28ce61b12f2ff32c26bcac213
```

It has one connected component, satisfies all 16,261 frozen guards, covers
`19,411/19,412` necessary non-`D` colours, and misses only `32058`.

The selected debt-two return is the following literal circulation. `P` is
the unchanged owner at the displayed root.

| root `L` | fixed `P` | old `T^-` | new `T^+` | old colour | new colour |
|---:|---:|---:|---:|---:|---:|
| 29978 | 32026 | 29982 | 30010 | 32030 | **32058** |
| 30002 | 30006 | 30010 | 62770 | 30014 | 62774 |
| 54578 | 54586 | 62770 | 54579 | 62778 | 54587 |
| 50483 | 50995 | 54579 | 50487 | 55091 | 50999 |
| 50455 | 50583 | 50487 | 54551 | 50615 | 54679 |
| 54550 | 56598 | 54551 | 54558 | 56599 | 56606 |
| 21790 | 21822 | 54558 | 29982 | 54590 | 30014 |

The owner sequence is the directed cycle

\[
29982\to30010\to62770\to54579\to50487\to54551
\to54558\to29982.                                  \tag{2.1}
\]

Thus seven distinct roots lose the incidence variables

```text
53759,53841,100178,91285,91208,100072,36593
```

and gain

```text
53760,53846,100171,91279,91213,100073,36592.
```

This is an alternating `C14` in the literal root--owner incidence graph and
is internal to the necessary non-`D` palette.
Owner and root degrees follow directly from (2.1); the `30014` colour is
transported internally and cancels from the net signature. All displayed
colours lie in the necessary non-`D` palette. The exact input multiplicity
replay shows that every uncancelled old colour has at least two providers.
Literal final replay therefore finds gain `{32058}`, no lost promised colour,
all guards true, and one final component.

The promoted factor is

```text
/home/amodo/or15/work/root_k17_q1_targeted_static_20260802/
  q1zero.independent.model
SHA-256 b1fc0d9ca69c8411aad96557f5a47fe031616c88644f5d5691bec705b2b61a31
```

Its independently extended 1,093,878-variable model has SHA-256
`f544cbc2a6c3bf9f9d7500202b4a60cb06660c3b5a1cdd382daec4d8dd4bbb90`.
The exact q1 replay is

```text
required=19412 covered=19412 missing=0 cut_literals=0
```

so (1.5) holds for every promised colour.

The construction is support seven, but no global minimum-support claim is
made. The complete declared C6/star-C8 catalogue at the one-hole state has
no gainful move, and the one-debt return catalogue has no guarded return.
The chosen circuit is the unique length-seven positive row in the recorded
debt-two table. Those facts give bounded-catalogue lower bounds only; they do
not exclude another C8 type, an overlapping compound packet, a non-root-
simple exchange, or an unrestricted option-master solution of smaller
support.

## 3. Exact circuit Benders oracle

For any explicit circuit catalogue `C`, record its base-relative colour
signature `delta_C(R)`. For pairwise root-disjoint compatible circuits, or
when the aggregate signature has been recomputed from the joint final state,
binary circuit-selection variables `lambda_C` obey

\[
 m_F(R)+\sum_C\delta_C(R)\lambda_C\ge1
       \qquad(R\in\mathcal U_{\neg D}),             \tag{3.1}
\]

plus literal edge/root compatibility and final factor guards. Signatures of
overlapping base-relative circuits need not add, because both selected
incidences at one root can change; such packets require joint recomputation
or the final option master below. A missing
colour or displaced singleton separates one exact row (3.1). With prices
`pi_R`, an unguarded root transition has reduced cost

\[
                    1+\pi_{o(a)}-\pi_{n(a)}.        \tag{3.2}
\]

After forcing an arc with new colour `R_star`, the unguarded pricing problem
is a shortest owner-return path. Root uniqueness, multiplicity debt, frozen
clauses and connectivity are structural guards, so the priced path is only
a relaxation until literal replay. The two-debt automaton used to discover
(2.1) is sufficient for that bounded state space; the proof of the promoted
factor is the final simultaneous multiplicity and guard replay, not the
intermediate debt states.

For a completeness-safe optimization or no-go, use final option variables:

\[
 \sum_{e\in\mathcal O_L}y_e=1,
 \qquad
 \sum_{e:T\in e}y_e=b_T,
 \qquad
 \sum_{e:R(e)=R}y_e\ge1,                            \tag{3.3}
\]

with the exact boundary/protection rows. Every feasible final factor differs
from the incumbent by a balanced symmetric difference and hence decomposes
into alternating even circuits. Bounded C6/C8 or debt-state failure is not a
global infeasibility certificate.

## 4. Residual-flow complement after q1 completion

Let `p_e` be the repaired factor diamonds. For every one of the 19,412
promised non-`D` colours choose one actual provider; choosing the least
`(L,T,H)` tuple makes this deterministic:

\[
 x_e\le p_e,
 \qquad
 \sum_{e:R(e)=R}x_e=1.                              \tag{4.1}
\]

Root injectivity is automatic because one ordinary factor root produces one
diamond. Primary owner degree is bounded by the factor degree, and the
primary graph is a subgraph of the normalized ordinary two-path factor.

Define the complementary factor edges by

\[
                            f_e=p_e-x_e.             \tag{4.2}
\]

### Theorem 2 (literal residual complement)

For every selector satisfying (4.1), `f` is an integral saturating residual
flow. In particular,

\[
 |A|=24308-19412=4896,
 \qquad
 \boxed{F(Q)=9792,\quad d(Q)=0.}                    \tag{4.3}
\]

#### Proof

Every unused ordinary root retains its two factor incidences in `f`. At an
owner,

\[
 \deg_f(T)=\deg_p(T)-\deg_x(T)
           =b_T-\deg_Q(T)=c_Q(T).                   \tag{4.4}
\]

Thus `f` sends two units from every one of the 4,896 unused roots and exactly
fills every residual owner capacity, for total flow 9,792. The closed-shore
value theorem gives `d(Q)=0`. \(\square\)

Equivalently, every owner shore satisfies

\[
 2I_A(Y)+J_A(Y)\le\sum_{T\in Y}c_Q(T).              \tag{4.5}
\]

The fixed h1 boundary ledger is

\[
 b_T=2-\mathbf1_{T=B}-d_T^D,qquad \sum_Td_T^D=3,  \tag{4.6}
\]

so `sum_T b_T=48,616=2*24,308`. If the `D` bank is allowed to change, it
must be co-designed through

\[
 c_T=2-\mathbf1_{T=B}-d_T^D-\deg_x(T),             \tag{4.7}
\]

and every Benders deficiency row gains `sum_(T in Y) d_T^D`.

As a fail-closed decoder check, rebuild the residual network and require
flow 9,792. A smaller flow would return a positive closed shore, contradict
the literal complement (4.2), and therefore signals a factor/primary
channel, boundary-ledger, or decoder error. Without `x<=p`, the same min-cut
is a genuine Benders cut rather than a consistency audit.

The primary forest has `24,310-19,412=4,898` components including isolated
owners. The 4,896 complementary ordinary edges have contracted graphic rank
4,896, leaving the two normalized ordinary paths. This is still only the
central factor/primary/residual topology interface.

## 5. Exact scope

The support-seven circulation closes the necessary non-`D` q1 palette and
constructs a residual-perfect non-`D` primary decomposition. It does not
cover the 36 deferred `D`-containing rank-ten targets. It does not prove
positive depth-three residence, the passive physical all-width deck, ranks
11--17, source antecedents, lower or terminal compiler, opening/exterior
windows, regeneration, or a universal word.
