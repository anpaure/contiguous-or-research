# Klein four-block `C8`: native packet matroid, physical no-go, and exact compiler boundary

> **Major quotient-fold update.**  Sections 1--6 correctly classify the
> literal four-copy word and its compiler quotient.  A later exact theorem
> now supplies the missing nonliteral physicalization: quotient by owner
> value, select one lower-colour edge at each colour, and obtain one of 16
> degree-two graphs, all Hamilton cycles.  Two per phase are upper-complete.
> Cutting a common edge gives same-endpoint resident Hamilton paths whose
> distinct-value residue is exactly two nested rays per phase.  Section 7
> computes the resulting two-host packet matroid and proves conditional
> background cut zero.  Antitone pairing then gives exact terminal Hall
> defect zero for the canonical threshold marginals.  The host construction
> is only support-exact: a separate audit finds a nonzero graded/contextual
> residue, so regenerative use still requires a phase-sensitive collar or
> equivalent transport theorem.  Thus the literal no-go remains valid, but
> it is no longer the endpoint of the lane.

Date: 2026-08-01  
Lane: R, coherent `C8` / terminal compiler  
Status: exact source-signature and native-matroid theorem; independently
replayed literal obstruction; exact quotient-folded physical central factor
and conditional terminal two-ray Hall closure.  No closed regenerative CBC
lift and no additive-constant upper bound are claimed.

## 0. Verdict

The literal Klein four-block relation uses the four coordinate relabellings

\[
 1,\qquad \beta=(a_1\ a_3),\qquad
 \alpha=(a_0\ a_2),\qquad \alpha\beta
\]

and exchanges phase vectors

\[
                         0110\longleftrightarrow1001.       \tag{0.1}
\]

Its source-signature relation and pointwise phase-common source cap are
valid.  At every depth `q=2,...,d` it also certifies eight distinct native
target values, eight occurrence-labelled native cells, and a jointly legal
perfect identity-cap matching.  Therefore, if

\[
 N=8(d-1),
\]

the exact **certified native restriction** of the packet transversal matroid
at either endpoint is

\[
                 U_{N,N}.                                  \tag{0.2}
\]

The chordless `C8` is the packet-slot/channel Markov support; it is not a
matroid circuit of (0.2).  The unrestricted packet matroid is not determined
by the `C8` relation, because incidences from exterior targets to the native
cells are not recorded.

The literal four-block word is not a physical CBC endpoint.  For every
`d>=2` its four central owner blocks have

\[
 32d+92\text{ owner occurrences but only }8d+24
 \text{ distinct owners},                                  \tag{0.3}
\]

and its lower-q1 palette has

\[
 32d+88\text{ occurrences but only }8d+24
 \text{ distinct colours}.                                 \tag{0.4}
\]

Almost every value in (0.3)--(0.4) has multiplicity four.  Exact `d`-letter
overlap does not identify the owner windows, and uniform block-private tags
destroy the connected cancellation relation.  Thus neither endpoint has a
legal physical compiler-boundary record in the literal model.

Conditional on a future nonliteral quotient weave which removes this
owner/palette multiplicity while retaining the native matching `mu`, the
compiler quotient contracts to one residual background rank cut.  If `D`
is the native target bank, `R=L-D`, and `B` is the background cell bank, then
for one compatible complete cap state `theta`,

\[
 \delta_\theta(T;\mu)
   =|R|-r_{M_B^\theta}(R)
   =\max_{X\subseteq R}
        (|X|-|N_{B,\theta}(X)|)_+.                          \tag{0.5}
\]

Consequently the exact missing datum is not another coherent token count.
For the literal model it is an occurrence-labelled physical weave and, in
one boundary-compatible cap state, the residual rank in (0.5).  The quotient
fold now supplies the weave.  Its remaining datum is the physical occurrence
of two typed source sockets; once they exist, the local residual rank is
exactly full by Section 7.

## 1. The two distinct graphs called `C8`

For `t=d+1-q`, use the eight cube targets in the notation of the coherent
birail theorem:

