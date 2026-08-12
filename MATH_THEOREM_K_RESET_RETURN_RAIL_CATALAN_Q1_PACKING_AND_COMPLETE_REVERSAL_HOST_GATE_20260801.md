# Catalan-scale q1 packing and a complete-reversal host gate for the resident reset rail

**Date:** 2026-08-01  
**Lane:** K, protected host planting for the all-depth three-return packet  
**Status:** exact abstract packing theorem, integration of the known
one-packet root/lower-q1 host and the coefficient-one `d`-overlap/twin-bank
opening, an exact sufficient fixed-exterior global-join lemma, and the
corrected one-oriented reversal-quotient host reduction.  The packet's local
cut collateral is paid with zero appended source letters and `O(d)` reserved
owner positions.  No all-`m` simultaneous protected-forest extension,
exterior all-width preservation, terminal compiler, or regenerative
construction is claimed.  A separately replayed `k=17` factor now closes
the finite owner/lower/immediate-upper row only.

## 0. Outcome

The resident reset-return packet of
MATH_THEOREM_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md
has \(M=4d+2\) roots and \(M\) distinct immediate colours on each shore.
Two useful consequences can be proved without assuming a host factor.

1. Its complete coordinate orbit contains a root/lower/upper-q1-disjoint
   family of size at least

   \[
      \left\lceil {N_{\min}\over3(4d+2)^2}\right\rceil,
      \qquad
      N_{\min}=\min_{s\in\{r-1,r,r+1\}}\binom{k}{s}.       \tag{0.1}
   \]

   In the odd central case \(k=2m+1,r=m\), this is

   \[
      \left\lceil
       {m\over m+2}{\binom{2m+1}{m}\over3(4d+2)^2}
      \right\rceil.                                       \tag{0.2}
   \]

   Hence, for fixed \(c>0\), \(d\le c\sqrt m\) gives at least
   \((1/(24c^2)+o(1))\operatorname{Cat}_m\) abstract packets.
   Root/q1 scarcity is therefore not the asymptotic obstruction.

2. Suppose a (possibly nonlocal) connector plants the packet in an ambient
   factor and leaves the two phases with the **same connected undirected
   degree-two component**. If one packet edge is reversed, orientation
   rigidity forces the whole touched component to reverse. Subject to a
   one-phase depth-\(d\) guard, every packet--ambient crossing window, every
   derivative inventory, and the phasewise compiler incidence graph then
   transports by that same reversal. A nondegenerate ordinary two-edge
   splice cannot meet this interface while preserving an exact upper-q1
   palette; on the exact face the connector must have support at least
   three (or use a separately compensated global palette change).

Separately, the frozen protected-factor theorem supplies one
phase-common q1 two-factor host for the opened packet when
\(m_{\rm ML}\ge8d+4\), where \(m_{\rm ML}\) is its
\(ML_{m_{\rm ML}}\) parameter.
That closes one-packet incidence degrees, not the upper-surjective,
low-component, resident/compiler refinement or a simultaneous packet bank.

The two statements do **not** prove that the packed packets occur in one
factor.  For a fixed-exterior local phase switch they sharpen the surviving
gate to a common-undirected, collar-safe connector.  For the weaker
existential same-parity induction, however, global reversal changes the
quantifiers: construct one oriented complete child (host, witnesses,
opening and compiler) and reflect the whole certificate.  No fixed-address
cross-phase intersection is then required.  The surviving gates are the
one-oriented prescribed-factor extension, topology, exterior cross-window
preservation, the terminal compiler, and regeneration of a reversal-closed
boundary orbit.

There is no longer a local quadratic opening-debt row for the canonical
construction.  Prepending the last `d` cyclic antecedent letters uses the
`d` boundary positions already forced in any depth-`d` linear antecedent,
produces every packet owner once, and leaves exactly two upper Ferrers
triangles.  Explicit `2d`- and `3d`-owner Johnson paths cover those triangles;
before any collar is added, the exact local protected object reserves

\[
             (4d+2)+5d=9d+2                             \tag{0.3}
\]

owner positions and adds no source letter beyond the coefficient-one word.
Each bank path has clipped deficits at both ends.  The frozen two collars
repair only `P_X`-right and `P_U`-left.  Therefore a resident embedding must
either supply explicit ambient continuations at `P_X`-left and `P_U`-right
(then the protected count is at most `11d+2`) or use two further collars
(at most `13d+2`, conditional on a collision-free filler/continuation
realization).  At `k=17` a different literal `h=2` bank has now been embedded
in a seven-component owner/lower/immediate-upper-complete factor.  The
unresolved global question is whether such a protected factor can be
rethreaded, joined, made resident and deep-upper-complete, and compiled in
one oriented carrier; the finite `k=17` downstream version is recorded
below.

## 1. The q1 footprint orbit

Fix one anchored reset-return packet \({\cal P}\) satisfying

\[
                    r\ge2d+2,\qquad k-r\ge2d+1.            \tag{1.1}
\]

Let \({\cal O}({\cal P})\) be its orbit under all coordinate permutations.
Repeated parameter descriptions which produce the same embedded packet are
identified. For \(P\in{\cal O}({\cal P})\), define its immediate footprint

\[
 \Phi(P)=V(P)\;\dot\cup\;I(P)\;\dot\cup\;U(P),             \tag{1.2}
\]

where \(V(P)\) is its rank-\(r\) root set, \(I(P)\) its rank-\(r-1\)
edge-intersection set, and \(U(P)\) its rank-\(r+1\) edge-union set.
The complete-reversal theorem gives

\[
                    |V(P)|=|I(P)|=|U(P)|=M=4d+2.          \tag{1.3}
\]

All three families in (1.3) are simple.

### Theorem 1.1 (exact orbit-packing lower bound)

The footprint hypergraph

\[
 \left(\binom{[k]}{r-1}\dot\cup\binom{[k]}r
              \dot\cup\binom{[k]}{r+1},
       \{\Phi(P):P\in{\cal O}({\cal P})\}\right)           \tag{1.4}
\]

has a matching of size at least (0.1).

#### Proof

Put \(P_0=|{\cal O}({\cal P})|\) and \(N_s=\binom{k}{s}\).
The symmetric group is transitive on the rank-\(s\) resources. Counting
packet--resource incidences and using (1.3), every fixed rank-\(s\)
resource has degree