\[
\begin{split}
 D_q=\{&E_{000}(A_t),E_{100}(A_t),
        E_{010}(B_t),E_{110}(B_t),\\
      &E_{001}(B_t),E_{101}(B_t),
        E_{011}(A_t),E_{111}(A_t)\}.                 \tag{1.1}
\end{split}
\]

The four two-target channels are `alpha,beta,gamma,delta`, and their packet
incidences are

\[
\begin{array}{c|cccc}
 &\alpha&\beta&\gamma&\delta\\ \hline
 p_0&*&*&0&0\\
 p_1&*&0&*&0\\
 p_2&0&*&0&*\\
 p_3&0&0&*&*
\end{array}.                                               \tag{1.2}
\]

Thus the packet-slot/channel graph is the chordless cycle

\[
 p_0-\alpha-p_1-\gamma-p_3-\delta-p_2-\beta-p_0.           \tag{1.3}
\]

Its two unit-margin tables are exactly the endpoint phase vectors in
(0.1), and their difference is the indispensable quartic Markov move.

For compiler matching there is a second graph.  A channel has two
occurrence cells, one in each incident packet, and two target values, its
distinguished value and its partner.  At either endpoint those two cells
are matched diagonally to the two target values; changing endpoint swaps the
diagonal.  The union of the two endpoint native graphs is therefore one
`K_(2,2)` per channel.  At fixed `q` it is a disjoint union of four such
squares, not the cycle (1.3).  The structural zeros in (1.2) are Markov
state zeros and must not be substituted for the full occurrence/compiler
zeros.

The sets `D_q` are pairwise disjoint: the eight cube triples are distinct
at fixed `q`, and different depths have different target ranks.  The native
interval cells at different depths have different occurrence addresses.
Put

\[
                 D=\biguplus_{q=2}^d D_q,qquad |D|=N.        \tag{1.4}
\]

## 2. Exact certified packet matroid

Let `P` be the `N` occurrence-labelled native cells and let

\[
                      \mu_\epsilon:D\longrightarrow P       \tag{2.1}
\]

be the endpoint-`epsilon` native assignment.  Every assigned target is the
literal OR of the source letters in its cell.  Capping all selected cells by
their current OR leaves the displayed source word itself as a simultaneous
witness, so all edges of `mu_epsilon` coexist in one source-cap state.

### Theorem 2.1 (native restriction is free)

For either endpoint,

\[
                         M_{P,\epsilon}|D=U_{N,N}.             \tag{2.2}
\]

If the declared packet graph contains no incidences from `P` to targets
outside `D`, then on the complete target shore `L`

\[
             M_{P,\epsilon}=U_{N,N}\oplus U_{L-D,0},          \tag{2.3}
\]

whose unique basis is `D`.

#### Proof

The matching (2.1) saturates all `N` elements of `D`.  A matroid on `N`
elements with rank `N` is free, proving (2.2).  Under the additional
structural-zero hypothesis every target outside `D` is a loop, giving
(2.3).  \(\square\)

The source-signature theorem proves (2.2), not the extra hypothesis in
(2.3).  In a complete compiler state a native occurrence may have legal
incidences to exterior targets.  Those incidences can create additional
bases without changing (0.1), (1.2), or the native matching.

### Theorem 2.2 (full addressed transport matroid)

There is a larger exact transport object supplied by the width-graded
four-block identity.  Let `k=(s,t,X)` be a nonzero addressed surplus key:
relative interval start, relative interval end, and literal OR value.  Its
signed four-block contribution has either one positive and one negative
entry, or two positive and two negative entries.  Put `m_k=1` or `2`
accordingly.  Let `T_k` be its `m_k` old-surplus occurrence copies and
`P_k` its `m_k` new-surplus cells.

Pair the forced copies on a sparse row.  On a full row pair blocks `0--1`
and `3--2`, reversing arrows with the sign.  Equal keys have equal address,
width, and value, so the native transport block is `K_(m_k,m_k)`.  Hence

\[
 M_{\rm addr}^{\rm nat}
     =\bigoplus_k U_{m_k,m_k},                            \tag{2.5}
\]

which is a free matroid on the transported occurrence copies.  The sparse
rows use all four edges of the connected block graph

\[
               K_{2,2}\text{ on }\{0,3\}\mid\{1,2\}.       \tag{2.6}
\]

Thus both perfect matchings of that block graph are required.  The paired
widths extend to `6d+15`; this is not a depth-`d` collar-only transport.

If target masks, rather than their occurrence copies, are the compiler
shore, choose one transported occurrence of each distinct mask.  These
identity assignments use distinct cells and coexist in the displayed source
word, so the resulting target restriction is again free.  Formula (2.5)
does not determine incidences to other targets after mandatory-core,
deadline, guard and common-cap filtering.

There is an exact description once those missing incidences are supplied.
Fix `mu=mu_epsilon`.  Form the matching-exchange digraph on targets by
putting an arc `x -> d` whenever target `x` may use the packet cell
`mu(d)`.  For `J subseteq L-D` and `K subseteq D` with `|J|=|K|`,

\[
                  (D-K)\cup J                              \tag{2.4}
\]

is a packet basis if and only if the exchange digraph contains `|J|`
vertex-disjoint directed alternating paths from `J` to `K`, internally
through `D`.  This is the ordinary symmetric-difference characterization
of bases of a transversal matroid.  Hence the precise missing input for the
**full** packet matroid is the occurrence-labelled exterior-to-packet
incidence table, not another coefficientwise action identity.

For example, adjoining an exterior target adjacent to one native cell makes
it parallel, in the appropriate restriction, to that cell's native target;
adjoining targets meeting two cells creates overlapping transversal
circuits.  Thus the full extension need not be a partition matroid even
though its native restriction is free.

## 3. The literal physical obstruction

Let `T^-` use phases `0110` and `T^+` use phases `1001` in the four Klein
relabelled blocks.  The shared audit proves, for every `d>=2`,

\[
\begin{array}{c|c|c|c}
 &\text{occurrences}&\text{distinct values}&
   \text{multiplicity histogram}\\ \hline
\text{central owners}&32d+92&8d+24&2^2,4^{8d+22}\\
\text{lower q1}&32d+88&8d+24&2^4,4^{8d+20}\\
\text{upper q1}&32d+88&16&2^4,4^4,(4d+8)^8.
\end{array}                                                \tag{3.1}
\]

After duplicate edges are suppressed, the physical owner graph has

\[
 8d+40\text{ edges},\qquad \Delta=4,qquad
 2^{8d}3^{16}4^8                                           \tag{3.2}
\]

as its degree histogram.  Both phases have the same owner/lower/upper
occurrence counters, but their physical edge counters differ.  Therefore
counter equality is not a simple factor embedding.

There is a positive pointwise common source cap.  This does not repair
(3.1).  Overlapping consecutive source blocks in exactly `d` letters
creates neither a new nor an identified width-`d+1` owner window.  Even the
largest phase-common overlap collar misses six required owner occurrences
and creates fourteen nonrequired ones in either state; decreasing a common
collar cannot restore a missing owner because owner union is monotone in
every collar letter.

### Proposition 3.1 (uniform private tags cannot repair the relation)

Suppose a uniform tag set `Z_i` is adjoined to every source letter of block
`i`.  The four signed surplus pairings have block graph

\[
                       K_{2,2}.                              \tag{3.3}
\]

For a target from block `i` to cancel literally with its paired target from
block `j`, their tag parts must agree, so `Z_i=Z_j` on every edge of (3.3).
Since (3.3) is connected, all four tag sets are equal.  Such tags do not
separate the repeated owner or palette values.  Pairwise-private uniform
tags separate them but destroy the cancellation equalities.

This proposition rules out only uniform block tags.  A nonliteral quotient
weave, position-dependent tags with additional cancellation, or a different
physical embedding is not excluded.