\[
                         \Delta_s={MP_0\over N_s}.          \tag{1.5}
\]

Thus the maximum vertex degree is

\[
                         \Delta={MP_0\over N_{\min}}.       \tag{1.6}
\]

More sharply, the conflict graph on packet footprints has maximum degree

\[
 D_{\rm conf}
 \le M\sum_{s=r-1}^{r+1}(\Delta_s-1).                    \tag{1.7}
\]

Indeed, each of the \(M\) resources in layer \(s\) names at most
\(\Delta_s-1\) other packets. Hence a maximal greedy packing has size at
least

\[
 \left\lceil
 {P_0\over 1+M(\Delta_{r-1}+\Delta_r+\Delta_{r+1}-3)}
 \right\rceil.                                           \tag{1.8}
\]

Substitution from (1.5) gives the parameter-free sharpening

\[
 h_{\rm pack}\ge
 \left\lfloor
 {1\over M^2\left(N_{r-1}^{-1}+N_r^{-1}+N_{r+1}^{-1}\right)}
 \right\rfloor+1.                                        \tag{1.9}
\]

The `+1` is valid even when the displayed reciprocal is integral: the
denominator in (1.8) is smaller than
\(P_0M^2\sum_sN_s^{-1}\) by \(3M-1>0\).

For the advertised simpler bound, one greedy packet choice deletes at
most

\[
                         |\Phi(P)|\Delta=3M\Delta          \tag{1.10}
\]

remaining packet footprints (counting a packet more than once only makes
this an upper bound). Greedy selection therefore returns at least

\[
 \left\lceil {P_0\over3M\Delta}\right\rceil
   =\left\lceil {N_{\min}\over3M^2}\right\rceil,           \tag{1.11}
\]

as claimed. \(\square\)

No freeness assumption is hidden here: \({\cal O}({\cal P})\) is the set
of distinct individual \(S_k\)-conjugate footprints, and stabilizers cancel
in the incidence double count. If instead one packs whole orbits of a
smaller group \(\Gamma\) as indivisible bundles, the statement must be
recomputed on the \(\Gamma\)-orbit resource sets. In particular, the packet
resources in each layer must lie in distinct \(\Gamma\)-orbits and the
eligible bundles must be balanced there. Freeness on packet descriptions
alone is insufficient: a fixed-seam family can have arbitrarily many
descriptions while its footprint matching number is one.

The constant \(3\) protects exactly the owner, lower-q1 and upper-q1
layers. Deeper witnesses, occurrence addresses, exterior guards or compiler
tokens require their own conflict terms; Theorem 1.1 supplies none of them.

At \((k,r,d)=(17,8,3)\), \(M=14\) and the three layer sizes are
\((19448,24310,24310)\). Thus (1.11) gives \(34\) individual conjugate
packets, while the harmonic sharpening (1.9) gives \(39\). These are
abstract footprint matchings, not packets simultaneously installed in the
authenticated \(k=17\) factor.

### Corollary 1.2 (Catalan scale)

For \(k=2m+1,r=m\),

\[
 N_{\min}=\binom{2m+1}{m-1}
           ={m\over m+2}\binom{2m+1}{m}.                  \tag{1.12}
\]

Writing \(B_m=\operatorname{Cat}_m=\binom{2m+1}{m}/(2m+1)\),
Theorem 1.1 gives

\[
 {h_{\rm pack}\over B_m}
 \ge {m(2m+1)\over3(m+2)(4d+2)^2}.                        \tag{1.13}
\]

If \(d\le c\sqrt m\), the right side is \(1/(24c^2)+o(1)\).
The selected packets occupy only

\[
 O(B_m d)=O\!\left({1\over\sqrt m}\binom{2m+1}{m}\right)  \tag{1.14}
\]

roots when \(d=\Theta(\sqrt m)\).

Equations (1.13)--(1.14) are purely an abstract Boolean-resource statement.
They neither orient a common factor nor reserve deeper witnesses. In
particular they do not contradict the isometric-wreath obstruction: the
selected conjugates live in different conjugate factors until a non-wreath
planting theorem is supplied.

### Theorem 1.3 (native-wreath edit floor for long returns)

Assume the odd central setting and the anchored packet range
\(m\ge2d+2\). Let \(G_0\) be any disjoint union of complete MSW wreath
cycles, and let \(G\) be any graph of maximum degree two on the same roots.
Put

\[
                         J=|E(G)\setminus E(G_0)|.          \tag{1.15}
\]

Then the number of simple \((2d+1)\)-edge paths in \(G\) whose endpoints
are Johnson adjacent is at most

\[
                         (2d+1)J.                           \tag{1.16}
\]

In particular, if \(G\) contains \(h\) reset-return packets with distinct
designated return paths (for example, a footprint-disjoint bank), then

\[
                         J\ge {h\over2d+1}.                 \tag{1.17}
\]

#### Proof

The every-second owner cycle of a wreath is isometric: endpoints separated
by \(t\) wreath edges have Johnson distance
\(\min(t,2m+1-t)\). At \(t=2d+1\), the two arguments are
\(2d+1\ge3\) and \(2(m-d)\ge2d+4\). Thus a native wreath path of that
length cannot have adjacent endpoints. Every path counted in (1.16)
therefore contains an edge of \(E(G)\setminus E(G_0)\).

In a maximum-degree-two graph, a fixed edge can occupy any one of at most
\(2d+1\) positions in a simple path of \(2d+1\) edges, and each position
determines at most one such path. Charge each counted path to one new edge
on it. This proves (1.16). Every reset-return packet contains its
designated \(F\)-to-\(E\) return path of this length, proving (1.17).
\(\square\)

This is an edit lower bound, not a no-go. For \(h=\Theta(B_m)\) and
\(d=\Theta(\sqrt m)\), it requires only
\(\Omega(B_m/\sqrt m)=o(B_m)\) new edges. The more substantial missing
condition is their correlated extension to one factor, not their scalar
number.

## 2. Exact prescribed-factor extension row

Let \(J(k,r)\) have edge labels

\[
                         \ell(e)=A\cap B,
\qquad                  u(e)=A\cup B                      \tag{2.1}
\]