### Corollary 3.2 (no literal physical endpoint)

If the safe chronology class requires simple middle ownership and a strict
lower-q1 palette, neither `T^-` nor `T^+` belongs to it.  In the notation of
the compiler-boundary quotient,

\[
               \Theta_{\rm phys}(T^-)
                =\Theta_{\rm phys}(T^+)=\varnothing          \tag{3.4}
\]

for the literal four-block embedding.  Its physical boundary signature is
therefore empty.  The formal source-cap state and the native matroid (2.2)
remain valid, but they are not a CBC lift.

## 4. Exact background response after a future physical weave

Assume now, explicitly, that a nonliteral weave or different host has
produced one legal endpoint `T_epsilon`, preserved the native bank `D,P`,
and supplied a complete cap state retaining `mu_epsilon`.  Let

\[
                   R=L-D,qquad B=C-P.                       \tag{4.1}
\]

For a fixed complete state `theta` retaining `mu_epsilon`, contract its
`N` matching edges.  Hall's theorem gives the exact conditional deficiency

\[
\begin{split}
 \delta_{\epsilon,\theta}(T;\mu_\epsilon)
   &=|R|-r_{M_{B,\epsilon}^\theta}(R)\\
   &=\max_{X\subseteq R}
       (|X|-|N_{B,\epsilon}^\theta(X)|)_+.              \tag{4.2}
\end{split}
\]

If `b` is a boundary separator containing every shared cap/guard bit, define

\[
 \rho_{\epsilon,b}
   =\max_{\theta\in\Theta_\epsilon(b):\,
                    \mu_\epsilon\subseteq E_\theta}
       r_{M_{B,\epsilon}^\theta}(R).                         \tag{4.3}
\]

Then the exact native-branch background response record is

\[
             (b,\epsilon,\kappa_{\epsilon,b}(D)),\qquad
 \kappa_{\epsilon,b}(D)=|R|-\rho_{\epsilon,b}.               \tag{4.4}
\]

For terminal optimization duplicate records with the same boundary type may
be suppressed.  For later composition the boundary type or the literal
background--packet compatibility relation must be retained; cap-state edges
may not be unioned.

If exterior-to-packet incidences are allowed and the terminal compiler may
abandon `mu_epsilon`, the complete signature is the vector

\[
                 \bigl(\kappa_{\epsilon,b}(I)\bigr)_{I}       \tag{4.5}
\]

over the linkable packet bases (2.4), not only the entry at `D`.  Formula
(4.4) is exact for the certified native branch; it is an upper bound on the
unrestricted deficiency when extra packet bases exist.

### Corollary 4.1 (bounded-cut endpoint criterion)

A future physical endpoint has native-branch compiler defect at most the
absolute constant `C` if and only if one compatible complete cap state
satisfies

\[
               |N_{B,\epsilon}^\theta(X)|\ge |X|-C
                    \qquad(X\subseteq R).                     \tag{4.6}
\]

Equivalently its residual background matching rank is at least `|R|-C`.
To certify exact defect `C`, exhibit both such a matching and a set `X`
attaining equality in the Hall deficiency.

The four-block relation gives intrinsic packet cut zero by taking `L=D`.
It gives no global bound in (4.6): abstractly, one may attach any number of
background loop targets while leaving the identical source-signature/native
packet data unchanged.  This is a compiler-graph nonimplication, not a
physical Pascal-carrier counterexample.

## 5. Sharp remaining datum for the literal four-copy word

No literal endpoint with a bounded physical rank cut exists, because the
literal endpoints fail before the compiler is reached.  A positive endpoint
now requires exactly the following additional data.

1. **Physical weave.**  An occurrence-labelled nonliteral quotient weave or
   host embedding which removes the multiplicities (3.1), has owner degree
   two and a strict q1 palette, and retains the native `D--P` matching.
2. **Compatible cap state.**  One complete state containing all owner,
   palette, residence, upper-witness, nonzero-source and boundary choices,
   together with `mu_epsilon`.
3. **Residual rank.**  The occurrence-labelled residual `R x B` incidence
   graph, or a matching of size `|R|-C` and the all-cut inequality (4.6).
4. **Optional packet exchanges.**  If the native basis may be abandoned,
   the `R x P` incidences determining the linkable bases (2.4).

The first datum is missing in the literal contiguous four-copy geometry.
Consequently asking which literal phase has the better background rank is
premature: neither literal phase is in the physical state space.  The
quotient fold in Section 7 supplies a different physical geometry and must
not be conflated with those literal endpoints.

## 6. Independent audit

The shared replay was rerun independently without changing its artifact:

```text
python3 scratch/audit_c8_fourblock_physical_owner_palette_nogo_20260801.py
```

It reproduced

```text
PASS_C8_FOURBLOCK_PHYSICAL_OWNER_PALETTE_NOGO
payload_sha256=32fc8da843df199a9383581891d0def9b5cd92a2db185e4b1d66404e913ef50c
```

for `2<=d<=12`, including the all-`d` formulas (3.1)--(3.2), the common-cap
row, and the overlap obstruction.  Frozen files:

```text
scratch/audit_c8_fourblock_physical_owner_palette_nogo_20260801.py
  SHA-256 a64061ea9f573ece51af78a19aa574dc34ea5172efdb917bbba89aadf8cd5d78
scratch/c8_fourblock_physical_owner_palette_nogo_20260801.audit.json
  SHA-256 00424a3bbd4753fae30ce9f4a257e0474d66fc1a5b982e81b24a02f3ac56c0b4
```

The rank-contraction formula was independently audited from the
packet/background matroid-union theorem.  The audit also caught the necessary
boundary-compatibility correction: a terminal rank record may be deduplicated,
but arbitrary later composition must retain its separator label.

## 7. Quotient-folded physical endpoint and exact two-ray packet

The owner-value quotient changes the conclusion.  On the `8d+24` distinct
owners, each phase has exactly sixteen lower-rainbow degree-two selections;
all sixteen are Hamilton cycles, and exactly two per phase cover all sixteen
upper-q1 colours.  Every old/new upper-complete pair has the same upper
multiplicity counter.  Cutting a common edge gives same-endpoint Hamilton
paths.  Every audited cut is depth-`d` resident and has a nonempty exact
maximal inverse.

For every ray-clean paired cut, after the common relabelling used by the
folded audit, the phase-exclusive distinct-value supports are

\[
\begin{aligned}
 \mathcal P_0&=\{K+za_3+F[1,j]:1\le j<d\},&
 \mathcal S_0&=\{K+za_1+F[j,d]:2\le j\le d\},\\
 \mathcal P_1&=\{K+za_1+F[1,j]:1\le j<d\},&
 \mathcal S_1&=\{K+za_3+F[j,d]:2\le j\le d\}.          \tag{7.1}
\end{aligned}
\]

They are two disjoint chains of `d-1` masks per direction.  There are two
cut objectives which must not be conflated.

* The global minimum-signature cut has graded source-counter `L1=6d+4`
  and loses one upper-q1 value.  Its ray witnesses are not at the common
  aligned anchor positions used in (7.3).
* The aligned-base cut has `L1=10d+12`, loses one upper-q1 value, and has
  common anchors at zero-based positions `4d+12` and `5d+12`.
* An upper-safe cut retains all sixteen upper-q1 values and has
  `L1=10d+20`.

Both have the same two ray supports (7.1), and opening either Hamilton cycle
loses one lower-q1 edge colour.  Thus the upper-safe endpoint has one bounded
lower sidecar; the aligned endpoint has one lower and one upper sidecar.
Distinct-target ray repair needs only the `2d-2` masks in (7.1); `L1` is not
a matching-rank certificate.

### 7.1 Exact two-host closure

Put

\[
\begin{array}{ll}
 L_0=K+za_3+f_1,&L_1=K+za_1+f_1,\\
 R_0=K+za_1+f_d,&R_1=K+za_3+f_d,
\end{array}
\]