for \(e=AB\). Let \({\cal P}_1,\ldots,{\cal P}_h\) be a
footprint-disjoint packet bank. Prescribe all their cycle edges and let
\(d_{\cal P}(v)\in\{0,2\}\) be their used root degree. Given allowed
immediate-colour capacities \(b^-_L,b^+_U\), the exact residual host face is
the following zero--one system on unprescribed Johnson edges:

\[
 \sum_{e\ni v}x_e=2-d_{\cal P}(v),                         \tag{2.2}
\]

\[
 \sum_{e:\ell(e)=L}x_e\le b^-_L-n^-_{\cal P}(L),\qquad
 \sum_{e:u(e)=U}x_e\le b^+_U-n^+_{\cal P}(U).             \tag{2.3}
\]

Here the right sides are required to be nonnegative, and forbidden edges
are fixed to zero. Add the desired component/subtour inequalities when a
path forest or one cycle rather than an arbitrary two-factor is required.

### Proposition 2.1 (literal host criterion)

The packet bank extends to a factor with the declared immediate capacities
and topology if and only if (2.2)--(2.3), together with those declared
graphic constraints, has a zero--one solution.

This proposition is taut but load-bearing: Theorem 1.1 proves only that
the prescribed right sides in (2.3) are nonnegative on the packet bank.
It does not prove the correlated residual system feasible. This is the
precise gap between a dense conjugate catalogue and one physical host.

### Theorem 2.2 (known one-packet q1 closure)

The separate protected-factor theorem
MATH_THEOREM_RESET_OPEN_PATH_PHASE_COMMON_Q1_HOST_20260801.md closes
the root-degree equation (2.2) and the **lower-incidence** half of (2.3)
for one packet:

* after opening one common packet edge, the resulting protected incidence
  path extends to one phase-common spanning q1 two-factor when
  \(m_{\rm ML}\ge8d+4\);
* protecting the complete packet incidence cycle gives an isolated
  phase-common factor component when \(m_{\rm ML}\ge8d+6\).

It does not close the upper-capacity half of (2.3): the arbitrary residual
two-factor can repeat or omit paired upper colours. This is a genuine
root/lower-q1 planting theorem, not an assumption of the
present note. In the open mode, linearization protects \(M\) roots but only
\(M-1\) lower colours and \(M-1\) adjacent upper colours; the omitted
packet edge's two q1 labels have to be supplied by the residual factor.
The protected-factor completion guarantees the lower incidence degree row,
but it does not force the paired upper colours to be surjective. Its
residual two-factor also need not be low-component, resident across the
open packet boundary, upper-complete at larger widths, or compiler
feasible.

The factor component containing the protected path is already a
common-undirected host in the sense of Section 3: choosing its two
orientations realizes the two packet phases. Theorem 3.2 will therefore
make all packet--residual crossing-window comparisons automatic **if that
one completed component first passes the one-phase residence and coverage
guards**. The protected-factor theorem supplies no such guard. The
simultaneous Catalan-bank extension and all these refinements remain open
even though the one-packet q1 degree row is closed.

For the reversal-quotient induction of Theorem 3.5 this phase-common output
is stronger than necessary.  Its one oriented representative may be used
directly; alternatively any one-phase solution of (2.2)--(2.3) would
suffice, because the other representative is obtained only after the full
child certificate has been reflected.

The later phase-common protected Catalan criterion uses central shadow Hall
to extend the packet's protected adjacent-upper tickets to distinct rooted
tails. That closes the marginal upper-tail row, not the joint choice of
distinct other heads plus graphic acyclicity, and not arbitrary-width upper
coverage. Those correlated rows remain part of the host gate below.

### 2.3 The coefficient-one protected three-path face

The local cut theorem
`MATH_THEOREM_RESET_RETURN_DOVERLAP_AND_UPPER_FERRERS_TWIN_BANK_20260801.md`
changes the global host face.  Let `K_d^raw` denote the union of:

1. the opened reset--return path on `M=4d+2` packet owners;
2. the `X`-gap path on `2d` owners; and
3. the `U`-gap path on `3d` owners.

This is unconditionally a three-component linear forest with

\[
 |V(K_d^{raw})|=9d+2,\qquad |E(K_d^{raw})|=9d-1,\qquad
 |E(\widehat K_d^{raw})|=18d-2,                          \tag{2.4}
\]

where `widehat K_d^raw` is the alternating incidence lift.  Every protected
owner and every protected lower-q1 colour is distinct.  Before the collars
are attached, the surviving packet path and the two banks also use exactly

\[
 (M-1)+(5d-2)=9d-1                                      \tag{2.5}
\]

pairwise-distinct upper-q1 colours.  Collar upper colours must be charged
to their literal values; their internal simplicity alone is not permission
to treat them as globally new.

The source word of the packet itself has `M+d=5d+2` positions, exactly the
number required to expose `M` depth-`d` owners.  It has no lower or middle
leave.  Its exact remaining leave consists of `d(d+1)` upper targets in two
Ferrers triangles, and the two uncollared banks give literal witnesses for
all of them.  Consequently (2.4) is an `O(d)` reservation *inside* the
ambient owner chronology, not an additive word-length charge.

There are four clipped bank boundaries, not two.  In the notation of the
local theorem their exact nonconstant deficits are:

* `P_X`-right: `eta_1:1` and `x_s:d+2-s`;
* `P_X`-left: `eta_2:1` and `x_s:s+1`;
* `P_U`-left: `eta_3:1` and `u_s:s+1`; and
* `P_U`-right: `eta_4:1` and `u_s:d+2-s`,

with only the nontrivial indexed ranges retained.  The two collars written
in the frozen local note repair the first and third boundaries.  They do
not repair `P_X`-left or `P_U`-right.  Consequently:

* two protected collars plus explicit legal ambient continuations at the
  other two ends use at most `11d+2` protected owners and `11d-1` edges;
* four protected collar paths use at most `13d+2` owners and `13d-1`
  edges, conditional on a collision-free filler/continuation realization.

The protected-subgraph theorem applies directly to `widehat K_d^raw`: since
it has maximum degree two, the owner/lower-q1 factor row closes whenever

\[
                              m\ge18d.                    \tag{2.6}
\]