and

\[
 X_L=L_0\cup L_1,qquad X_R=R_0\cup R_1.               \tag{7.2}
\]

If the ambient source contains the typed rail

\[
                   X_L,f_2,\ldots,f_{d-1},X_R,          \tag{7.3}
\]

refine its ends in phase `epsilon` by

\[
 X_L\mapsto(X_L,L_\epsilon),\qquad
 X_R\mapsto(R_\epsilon,X_R).                            \tag{7.4}
\]

Every old interval has an injective full-block lift.  The right-facing cells
at the left host are exactly `P_epsilon`, and the left-facing cells at the
right host are exactly `S_epsilon`.  Moreover

\[
                       L_0\cup R_0=L_1\cup R_1,          \tag{7.5}
\]

so the unique cell trimming both hosts is phase-common.  There is no hidden
cross-host overshoot.  The pointwise cap word is

\[
             X_L,X_L,f_2,\ldots,f_{d-1},X_R,X_R.         \tag{7.6}
\]

### Theorem 7.1 (two-ray packet matroid and zero local response)

Let

\[
 D_\epsilon=\mathcal P_\epsilon\mathbin{\dot\cup}
             \mathcal S_\epsilon,qquad |D_\epsilon|=2d-2,
\]

and let `P_epsilon` be the `2d-2` side-cell occurrences created by (7.4).
In the complete cap state (7.6),

\[
             M_{P_\epsilon}|D_\epsilon=U_{2d-2,2d-2}. \tag{7.7}
\]

If a reference old matching is transported by the full-block lift and its
edges on `D_epsilon` are released when necessary, then the packet cells
saturate `D_epsilon` and the transported background saturates every other
old target.  Under this explicit background-saturation hypothesis the exact
local compiler-boundary response is

\[
                         \kappa(D_\epsilon)=0.           \tag{7.8}
\]

#### Proof

Equations (7.3)--(7.4) give one distinct interval occurrence for every
member of each ray, hence a diagonal matching of size `2d-2`; this proves
(7.7).  Full-block transport is injective, preserves every old OR value,
and uses no side cell.  Its matching and the diagonal ray matching are
therefore cell-disjoint and jointly legal in (7.6), proving (7.8).
\(\square\)

Thus this is the requested endpoint with bounded rank cut: **conditionally
on actual typed hosts, the local cut is zero, not merely `O(1)`.**

### Corollary 7.2 (best bounded endpoint before host embedding)

Choose an upper-safe folded Hamilton path.  It retains all sixteen upper-q1
colours and has exactly one lower-q1 cut casualty.  Conditional on either
typed host module above and on injective transport of the old background
matching, the two ray banks have rank `2d-2`; consequently the whole
remaining local packet deficiency is at most one.  Reserving one protected
sidecar cell for the cut lower colour enlarges the native free restriction to

\[
                         U_{2d-1,2d-1}                     \tag{7.9}
\]

and makes the local deficiency zero.  By contrast, the aligned-base cut
loses one lower and one upper colour and therefore
needs two sidecars for the same conclusion.  This comparison is local: it
does not assert that the typed host, either sidecar, or the transported
background matching exists in a Pascal child.

### 7.2 Exact remaining socket datum

The quotient-folded maximal inverse does not itself contain `X_L,X_R` at
the required anchor positions.  At zero-based source positions `4d+12` and
`5d+12`, respectively, their values are the unions of the two phase letters,
strictly larger than either legal native maximal-erosion letter.  Enlarging
the native letters is not owner-preserving because maximal erosion is already
the largest antecedent of the fixed owner path.

Hence the remaining theorem is no longer a Hall theorem on the two ray
chains.  It is the following two-socket physical embedding statement.

> Supply two occurrence-labelled old source sockets whose literal values and
> intervening trace are (7.3), such that the refinements (7.4) preserve owner
> rank, Johnson adjacency, the folded lower/upper palettes, residence,
> deadline and all protected witnesses.  For regenerative use, contraction
> of the same two marked blocks must also preserve the ambient protected
> matching.