This says only that some spanning incidence two-factor contains all three
raw protected paths.  It does not repair a clipped boundary, put the paths
in one component, control collar upper colours, make the upper palette
surjective, preserve exterior arbitrary-width witnesses, or produce a
compiler.  Applying the same small-subgraph bound after protecting two or
four collision-free collar paths gives the **conditional** thresholds `m>=22d` or
`m>=26d`, respectively.

One positive upper marginal is nevertheless automatic once a literal
residence completion has been chosen.  Let
`F={(R_i,T_i):1<=i<=h}` be its forced immediate-upper/tail tickets, and
assume the `R_i` and `T_i` are separately distinct and `h<=m`.  The central
shadow inequality

\[
                 |\partial X|\ge |X|+m                  \tag{2.6a}
\]

follows directly from Lovasz--Kruskal--Katona: write
`|X|=binom(x,m+1)` with `m+1<=x<=2m-1`; then the shadow excess is at least
`g(x)=binom(x,m)(2m+1-x)/(m+1)`, and `g` is increasing, so
`g(x)>=g(m+1)=m`.  Therefore deleting the `h` forced uppers and tails leaves Hall:
`|N(X)-{T_i}|>=|X|+m-h>=|X|`.  Hence all forced tickets extend to an
injection of every immediate-upper colour into distinct tails.  Applied to
the raw forest this has `h=9d-1`; conditional collision-free two- or
four-collar completions have
`h<=11d-1` or `h<=13d-1`.  Thus the corresponding protected-subgraph
thresholds are already more than sufficient for this tail extension.

This is the valid positive marginal from
`MATH_THEOREM_A_TWIN_BANK_FIXED_M0_ONE_ORIENTED_HOST_MINMAX_20260801.md`.
That note's assertion that two collars alone complete residence must be read
conditionally on legal ambient continuations at the other two bank ends.
The Hall argument itself is independent of that correction.  It closes the
upper-colour/tail projection, not the fixed-`M_0` head or graphic row.

Here is the exact residual factor system after the local theorem.  Prescribe
one chosen residence-completed enlargement `K_d` of `K_d^raw`, give each
owner `v` its desired final degree
`b_v in {1,2}`, and let `x_e` range over unprescribed Johnson edges.  Put
`n_K^-(L)` and `n_K^+(U)` for the literal protected lower and upper
multiplicities.  If the demanded lower and upper multiplicity intervals are
`[a_L^-,b_L^-]` and `[a_U^+,b_U^+]`, respectively, the residual equations
are

\[
 \sum_{e\ni v}x_e=b_v-d_{K_d}(v),                         \tag{2.7}
\]

\[
 a_L^-\le n_K^-(L)+\sum_{e:\ell(e)=L}x_e\le b_L^-,       \tag{2.8}
\]

\[
 a_U^+\le n_K^+(U)+\sum_{e:u(e)=U}x_e\le b_U^+.          \tag{2.9}
\]

Add the declared path/cycle cut inequalities.  Exact lower-q1 uses
`a_L^-=b_L^-=1`; upper surjectivity uses `a_U^+=1`, while an exact
upper-q1 face also sets `b_U^+=1`.  Equations (2.7)--(2.9) are necessary
and sufficient for the immediate-palette/degree projection with the chosen
topology constraints.  Condition (2.6) proves that reduced assertion only
for `K_d^raw`, after dropping (2.9) and the component requirements.  A
completed `K_d` uses the corresponding `22d-2` or `26d-2` incidence-edge
bound and still requires its literal upper/collar audit.

There is one further Boolean-specific row which must remain joint.  For an
upper colour `R`, orient its selected edge from tail `T` to head `V`, put

\[
                         J=T\cap V,                        \tag{2.10}
\]

and let `M_0` be the predecessor matching.  A rooted occurrence is legal
exactly when

\[
        T\cup V=R,\qquad M_0(J)=T.                         \tag{2.11}
\]

The selected `T`, `V`, and `J` values must be injective on their respective
shores, and the directed arcs `T->V` must satisfy the required graphic
acyclicity.  The corrected head-completion theorem supplies a disjoint
second-facet projection after the tails are fixed, including the protected
tickets.  It does **not** imply (2.11), lower-colour injectivity, or
acyclicity.  Thus generic degree-only rainbow matching cannot replace this
fixed-`M_0` correlation.  Quantitatively, the generic graph theorem asks
for colour classes larger than `2 Delta`; here the Boolean class size is
`m+1` while `Delta=m-1`, already below that threshold for `m>=4`.
Wdowinski's sharp abstract examples at `2 Delta-1` rule out repairing this
gap by a generic bounded-degree shortcut.  Any positive completion must use
the Boolean incidence and rooted equation (2.11).  In particular, after
the Hall extension above, the first open central marginal is not the tail
assignment: it is the functional fixed-`M_0` head/lower injectivity and
graphic acyclicity for those same choices.

On the central face this joint row has a sharper exact obstruction.  Put

\[
 W=\binom{2m-1}{m},\qquad U=\binom{2m-1}{m+1},            \tag{2.11a}
\]

and, for a fixed `M_0` and a chosen legally residence-completed protected
arc set `P`, let `F_(M_0)(P)` be the family of all `M_0`-legal directed
path forests containing `P`.  If `up(F)` is the set of immediate-upper
colours used by `F`, define

\[
 \boxed{\displaystyle
 \Delta_{M_0}(P)=W-1+U-
   \max_{F\in\mathfrak F_{M_0}(P)}
           \bigl(|F|+|\operatorname{up}(F)|\bigr).}       \tag{2.11b}
\]

Set `Delta=+infinity` if the protected arcs are themselves incompatible.
The fixed-`M_0` min--max theorem proves

\[
 \Delta_{M_0}(P)=0
 \quad\Longleftrightarrow\quad
 \begin{array}{c}
 \text{there is an owner-Hamilton, lower-rainbow,}\
 \text{immediate-upper-surjective path containing }P.
 \end{array}                                               \tag{2.11c}
\]

Indeed every such forest has `|F|<=W-1` and
`|up(F)|<=U`; equality of their sum forces both equalities separately.
This is an integral obstruction, not an LP or degree bound.  It is the
sharpest current central host gate.  Even `Delta=0` says nothing about
residence of the unprotected bulk, exterior arbitrary-width witnesses,
the maximal antecedent, or the terminal compiler (2.12).