Once those sockets exist, Theorem 7.1 closes common cap, all distinct ray
targets, cross-host cells and local compiler Hall automatically.  For a
single terminal use, the only remaining background response is the ambient
matching transported outside the prepared rail.  For serial regeneration,
retain its boundary separator and contraction rank as in Proposition 3.3 of
the compiler-boundary quotient.

### 7.3 One-host nonflat alternative

There is a sharper source interface if one one-step deadline jump is allowed.
Put

\[
 X=K+za_1a_3,qquad
 (Z^0,T^0)=(K+za_3,K+za_1),qquad
 (Z^1,T^1)=(T^0,Z^0).                                  \tag{7.10}
\]

Between decreasing left and right filler rails, replace the one source
letter `X` by `Z^epsilon,T^epsilon`.  The left intervals ending at
`Z^epsilon` and right intervals beginning at `T^epsilon` are exactly the two
rays (7.1), every such witness has width at most `d`, every old interval has
an equal-OR full-block lift, and `X` is one exact phase-common cap.  Hence
the packet matroid is again (7.7) and the conditional local response is
again zero.

This cannot be an internal flat depth-`d` split.  The `d` new natural owner
windows containing both halves lie in intersections of consecutive old
rank-`r` Johnson owners and therefore have rank at most `r-1`.  The old
owner cells crossing the split survive at width `d+2`, so this is a
cost-one **nonflat/one-deadline-jump** packet.  It is the smaller additive
interface, but it still requires one legal typed host occurrence and a
halo/global-erosion theorem.  Same owner endpoints alone do not supply the
needed `d`-letter source halos.

### 7.4 Exact terminal birail Hall closure

For two threshold multisets `x_1,...,x_N` and `y_1,...,y_N`, write

\[
 C_\pi(a,c)=\#\{i:x_i\le a,\ y_{\pi(i)}\le c\},
 \qquad
 \delta(\pi)=\max_{a,c}(C_\pi(a,c)-a-c)_+ .           \tag{7.11}
\]

If `L(a)=#{i:x_i<=a}`, `R(c)=#{j:y_j<=c}` and

\[
 E_L=\max_a(L(a)-a),\qquad E_R=\max_c(R(c)-c),          \tag{7.12}
\]

the antitone-birail theorem proves

\[
                    \min_\pi\delta(\pi)
                    =(E_L+E_R-N)_+.                    \tag{7.13}
\]

For the folded ray bank the two marginal multisets are both

\[
                  \{0^{d-1},1,2,\ldots,d-1\}.          \tag{7.14}
\]

Hence `N=2d-2` and `E_L=E_R=d-1`, so the abstract terminal optimum is
exactly zero.  Equivalently, the prefix/suffix exchange has the correct
comparator shape: the endpoint labels `a_1,a_3` are interchanged between
the same two nested chains.

This conclusion applies only after an owner-legal host atlas exposes the
two-prefix lists (7.14) inside one matching-closed cap state and permits the
required endpoint pairing.  It does not follow merely from the set supports
(7.1).  Under those hypotheses, however, the ray Hall problem is closed;
there is no hidden positive rank cut beyond the palette sidecars in
Corollary 7.2.

### 7.5 Support closure is not graded regenerative closure

Let `S_0,S_1` be the canonical aligned folded source paths and `G_0,G_1`
the opposite two-host ray words.  The independent contextual audit proves

\[
\begin{aligned}
 \|D(S_0)-D(S_1)\|_1&=10d+12,\\
 \|D(G_0)-D(G_1)\|_1&=4d-4,\\
 \|D(S_0)+D(G_1)-D(S_1)-D(G_0)\|_1&=6d+16.            \tag{7.15}
\end{aligned}
\]

The last residue has one positive and one negative entry at every width
`2d+5,...,5d+12`.  Common exterior screens equalize the crossing prefix and
suffix chains but do not change (7.15).  Therefore the two-host theorem is
an exact distinct-target/common-cap and terminal-matching theorem, not an
exact graded source relation in arbitrary context.