There is now one exact finite closure of the cycle-factor version of this
gate.  At `k=17,m=9`, a protected 29-owner residual b-flow followed by a
protected-preserving `C_6` walk gives a spanning two-factor with all `24310`
owners, all `24310` lower-q1 colours, and all `19448` rank-10 upper colours.
Orienting its cycles forces a predecessor matching by
`M_0(T intersection V)=T`, so the cyclic analogue of (2.11b) is zero for
that factor.  It has seven components, not one Hamilton path, and its
interiors remain nonresident; thus it is a finite closure of the central
row, not of Theorem 2.3.  The exact downstream port criterion and the
residence boundary-hit lower bound are recorded in
`MATH_THEOREM_K_K17_PROTECTED_CENTRAL_HOST_CLOSURE_AND_DOWNSTREAM_PORT_GATE_20260801.md`.
The independent replay is now frozen: the factor SHA-256 is
`7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df`
and the verifier output SHA-256 is
`d49405282c791e408a20e2ff378aa66317e61c567129f50dd5f2b64ebd8ad9df`.
Its exact circular short-run transversal is `3807` old adjacencies, unchanged
when all 26 protected internal gaps are forbidden.  Thus the finite central
closure forces a global, rather than bounded-local, downstream rethread.

Finally, after an oriented source word `A*` has been built, let
`Adm_A*(S)` be the literal cells whose target value, maximal cap, nonzero
condition and every guard admit target `S`.  The terminal compiler row is
exactly the matching system

\[
 \sum_{c\in Adm_{A^*}(S)}z_{S,c}=1,qquad
 \sum_S z_{S,c}\le1,qquad z_{S,c}\in\{0,1\}.            \tag{2.12}
\]

Only this one-oriented system is needed in the reversal quotient.  Its
reflected matching is the compiler for the opposite representative; no
edge of a fixed-address phase intersection is required.

### Theorem 2.3 (conditional protected-overlap host lemma)

Assume the coordinate supply and marker hypotheses of the local twin-bank
theorem, and suppose one oriented coefficient-one child has the following
certificates.

1. Its owner chronology contains `K_d` on the protected positions, with the
   coefficient-one `d`-overlap source and the two Ferrers witness banks, and
   all four clipped bank boundaries are repaired either by literal ambient
   continuations or by collars.
2. Equations (2.7)--(2.9), the rooted equations (2.10)--(2.11), and the
   declared graphic constraints have a common integral solution.
3. The resulting joins are depth-`d` resident, and every required exterior
   target has a surviving or newly created interval witness.  The two local
   Ferrers triangles use their protected witnesses and are not charged to
   the exterior.  If the induction records occurrence multiplicities rather
   than support only, this clause means an occurrence-injective transport of
   the declared exterior multiset.
4. The completed source satisfies the one-oriented compiler system (2.12).
5. Its exported endpoint, witness, compiler and guard state is closed under
   simultaneous reversal.

Then this gives one complete child with zero additive source-length charge
from the packet opening.  Reversing the entire child and all certificates
gives the opposite packet representative.  No phase-common exterior,
common fixed-address compiler, or second cut audit is needed.

If the immediate upper palette is squarefree, any nondegenerate connector
which joins distinct protected components by changing only two old edges is
excluded by Lemma 3.3 below.  Thus item 2 requires a support-at-least-three
zero-palette circuit or a compensated use of upper-palette slack.  The
theorem is conditional precisely at this topology/correlation/exterior/
compiler conjunction; it does not hide those rows behind the local
`d`-overlap identity.

## 3. A whole-component reversal join

For a directed factor \(F\), write \(|F|\) for its underlying undirected
graph. A **common-undirected host certificate** for two phases
\(F^+,F^-\) consists of a root set \(H\) such that:

1. \(|F^+|[H]=|F^-|[H]\) is one simple cycle, or one simple path with the
   same unordered endpoint pair in both phases;
2. the reset-return packet is a subpath of this component in both phases;
3. at least one packet edge has opposite directions in \(F^+\) and
   \(F^-\); and
4. the selected roots, undirected edges, immediate palettes and all
   required one-phase physical guards are legal in \(F^+\).

The connector producing \(H\) may be a support-three or larger alternating
circuit and may touch several old components. Nothing in the definition
presumes an ordinary two-edge splice.

### Lemma 3.1 (orientation rigidity)

Under conditions 1--3,

\[
                         F^-[H]={\rm rev}(F^+[H]).          \tag{3.1}
\]

#### Proof

A connected undirected cycle has exactly two orientations in which every
vertex has indegree and outdegree one. They are complete reversals. A
connected undirected path likewise has exactly two directed-path
orientations once its unordered endpoints are fixed. Thus two legal phases
on the same component are either identical or complete reversals. The
oppositely oriented packet edge excludes the identical case. \(\square\)

Define the **depth-\(d\) component guard** to mean that every nonconstant
positive coordinate run of \(F^+[H]\) has length at least \(d+1\). If the
component was assembled from already resident pieces, only runs meeting a
changed seam need checking; a connector of support \(s\) exposes at most
the \(2s\) length-\(d\) endpoint collars. The definition itself, however,
is the literal one-phase run condition and does not assume locality.

### Theorem 3.2 (protected complete-reversal host lemma)

Suppose a common-undirected host certificate exists and its depth-\(d\)
component guard holds. Then:

1. the two phases have identical root and immediate-colour inventories;
2. both are depth-\(d\) resident;
3. reversal gives a value-preserving bijection of all cyclic intervals
   (or all linear intervals in the path case), including every interval
   crossing a packet--ambient join;
4. their interval-union and interval-intersection spectra agree at every
   width;
5. in the cycle case, maximal depth-\(d\) antecedents and every derivative
   row are reversals up to the forced index shift; the same holds in the
   path case whenever the chosen boundary convention supplies one valid
   antecedent in the forward phase; and
6. every occurrence-labelled target--cell matching whose cells are
   intervals of the complete touched component transports to the other
   phase by reversing interval addresses.

#### Proof

Lemma 3.1 proves complete reversal of the entire component. The common
undirected edge set gives identical immediate lower and upper labels.
Reversal preserves cyclic runs, so the one-phase component guard proves
residence in both phases. Reversing an interval preserves its member-root
set and therefore its union and intersection, including at every internal
packet--ambient seam. On a cycle, maximal erosion and every derivative
commute with reversal up to the standard index shift. The same algebra
transports any valid linear antecedent together with its boundary
convention. Finally, interval reversal is a bijection on physical cells
and preserves each cell target, so it is an
isomorphism of the two target--cell incidence graphs. \(\square\)

Thus **one** common-undirected connector certificate and **one** physical
phase audit replace separate cross-window and compiler-transport audits
for the touched component. This is transport, not a fixed-address common
cap: the matching cell at address \(I\) is generally sent to a different
address \({\rm rev}(I)\).

If the touched component is the final cyclic word, or the complete final
linear path, Theorem 3.2 handles every exterior window. If it is merely a
block inside a larger unreversed word, the theorem handles all windows
crossing the packet--ambient joins **inside \(H\)** but says nothing about
windows crossing the two outer boundaries of \(H\).

### Lemma 3.3 (exact two-edge obstruction)

In an upper-q1-exact Johnson factor, no nondegenerate ordinary two-edge
cross-splice between distinct components preserves the upper-colour
multiset.

Here “upper-q1-exact” is the squarefree face: every required upper colour
occurs once, so the two removed edges have distinct upper colours.

#### Proof

Let old edges \(ab\) and \(cd\) have distinct rank-\((r+1)\) upper colours

\[
                         U_1=a\cup b,qquad U_2=c\cup d.   \tag{3.2}
\]

Consider the cross-splice \(ad,cb\); the other crossing is symmetric. If
the new upper colours are again \(\{U_1,U_2\}\), first assign
\(a\cup d=U_1,c\cup b=U_2\). The old and new containments imply that both
\(b\) and \(d\) are rank-\(r\) subsets of \(U_1\cap U_2\). Two distinct
rank-\((r+1)\) sets have at most one common rank-\(r\) subset, so \(b=d\),
and the switch is degenerate. The opposite assignment analogously gives
\(a=c\). The excluded case \(U_1=U_2\) is precisely a violation of the
squarefree hypothesis. \(\square\)

Consequently an exact-palette host cannot be built by iterating ordinary
two-switches. It needs a support-three-or-larger zero-palette circuit, or a
larger globally compensated change. With slack capacities a legal
two-switch can still join two cycles; Lemma 3.1 then applies to the joined
common undirected cycle, but that is not the exact-q1 face needed here.

### Corollary 3.4 (the bare-cut collateral statement survives only on its
self-supply face)

In the maximal antecedent of the sharp reset-return packet, every bare
one-copy cut `A_c,A_(c+1),...,A_(c+M-1)` loses at least

\[
                         d(2d-1)                           \tag{3.3}
\]

distinct packet-internal cyclic interval-OR values. More precisely, for
each width \(2\le w\le2d\), the \(w-1\) intervals crossing the cut have
globally unique values *inside the cyclic packet*. The same statement
holds after adding any permanent common core to all packet letters.

Complete-component reversal makes this loss phase-symmetric: the reverse
phase loses the reflected occurrences of the same value family. It does
not create noncrossing packet-internal replacements. Therefore a final
linear word using a **bare opening** of this component must either

1. obtain witnesses for (3.3) from ambient cells or another packet;
2. use a phase-reflected exterior whose crossing intervals supply them; or
3. retain the component cyclically rather than claim the complete cyclic
deck for a bare opening.

The bound (3.3) is not a lower bound on the number of globally missing
targets after host planting: ambient duplicates may repay all of them. It
is the exact uniform lower bound on **self-supply lost by linearizing the
packet**.

It is also not a deficit of the protected construction in Section 2.3.
There the canonical `d`-overlap restores every owner and every lower/middle
target, and the two explicit banks cover the complete remaining upper
leave.  Thus (3.3) remains a correct warning against a bare cut, a lucky-cut
argument, or reversal used as repayment; it is no longer one of the
conditional rows of Theorem 2.3.

#### Proof

This is Theorem 4.1 of
MATH_THEOREM_RESET_RETURN_RAIL_LINEARIZATION_COLLATERAL_20260801.md.
Its short-interval injectivity proof gives
\(\sum_{w=2}^{2d}(w-1)=d(2d-1)\). Reversal bijects the two cut families,
while adding a coordinate common to every packet letter changes neither
equality nor uniqueness. \(\square\)

### Theorem 3.5 (one-oriented complete-host quotient reduction)

Let \({\cal C}^{+}\) be the set of complete oriented child certificates
whose packet representative is \(H_0\) (respectively \(H_1\)).  A member
contains, at minimum,

\[
 (A,T,F,{\cal W},c,{\cal M},{\cal E},\Xi),                \tag{3.4}
\]

where \(A\) is the source word, \(T=D^dA\) its owner chronology, \(F\)
the selected physical factor, \({\cal W}\) the complete upper-witness
bank, \(c\) the final opening, \({\cal M}\) the occurrence-labelled
compiler matching, \({\cal E}\) the ordered endpoint state, and \(\Xi\)
the carried guards.  Let \({\cal C}^{-}\) be the analogous class for
\(H_3\) (respectively \(H_2\)).  Assume that the admissible parent and child
interfaces are closed under simultaneous reversal of every object in
(3.4), with the two endpoint roles exchanged and any unordered fresh
coordinate pair exchanged, and that every legality predicate is invariant
under this transport.

If the optional coordinate exchange is used, child targets and prepared
pins containing those coordinates are transported by the same ground-set
permutation. Likewise prefix/suffix, predecessor/successor and left/right
erosion row types must be exchanged by their declared type involution.

Then reversal is a bijection

\[
                      {\cal R}:{\cal C}^{+}\longrightarrow
                      {\cal C}^{-}.                         \tag{3.5}
\]

Consequently an existential same-parity transition on reversal-orbit
states needs exactly one of the two oriented host systems to be feasible.
In particular:

1. \([H_0]=[H_3]\) and \([H_1]=[H_2]\); no local three-return converter is
   required merely to change between these representatives;