This sharply separates the two surviving gates:

1. for a single terminal endpoint, plant the typed host(s), the one palette
   sidecar, and one compatible background matching; then (7.13) gives zero
   terminal ray deficiency;
2. for serial regeneration, additionally cancel (7.15), or prove that its
   addressed cells are transported and recycled without accumulating
   charge.

## 8. Single-cut boundary rail: exact positive source row and owner no-go

The aligned host addresses differ by `d`, but this does not permit two
independent internal full-window hosts.  A minimal host `X` of size
`r-d+1` is seen by `d+1` rank-`r` owners; after deleting `X`, those owners
form a length-`d` walk on `(d-1)`-sets.  Its `d` arrival runs cannot all
survive to a final set of size `d-1`, so one positive run is strictly
internal and has length at most `d-1`.  For hosts at `p_L,p_R=p_L+d`, the
two sets of affected transition edges are disjoint.  One cut therefore
cannot make both independent full hosts resident.

The surviving architecture is a genuinely clipped rail: open the owner
cycle first, put `X_L,L_epsilon` at one source boundary and
`R_epsilon,X_R` at the other, and solve the boundary reconstruction equations
rather than retaining both internal `d+1`-window families.  Under those
equations, the run criterion, the palette-survival ledger and one compatible
background matching, the ray matroid and zero terminal Hall conclusions of
Section 7 apply verbatim.

There is now exact positive evidence for the source-language half.  For the
canonical aligned folded words `S_0,S_1` and opposite host words `G_0,G_1`,
a common cyclic cut one letter into `S` gives

\[
        D_{\rm graded}(\rho(S_0G_1))
        =D_{\rm graded}(\rho(S_1G_0))                  \tag{8.1}
\]

for every audited `2<=d<=12`; the reverse block order has the same cut at
position `d+3`.  Before screening, suffix signatures agree and exactly
`3d+8` prefix entries differ.  Prepending either common screen
`{a_1,a_3}` or `{z,a_1,a_3}` preserves (8.1) and makes both boundary
signatures equal.  Hence the screened words have identical width-graded OR
decks in every fixed exterior context.  This is value/width equality, not
addressed start/end equality; protected occurrences still require the
matching transport of Section 4.  The replay prepends one actual screen
cell, so its certified charge is `+1` unless an existing boundary collar is
proved to carry that screen.

Thus the earlier regenerative residue is not an invariant: the global cut
and one common screen cancel it exactly on the audited family.  The precise
remaining datum is now an owner-legal clipped realization of that screened
source word, its q1 sidecar ledger, and a matching-closed common-cap
background state.  No all-`d` extrapolation or Pascal-child embedding is
claimed.

The folded audit was independently replayed.  The final frozen payload
distinguishes the aligned and upper-safe cuts described above and reports

```text
PASS_C8_FOLDED_HAMILTON_TWO_RAY_LIFT
payload_sha256=785e2e0e23f87e3840e243f5a4927f6f5f34e57a4c30b205578d7eaad29f946d
```

with the frozen script hash recorded in the handoff.
The exact two-host closure is proved independently in
`MATH_THEOREM_AD_OCTAGON_FOLDED_TWO_RAY_TWOHOST_CLOSURE_20260801.md`; the
one-host deadline theorem is
`MATH_THEOREM_AD_QUOTIENT_FOLD_TWO_RAY_COMMON_HOST_AND_DEADLINE_GATE_20260801.md`.
The single-cut owner obstruction and clipped endpoint interface are in
`MATH_THEOREM_R_FOLDED_C8_BOUNDARY_RAIL_HOST_LINK_AND_SINGLE_CUT_GATE_20260801.md`.
The complete compiler/source synthesis is
`MATH_THEOREM_R_FOLDED_C8_SINGLE_CUT_BOUNDARY_RAIL_CLOSURE_AND_EXACT_GATES_20260801.md`.