2. if \(G^+\) is the one-phase cap/compiler incidence graph, then
   \(G^-={\cal R}G^+\), and a matching \({\cal M}\) in \(G^+\) transports
   to \({\cal R}{\cal M}\) in \(G^-\); neither a matching in
   \(G^+\cap G^-\) nor one set of fixed physical cell addresses is needed;
3. every predecessor Rado or gammoid rank row transports by

   \[
           r_{{\cal N}^{-}}({\cal R}X)
                    =r_{{\cal N}^{+}}(X),                 \tag{3.6}
   \]

   so a common independent set for two phase matroids is not an induction
   requirement; and
4. the two phases need not be selected simultaneously on one common
   undirected host.  A solution of the one-oriented host equations
   (2.2)--(2.3), or of the protected-overlap system (2.7)--(2.12),
   completed through all one-phase physical rows, determines the opposite
   certificate by reflecting the *entire* completed child.

#### Proof

Literal reversal maps every linear interval \([i,j]\) to
\([n-1-j,n-1-i]\).  It therefore commutes with every derivative up to the
forced index shift and preserves the interval union or intersection value.
It reverses coordinate traces, so it preserves residence.  Reflect each
chosen factor edge, witness occurrence, opening address, compiler cell,
endpoint label and guard address.  This sends a complete legal certificate
to a complete legal certificate and is involutive, proving (3.5).

The packet theorem identifies the reflected endpoint representatives as
\(H_0\leftrightarrow H_3\) and \(H_1\leftrightarrow H_2\).  Reflection is
an incidence-graph isomorphism, so it carries matchings bijectively and
proves item 2.  A matroid or strict-gammoid rank is invariant under ground
set isomorphism, giving (3.6).  Finally, a quotient transition may choose
the parent representative for which the one-oriented construction is
available; its reflected construction represents the same child orbit.
Thus no simultaneous choice of the two physical hosts is involved.
\(\square\)

The interface-closure hypothesis is load-bearing.  The theorem does not
apply when an old exterior is frozen while only the packet is reversed, or
when the next transition demands a named right socket with no accepted
left-reflected socket.  With \(c\) separately oriented components, global
reversal removes only one global binary choice.  If component labels are
fixed it acts by \(\varepsilon\mapsto\varepsilon+{\bf1}\), leaving the
usual \(c-1\) relative phase bits.  If reversal permutes components by an
involutive permutation matrix \(P\), its exact action is
\(\varepsilon\mapsto{\bf1}+P\varepsilon\); its orbits still have size at
most two, although the displayed pairwise differences need not themselves
be invariant.  In those settings the common-undirected lemma above and the
literal three-return packet remain relevant.

### Corollary 3.6 (exact orbit-totality test)

For a complete parent state \({\sf S}\), let \(P({\sf S})\) mean that the
one-oriented system has a complete legal child certificate.  The quotient
transition is total exactly when

\[
       P({\sf S})\ \vee\ P({\cal R}{\sf S})              \tag{3.7}
\]

holds for every parent orbit.  If the transition formulas are reversal
equivariant, the two predicates in (3.7) are equivalent, so it is enough to
prove either one.  A phase-common construction instead asks for two
simultaneous certificates with an identified physical subcertificate (and,
on the fixed-address face, an intersection matching).  That is a strictly
stronger conjunction and is not implied by the quotient target.

#### Proof

A quotient transition may begin with either representative of its parent
orbit, so (3.7) is necessary and sufficient by definition.  Reflecting a
transition proves equivalence of its two terms under equivariance.
\(\square\)

### Corollary 3.7 (exact Pascal reversal holonomy)

Suppose a prospective child glues reversal-quotient parent copies indexed
by a graph \(\Gamma\). Give copy \(v\) an orientation bit
\(\varepsilon_v\), and suppose interface \(e=uv\) is legal exactly when

\[
                         \varepsilon_u+\varepsilon_v=b_e
                         \quad\text{in }\mathbb F_2.       \tag{3.8}
\]

Then the copies admit a joint orientation exactly when

\[
                         \sum_{e\in C}b_e=0               \tag{3.9}
\]

for every cycle \(C\) of \(\Gamma\). Named one-sided sockets are unary
constraints \(\varepsilon_v=s_v\); they are jointly legal exactly when
their prescribed values agree after propagation along every connecting
path. In particular, a gluing tree has no orientation obstruction beyond
its local binary interfaces, while a triangle with \(b_e=1\) on all three
edges is the smallest marginally feasible but globally impossible example.

#### Proof

Summing (3.8) around a cycle cancels every vertex bit, proving necessity.
Conversely choose one root bit in each connected component and propagate
(3.8) along a spanning forest. Equation (3.9) makes every non-tree edge
consistent. Unary constraints impose exactly the stated path-consistency
condition. \(\square\)

Thus the proof-safe exported interface is the complete occurrence-labelled
boundary state modulo simultaneous reversal, together with its relative
orientation torsor. Marginal endpoint, socket and pin inventories are not
enough.

## 4. Correct surviving gate in the two quantifier regimes

The resident reset-return packet itself no longer has a residence,
derivative, or internal phase-transport defect.  The remaining rows depend
on whether phase is a gauge or a local operation.

### 4.1 Reversal-quotient existential induction

For a reversal-closed same-parity induction, the exact remaining rows are:

1. **one-oriented refined factor planting:** solve (2.2)--(2.3), together
   -- or, for the coefficient-one opening, the sharper protected system
   (2.7)--(2.9) -- together with owner simplicity, upper surjectivity,
   residence and the required component constraints, for one chosen
   representative and for whatever packet subfamily is used.  The
   raw `d`-overlap/twin-bank forest reserves `9d+2` owner positions and
   covers the complete local cut leave.  For `m>=18d` its owner/lower-q1
   factor projection closes, but its four clipped bank boundaries still
   require ambient continuation or collars.  The two-collar `11d+2` count
   and threshold `m>=22d` are valid only when the other two boundaries have
   explicit ambient continuations; four protected collar paths, conditional
   on a collision-free filler/continuation realization, give at most
   `13d+2` owners and the corresponding `m>=26d` protected-subgraph bound.
   Conditional on any literal simple completed forest with at most `m`
   upper transitions, central-shadow Hall closes all forced upper/tail
   tickets.  The available head-injective theorem closes only the disjoint
   second-facet projection.  Relative to a predecessor
   matching \(M_0\), the still-open rooted row is the simultaneous choice
   of upper tails \(\psi(R)\), second facets \(\phi(R)\), and lower colours
   \(J(R)=\psi(R)\cap\phi(R)\) such that

   \[
                M_0(J(R))=\psi(R)                         \tag{4.1}
   \]

   for every upper colour \(R\), with \(J\), \(\psi\), and \(\phi\)
   injective on their respective lower, rooted-tail, and head shores, and
   with the directed arcs
   \(\psi(R)\to\phi(R)\) graphic-acyclic.  This joint
   lower/root/head/graphic condition is not implied by the projection.
   Equivalently, on a fixed-`M_0` protected face its exact scalar obstruction
   is `Delta_(M_0)(P)` from (2.11b); the central row closes exactly when
   `Delta=0`;
2. **one-oriented topology:** join the three protected paths, and then
   open the resulting representative as required by the final carrier.
   Lemma 3.3 still rules out a nondegenerate ordinary two-edge join on the
   squarefree upper-q1 face, so the oriented topology repair needs support
   at least three or compensated palette slack.  It need not simultaneously
   realize a second phase on the same undirected graph;
3. **exterior cross-window preservation:** the local `d`-overlap and twin
   banks already repay every packet-internal cut casualty, so no
   `d(2d-1)` ambient-duplicate row remains for this construction.  What
   remains is to preserve or recreate the old exterior witnesses affected
   when the three protected paths and their connector are inserted.  This
   is an occurrence-level host condition, not a scalar packet debt;
4. **one-oriented global witnesses and compiler:** retain every required
   upper target and find one nonempty cap/occurrence-labelled compiler
   matching satisfying (2.12) in the completed representative.  The matching, cap and
   witness bank of the opposite representative are their reflected images;
   there is no additional common-intersection Hall or Rado row; and
5. **orbit-total regeneration:** export an interface closed under reversal
   and prove that at least one representative of every admissible parent
   orbit enters the next Pascal construction with bounded inherited state.
   For a multi-copy child, its binary interface labels must also pass the
   cycle-holonomy and unary-socket conditions of Corollary 3.7.

For the authenticated `k=17` seed, the cyclic owner/lower/rank-10 part of
item 1 is now closed by the seven-factor described after (2.11c).  It does
not close the list above: the exact residence-cut distance is 3807 old
adjacencies, ranks 11--13 still have `1502,295,9` holes, and topology and
the compiler must be solved on the same global rethread.  Thus the finite
frontier has moved from the fixed-`M_0` central projection to items 2--4
plus the residence/erosion part of item 1.

The phase-common q1 host of Theorem 2.2 and the common-undirected lemma of
Section 3 are therefore stronger reusable sufficient certificates, not
necessary quotient-state interfaces.  The abstract packet packing still
does not put coordinate conjugates into one factor, so item 1 remains a
genuine correlated planting problem.

For a construction which declines the `d`-overlap/twin bank and uses a bare
cut, Corollary 3.4 re-enters unchanged: `d(2d-1)` is the packet's exact
short-width self-supply loss and must be repaid elsewhere.  This fallback
does not weaken the protected local theorem.

### 4.2 Fixed-exterior or relative-phase use

The stronger common rows survive precisely when the desired operation is
not global reversal.  They include:

* reversing one packet while holding the rest of the chronology fixed;
* prescribing a named right socket without accepting its reflected left
  socket;
* assigning independent phases to several packets or components (for
  setwise-fixed labels only the diagonal phase bit is gauge; under a
  reversal-induced component permutation \(P\), the action is
  \(\varepsilon\mapsto{\bf1}+P\varepsilon\) and still removes at most one
  global bit); or
* demanding that one physical occurrence or cap cell serve both local
  phases at the same address.

On those faces, a common-undirected touched component, the literal
attachment/predecessor returns, and possibly a common residual
Hall/Rado/cap condition remain necessary.  Global reversal neither repairs
their relative defect nor merges components.

## 5. Dependencies

The local packet and its exact internal scope are those of:

* MATH_THEOREM_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md;
* MATH_AUDIT_K_RESET_LONG_RETURN_COMPLETE_REVERSAL_AND_RADO_FACE_20260801.md;
* MATH_THEOREM_RESET_OPEN_PATH_PHASE_COMMON_Q1_HOST_20260801.md;
* MATH_THEOREM_RESET_RETURN_RAIL_LINEARIZATION_COLLATERAL_20260801.md;
* MATH_THEOREM_RESET_RETURN_DOVERLAP_AND_UPPER_FERRERS_TWIN_BANK_20260801.md;
* MATH_AUDIT_K_RESET_TWIN_BANK_MARKERS_COLLARS_AND_FIXED_M0_GATE_20260801.md;
* MATH_THEOREM_A_TWIN_BANK_FIXED_M0_ONE_ORIENTED_HOST_MINMAX_20260801.md;
* MATH_THEOREM_K17_H2_TWIN_FERRERS_BANK_AND_PROTECTED_ML9_FACTOR_20260801.md;
* MATH_THEOREM_K_K17_PROTECTED_CENTRAL_HOST_CLOSURE_AND_DOWNSTREAM_PORT_GATE_20260801.md;
* MATH_THEOREM_PHASE_COMMON_PROTECTED_CATALAN_CONNECTOR_CRITERION_20260801.md;
* MATH_THEOREM_HEAD_INJECTIVE_COMPLETION_AND_PROTECTED_INDUCED_PATH_20260801.md;
* MATH_THEOREM_GLOBAL_REVERSAL_QUOTIENT_INDUCTION_AND_RELATIVE_PHASE_OBSTRUCTION_20260801.md;
* MATH_AUDIT_K_GLOBAL_REVERSAL_BOUNDARY_TORSOR_AND_PASCAL_HOLONOMY_20260801.md.

The canonical-host distinction uses:

* MATH_THEOREM_K_MSW_ISOMETRIC_WREATH_SQUARE_RETURN_BARRIER_AND_SUPPORT4_ROLE_CONVERTER_20260801.md.

No assertion about an arbitrary fixed MSW factor, global all-depth target
coverage, existence of even one oriented complete host, or
\(\nu(k)=B(k)\) is made.
