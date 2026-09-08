# Lane W: quotient-cycle phase fusion after the failure of sparse residence

Date: 2026-07-25

Method: pure mathematics only.  No web search, computation, finite search,
solver, or long-running job is used.

## 0. Verdict

Put

\[
 N=2m+1,\qquad B=\operatorname {Cat}_m,\qquad W=NB,
 \qquad H=\lceil A\sqrt m\rceil
\]

for fixed \(A>0\).  This report takes as updated input the asserted exact
counterexample to the sparse residence statement \((RP_A)\).  It does not
reprove that counterexample.  In particular, nothing below uses the false
implication

\[
 d(D)=1\Longrightarrow
 \text{a return at }2\operatorname {ht}(D)+1.
\]

Every zero-return packet used below is assumed to be an actual first
zero-winding PBBS return.  The broader rainbow lemma is stated only for an
actual owner segment whose omitted labels are explicitly pairwise
distinct.  The scalar equality \(d(D)=1\) is used only at an initial
return edge, where it gives the exact phase rotor \(u\mapsto u-1\).

The attack produces five exact results.

1.  Every rainbow PBBS segment of step-two length \(s<m\), hence every
    genuine zero-winding packet, has a **two-core circular portal word** of
    length

    \[
       \boxed{2s+3}.                                      \tag{0.1}
    \]

    It realizes every intersection and every union of consecutive owners
    on both projected parities inside the packet, including all its
    \(2s+2\) middle owners.  An ordinary linear word is obtained by
    duplicating one ordered port of length \(s-1\), and therefore has

    \[
       \boxed{3s+2}                                      \tag{0.2}
    \]

    letters.  Thus the order-\(s\) packet toll is exactly a cycle-opening
    toll, not an internal target-count toll.

2.  If the outgoing ordered port of one packet equals, up to one ground
    rotation, the incoming port of the next, all \(N\) phase lifts splice
    by one exact phase permutation.  For \(r\) equal-height packets in
    \(c\) port-compatible lifted chains, their internal packet targets have
    one literal word of length

    \[
       \boxed{r(2s+3)+c(s-1)}.                     \tag{0.3}
    \]

    Relative to the \(r(2s+2)\) packet-owner positions, the excess is

    \[
       \boxed{r+c(s-1)}.                            \tag{0.4}
    \]

    More strongly, grouping quotient packets by their normalized ordered
    port gives fewer than \(2N^{H-1}=\exp(o(m))\) lifted chains for
    **every** height-at-most-\(H\) packet family.  Hence a Gaussian packet
    assignment with \(r=O(W/H)\) has packet-internal excess

    \[
       O(W/H)+2HN^{H-1}=o(W).                      \tag{0.5}
    \]

    This is an unconditional ordered-port compiler for any *given*
    Gaussian packet assignment, with every phase lift integral.  It does
    not preserve original packet adjacency and therefore does not yet
    cover crossing windows.  If one insists on a prescribed projected
    port graph, its lifted count is instead
    \(NP+\sum_i\gcd(N,\sigma_i)\); monodromy alone gives no small bound.
    For a physical internally edge-simple, pairwise edge-disjoint residence
    packing, shared endpoints cost at most one extra baseline charge per
    packet, so all middle owners and all packet-internal targets already
    have total length \(W+o(W)\).

3.  A separate appended chart cannot be the fusion mechanism.  At a
    rotationally rigid cut, one fixed depth \(q\) already gives \(Nq\)
    distinct equal-rank targets over the \(N\) phase lifts.  Endpoint
    injectivity forces every standalone literal chart to have at least

    \[
       \boxed{Nq}                                      \tag{0.6}
    \]

    positions.  The exceptional non-rigid target set has size at most

    \[
       (N-1)2^{N/3}\sum_{j=0}^{2H}\binom Nj
       =2^{N/3+o_A(N)},                              \tag{0.7}
    \]

    and is negligible against a Catalan-scale occurrence family even after
    the audited PBBS occurrence cap \(\binom{2q+1}{q}\).  Thus phase-deck
    fusion must recode the existing \(\Theta(NH)\) packet positions; it
    cannot append an \(O(N+H)\) universal seam.

    This obstruction is explicit at Gaussian residence.  For
    \(D_0=1^s0^{s-1}(10)^L0\), every
    \(2\le q\le\lfloor(s+1)/2\rfloor\) produces exactly \(Nq\) distinct
    phase-deck targets, and taking \(m=cs^2\) places it below any prescribed
    \(A\sqrt m\) cutoff after choosing \(c>A^{-2}\).  Moreover, its
    canonical ordered-port overlap graph on the \(N\) phases has only
    self-loops, so that particular opening architecture pays exactly
    \(N(s-1)\) duplicated letters.  This remains an absolute, not additive,
    lower bound against arbitrary in-place recoding.

4.  There is an exact long-block reduction which no longer mentions
    residence packing.  If blocks of quotient length

    \[
       H\ll b,\qquad b\log N=o(m)                  \tag{0.8}
    \]

    admit baseline-relative deck compilers of length

    \[
       N\ell+\eta_mN\ell+C_ANH,\qquad \eta_m=o(1), \tag{0.9}
    \]

    covering all depth-\(H\) targets assigned to the block, including its
    crossing collars, then the complete central word has length

    \[
       W+O(\eta_mW)+O_A(WH/b)+o(W)=W+o(W).          \tag{0.10}
    \]

5.  The corrected zero-endpoint-overlap sector \(\Lambda=0\) can in fact
    be paid independently, with no port matching at all.  If \(e_{m,s}\)
    counts its quotient starts of step-two length \(s\), then

    \[
       \boxed{e_{m,s}\le C_*{4^m\over s^6}}         \tag{0.11}
    \]

    for an absolute \(C_*\).  A killed-path kernel sharpening gives,
    uniformly in every cutoff,

    \[
    \begin{aligned}
       \sum_{s<H}e_{m,s}
       &=O\!\left({4^m\over m^{5/2}}\right),\\
       \sum_{s<H}(3s+2)e_{m,s}
       &=O\!\left({4^m\over m^2}\right).
    \end{aligned}                                  \tag{0.12}
    \]

    Hence all \(N\) phase lifts of every Gaussian \(\Lambda=0\) packet,
    with arbitrary overlap, cost

    \[
       O_A\!\left({W\over\sqrt m}\right)=o_A(W)   \tag{0.13}
    \]

    even after safe dominance-seam collars.  Thus, irrespective of where
    the literal counterexample to \((RP_A)\) lies, the \(\Lambda=0\)
    chamber cannot obstruct coefficient-one fusion.  Any surviving fusion
    obstruction must lie in positive endpoint overlap or another return
    class.

For the remaining dense sector, normalized port matching is no longer the
gate: Theorem 4.5 supplies it by subexponential type grouping.  The
decisive unresolved statement is a **crossing-border, baseline-relative
theorem**.  The reordered packet word must still represent every
support-essential target whose original owner window crosses a packet
boundary, or a larger in-place block chart must absorb those windows at
\(o(W)\) excess.  The exact double-zero equations exchange scalar side
lengths but do not supply that baseline reuse.  Precisely, an
edge-disjoint Gaussian rainbow cover closes the lane if the distinct
target support left outside its packet interiors is \(o(W)\) (Theorem
7.1).  Constant one is not claimed here.

## 1. The exact \(d=1\) phase rotor and its scope

For a normalized Dyck root

\[
 D=P1R0S
\]

at its canonical first maximum, put

\[
 d(D)=|S|+1,
 \qquad \tau=\phi^2.
\]

The even-time PBBS skew product is

\[
 (u,D)\longmapsto (u-d(D),\tau D)\pmod N.          \tag{1.1}
\]

### Lemma 1.1 -- unit-deficit deck rotor

If \(d(D)=1\), then the complete lift of the quotient edge
\(D\to\tau D\) is the perfect matching

\[
 \boxed{u\longmapsto u-1\qquad(u\in\mathbb Z_N).} \tag{1.2}
\]

It is integral and uses every physical edge in the fibre exactly once.

#### Proof

Substitute \(d(D)=1\) in (1.1).  Translation by \(-1\) is a permutation
of \(\mathbb Z_N\), so the \(N\) lifted edges are disjoint and exhaust the
edge fibre. \(\square\)

This is the only automatic consequence of \(d(D)=1\) used below.  It does
not say that \(d(\tau D)=1\), that a zero return occurs, or that two packet
ports have the same physical labels.  Those conclusions require the full
canonical orbit.

## 2. Rainbow PBBS segments have two fixed-core owner rows

Consider \(2s+2\) consecutive physical middle owners
\(A_0,\ldots,A_{2s+1}\) in one exact PBBS factor, where

\[
 1\le s<m.                                         \tag{2.1}
\]

and write the successive omitted labels as

\[
 a_j=\lambda_{2j}\quad(0\le j\le s),
 \qquad
 b_j=\lambda_{2j+1}\quad(0\le j<s).               \tag{2.2}
\]

Assume first that these \(2s+1\) labels are pairwise distinct; call such a
segment rainbow.  Put them in the cyclic active order

\[
 \Gamma=(\gamma_0,\ldots,\gamma_{2s})
       =(b_0,\ldots,b_{s-1},a_0,\ldots,a_s).       \tag{2.3}
\]

Let \(V_j\) be the cyclic \(s\)-window of \(\Gamma\) starting at \(j\).

### Lemma 2.1 -- rainbow fixed-core theorem

There are disjoint cores \(K,K'\), each of size \(m-s\), such that the
two projected parity rows are

\[
 E_j=K\cup V_j\qquad(0\le j\le s),                \tag{2.4}
\]

and

\[
 O_j=K'\cup W_j\qquad(0\le j\le s),               \tag{2.5}
\]

where

\[
 W_j=V_{s+1+j}\quad(0\le j<s),
 \qquad W_s=V_0.                                  \tag{2.6}
\]

Thus (2.4)--(2.5) are precisely the \(2s+2\) middle owners
\(A_0,A_1,\ldots,A_{2s+1}\), separated into their two projected parity
orders.

#### Proof

The exact owner recurrence is

\[
 A_{t+2}=A_t-\{\lambda_{t+1}\}+\{\lambda_t\},
                                                               \tag{2.7}
\]

and consecutive owners satisfy
\[
 A_t\mathbin{\dot\cup}A_{t+1}
 \mathbin{\dot\cup}\{\lambda_t\}=[N].             \tag{2.8}
\]

The valid update from \(A_{2j}\) to \(A_{2j+2}\) removes \(b_j\), so
\(b_j\in A_{2j}\); all earlier even updates involve only the other
distinct \(a_i,b_i\), hence \(b_j\in A_0\).  Equation (2.8) gives
\(a_j\notin A_{2j}\) for every \(0\le j\le s\), including the endpoint
\(a_s=\lambda_{2s}\).  Again, the earlier even updates do not touch
\(a_j\), so \(a_j\notin A_0\).  Define

\[
 K=A_0\setminus\{b_0,\ldots,b_{s-1}\}.
\]

Then

\[
 A_0=K\cup\{b_0,\ldots,b_{s-1}\},
 \qquad |K|=m-s.                                  \tag{2.9}
\]

Iterating (2.7) gives

\[
 A_{2j}
 =K\cup\{a_0,\ldots,a_{j-1}\}
       \cup\{b_j,\ldots,b_{s-1}\}
 =K\cup V_j.                                      \tag{2.10}
\]

The inactive complement of the active labels has size \(2(m-s)\).  Define

\[
 K'=([N]\setminus\{\gamma_0,\ldots,\gamma_{2s}\})\setminus K.
\]

Thus it is partitioned as \(K\mathbin{\dot\cup}K'\), with
\(|K'|=m-s\).  Equation (2.8) and
complementing (2.10) across the omitted label \(a_j\) gives

\[
 A_{2j+1}
 =K'\cup\{b_0,\ldots,b_{j-1}\}
        \cup\{a_{j+1},\ldots,a_s\}
 =K'\cup W_j.                                     \tag{2.11}
\]

This is (2.4)--(2.6). \(\square\)

Every genuine first zero-winding return of odd gap \(2s+1\) is an instance
of Lemma 2.1, because the exact simple-return theorem makes its omitted
labels rainbow.  Conversely, the lemma does not assert a return: it uses
only actual owner chronology and pairwise label distinctness.  In
particular nothing here is inferred from \(d(D)=1\) alone.

## 3. The two-core circular portal compiler

For a coordinate \(x\), write simply \(x\) for the singleton set-letter
\(\{x\}\).  Define three descending singleton blocks

\[
\begin{aligned}
 \mathcal A&=(\gamma_{2s-1},\gamma_{2s-2},\ldots,\gamma_s),\\
 \mathcal B&=(\gamma_{s-1},\gamma_{s-2},\ldots,\gamma_0),\\
 \mathcal C&=(\gamma_{2s},\gamma_{2s-1},\ldots,\gamma_{s+1}).
\end{aligned}                                      \tag{3.1}
\]

Each block has length \(s\).  Consider the ordinary word

\[
 \boxed{
 \mathcal L(\Gamma;K,K')
 =\mathcal A,\ K,\ \mathcal B,\ K',\ \mathcal C.}
                                                        \tag{3.2}
\]

Its length is \(3s+2\).  All letters are nonzero: singleton letters are
nonzero, and \(|K|=|K'|=m-s\ge1\).

### Theorem 3.1 -- exact two-core packet word

The word (3.2) realizes as contiguous ORs

\[
 \bigcap_{j=p}^{q}E_j,\quad
 \bigcup_{j=p}^{q}E_j,
 \qquad 0\le p\le q\le s,                         \tag{3.3}
\]

and

\[
 \bigcap_{j=p}^{q}O_j,\quad
 \bigcup_{j=p}^{q}O_j,
 \qquad 0\le p\le q\le s.                        \tag{3.4}
\]

In particular every one of the \(2s+2\) middle owners is represented.

#### Proof for the \(K\)-row

For \(0\le p\le q\le s\), ordinary cyclic-window arithmetic, with no
wrap in the displayed range, gives

\[
 \bigcap_{j=p}^{q}E_j
 =K\cup\{\gamma_q,\gamma_{q+1},\ldots,
                 \gamma_{p+s-1}\},                \tag{3.5}
\]

where the active interval is empty when \((p,q)=(0,s)\), and

\[
 \bigcup_{j=p}^{q}E_j
 =K\cup\{\gamma_p,\gamma_{p+1},\ldots,
                 \gamma_{q+s-1}\}.                \tag{3.6}
\]

The portion \(\mathcal A,K,\mathcal B\) of (3.2) is

\[
 \gamma_{2s-1},\ldots,\gamma_s, K,
 \gamma_{s-1},\ldots,\gamma_0.                   \tag{3.7}
\]

If the active interval in (3.5) is nonempty, the subword beginning at
\(\gamma_{p+s-1}\) on the left of \(K\), when \(p>0\), and ending at
\(\gamma_q\) on the right of \(K\), when \(q<s\), has OR exactly (3.5).
An absent left or right active part means that the corresponding endpoint
is \(K\).  When the active part is empty, the one-letter interval \(K\)
works.  The same argument with endpoints
\(\gamma_{q+s-1}\) and \(\gamma_p\) proves (3.6).

#### Proof for the \(K'\)-row

For \(0\le j\le s\), formula (2.6) is equivalently

\[
 W_j=
 \{\gamma_{s+1+j},\ldots,\gamma_{2s}\}
 \cup
 \{\gamma_0,\ldots,\gamma_{j-1}\},               \tag{3.8}
\]

with empty ranges omitted.  Hence

\[
\begin{aligned}
 \bigcap_{j=p}^{q}O_j
 &=K'\cup
   \{\gamma_0,\ldots,\gamma_{p-1}\}
   \cup
   \{\gamma_{s+1+q},\ldots,\gamma_{2s}\},\\
 \bigcup_{j=p}^{q}O_j
 &=K'\cup
   \{\gamma_0,\ldots,\gamma_{q-1}\}
   \cup
   \{\gamma_{s+1+p},\ldots,\gamma_{2s}\}.
\end{aligned}                                      \tag{3.9}
\]

The portion \(\mathcal B,K',\mathcal C\) of (3.2) is

\[
 \gamma_{s-1},\ldots,\gamma_0, K',
 \gamma_{2s},\ldots,\gamma_{s+1}.                 \tag{3.10}
\]

The first line of (3.9) is the OR of the interval from
\(\gamma_{p-1}\), or \(K'\) if \(p=0\), through \(K'\), to
\(\gamma_{s+1+q}\), or \(K'\) if \(q=s\).  The second line uses
\(\gamma_{q-1}\) and \(\gamma_{s+1+p}\).  This proves (3.4), and taking
\(p=q\) in the two rows proves the middle-owner assertion. \(\square\)

### Corollary 3.2 -- the circular toll is one

Put

\[
 \mathcal P=(\gamma_{2s-1},\ldots,\gamma_{s+1}),  \tag{3.11}
\]

an ordered port of length \(s-1\).  The cyclic word

\[
 \boxed{
 \mathcal Z(\Gamma;K,K')
 =\mathcal P,\gamma_s,K,\mathcal B,K',\gamma_{2s}}
                                                        \tag{3.12}
\]

has length \(2s+3\) and cyclically realizes all targets in
(3.3)--(3.4).  The linear word (3.2) is obtained by appending one further
copy of \(\mathcal P\) to (3.12).  Therefore the linearization toll is
exactly \(s-1\) for this construction.

#### Proof

The \(K\)-row witnesses lie in the nonwrapping arc
\(\mathcal P,\gamma_s,K,\mathcal B\).  The \(K'\)-row witnesses lie in
the cyclic arc \(\mathcal B,K',\gamma_{2s},\mathcal P\).  Appending
\(\mathcal P\) turns the latter cyclic intervals into ordinary intervals
and gives (3.2). \(\square\)

This corollary is the local fusion primitive.  The packet contains
\(2s+2\) original middle positions.  Its complete circular chart uses only
one additional position.  The whole order-\(s\) loss in (0.2) is the
opening of the one ordered port (3.11).

## 4. Exact port splicing and all \(N\) phase lifts

Two height-\(s\) packets \(P,Q\) are **port compatible** when their
ordered ports satisfy

\[
 \mathcal P(Q)=\rho^c\mathcal P(P)                \tag{4.1}
\]

letter by letter for some \(c\in\mathbb Z_N\), where \(\rho\) is cyclic
ground-coordinate rotation.  The offset \(c\) is unique as soon as the
port is nonempty, because equality of the first singleton determines it.

### Theorem 4.1 -- deckwise port splice

Suppose \(P,Q\) are port compatible with offset \(c\).  Then, for every
phase \(u\), the circular word of the phase-\(u\) lift of \(P\) may be
followed by the circular word of the phase-\((u-c)\) lift of \(Q\), and
the initial copy of \(\mathcal P(Q)\) supplies the missing terminal port
of \(P\).  The matching

\[
 \boxed{u\longmapsto u-c}                          \tag{4.2}
\]

is a permutation of all \(N\) phases.  No fractional owner assignment or
common-owner synchronization is used.

#### Proof

The terminal wrapping witnesses of \(\rho^u\mathcal Z(P)\) require the
ordered singleton string \(\rho^u\mathcal P(P)\).  By (4.1),

\[
 \rho^{u-c}\mathcal P(Q)
 =\rho^{u-c}\rho^c\mathcal P(P)
 =\rho^u\mathcal P(P).                             \tag{4.3}
\]

Thus the initial port of the indicated lift of \(Q\) is literally the
required terminal port of the lift of \(P\).  Translation by \(-c\) is a
bijection of \(\mathbb Z_N\), proving the deck statement.  All letters
are actual nonzero subsets, so the splice is a direct integral literal
construction. \(\square\)

### Corollary 4.2 -- exact chain ledger

Let \(r\) height-\(s\) packets be partitioned into \(c\) directed
port-compatible chains.  Then all their internal two-parity targets have
one ordinary word of length

\[
 \boxed{r(2s+3)+c(s-1)}.                           \tag{4.4}
\]

Relative to the \(r(2s+2)\) owner positions, the excess is

\[
 \boxed{r+c(s-1)}.                                 \tag{4.5}
\]

#### Proof

Use one unduplicated circular list (3.12) for every packet.  At every
internal chain edge, Theorem 4.1 makes the next packet's initial port serve
as the preceding packet's terminal port.  Only the terminal packet of each
chain needs an appended copy of its \((s-1)\)-letter port.  This gives
(4.4); subtracting \(r(2s+2)\) gives (4.5). \(\square\)

If Gaussian packets of heights in \([\alpha H,H]\), \(\alpha>0\), tile a
physical owner set of mass at most \(W\), then

\[
 r\le {W\over 2\alpha H}.                          \tag{4.6}
\]

Lifted monodromy does **not** by itself bound the number of port
components by the number of projected components.  More precisely, suppose
the projected port graph consists of \(P\) directed paths and directed
cycles \(C_i\).  If the edge offsets on \(C_i\) have total voltage

\[
 \sigma_i=\sum_{e\in C_i}c_e\pmod N,
\]

then its \(N\)-phase lift has exactly
\(\gcd(N,\sigma_i)\) cycles, with
\(\gcd(N,0):=N\), while every projected path lifts to \(N\) paths.
Therefore the exact lifted component count is

\[
 \boxed{c_{\rm lift}=NP+\sum_i\gcd(N,\sigma_i).}  \tag{4.7}
\]

Indeed, going once around \(C_i\) sends phase \(u\) to
\(u-\sigma_i\), whose translation permutation has
\(\gcd(N,\sigma_i)\) orbits.  The path statement follows because its
initial phase is never identified with another initial phase.

Consequently one must **assume or prove**, rather than infer from
monodromy, that

\[
 c_{\rm lift}=O(B)+o(W/H).                        \tag{4.7a}
\]

Under (4.7a), equations (4.5)--(4.6) give

\[
 r+c_{\rm lift}H
 =O(W/H+HB)+o(W)=o(W),                            \tag{4.7b}
\]

because \(H\to\infty\) and \(H/N\to0\).  This is the exact accounting for
a prescribed compatible graph.  Theorem 4.5 below removes (4.7a) by
choosing its own type paths and proves the stronger bound (0.5).

### Scope of Corollary 4.2

Corollary 4.2 covers every target whose original projected-owner window is
contained in one packet row.  It does not automatically cover a target
whose owner window crosses from one packet to the next.  A global theorem
must either prove that the port splice represents those cross-packet
windows as well, or add an in-place collar chart for them.  This is one of
the two explicit remaining clauses in \(\operatorname{CBF}_A\), stated in
Section 7.

### Theorem 4.3 -- affine iff for collapsing all translated ambient wreaths

The port splice above is a direct literal splice.  It must not be confused
with the stronger assertion that the \(N\) ground translates of one
ambient wreath completion are one and the same wreath cycle.

Let \(z=(z_t)_{t\in\mathbb Z_N}\) be the omitted-label permutation of an
ambient \((N,m)\)-wreath, and let

\[
 W_t=\{z_{t+1},z_{t+3},\ldots,z_{t+2m-1}\}.       \tag{4.8}
\]

Then ground translation \(x\mapsto x+1\) preserves the owner cycle
\(\{W_t\}\) if and only if

\[
 \boxed{z_t=\alpha+\beta t\pmod N}                \tag{4.9}
\]

for some \(\alpha\) and some unit \(\beta\in\mathbb Z_N^\times\).

#### Proof

The disjointness graph induced on the \(N\) owners of one wreath is the
cycle \(C_N\).  Ground translation acts on this graph by an automorphism.
The automorphism group is dihedral.  Because ground translation has odd
order \(N\), its action cannot be a reflection; it is a rotation
\(t\mapsto t+h\).

The unique coordinate omitted by the edge \(W_tW_{t+1}\) is \(z_t\).
Translation sends it to \(z_t+1\), while the rotated edge omits
\(z_{t+h}\).  Hence

\[
 z_{t+h}=z_t+1.                                    \tag{4.10}
\]

The orbit on the right has length \(N\), so \(h\) is a unit.  Writing
\(\beta=h^{-1}\), iteration of (4.10) gives (4.9).  Conversely, (4.9)
makes translation by one identical to owner-index rotation by
\(h=\beta^{-1}\), so the translated wreath is the same cycle. \(\square\)

For a genuine zero-return completion, the active anchors satisfy

\[
 z_{2j}=a_j,\qquad z_{2j+1}=b_j.                  \tag{4.11}
\]

Since \(a_1=a_0-1\), an affine completion must have

\[
 2\beta=-1\pmod N,\qquad \beta=m,                 \tag{4.12}
\]

and therefore

\[
 \boxed{a_j=a_0-j,\qquad b_j=a_0+m-j.}            \tag{4.13}
\]

In particular its initial first-maximum displacement is \(m\).  Thus the
scalar unit rotor does not make the \(N\) translated ambient completions
one wreath except in this affine class.  Theorem 4.1 remains valid outside
the affine class only when the shorter ordered-port equality (4.1) is
verified directly between the two actual packets.

### Corollary 4.4 -- exact affine interval compiler

In the affine class, the complement-Johnson owners are the \(N\) cyclic
coordinate intervals of length \(m+1\).  The singleton word consisting of
one full coordinate period followed by its first \(m+H\) symbols has

\[
 \boxed{N+m+H}                                     \tag{4.14}
\]

letters and represents every intersection and every union of at most
\(H+1\) consecutive owners, as well as all \(N\) middle owners.

#### Proof

An intersection of \(q+1\) consecutive length-\((m+1)\) cyclic intervals
is a cyclic coordinate interval of length \(m+1-q\); their union is one
of length \(m+1+q\).  For \(0\le q\le H\), all such intervals have length
at most \(m+1+H\).  One period followed by \(m+H\) repeated singleton
letters linearizes every one of them. \(\square\)

This is an unconditional nontrivial phase-deck compiler, but its additive
cost is \(m+H=\Theta(N)\) per affine deck.  It is not by itself a
coefficient-one theorem for a positive-density family.

For distinct spatial lifts \(u\ne v\) of one nonperiodic ordered port,
the canonical openings are \(\rho^u\mathcal P\) and
\(\rho^v\mathcal P\), and they are unequal: equality of their first
singleton would force \(u=v\).  Thus Theorem 4.1 does not chain the
different phases of one packet to each other.  It chains a phase of one
packet to a possibly different phase of a different packet only after the
quotient-level translated-string identity (4.1) has been proved.

That identity can nevertheless be forced for an arbitrary large packet
family by grouping normalized port types.  No natural quotient adjacency
or cycle voltage is needed.

### Theorem 4.5 -- subexponential normalized-port clustering

Assume \(1\le H<m\).  Let \(\mathscr P\) be any finite multiset of
rainbow quotient-packet occurrences as in Lemma 2.1 (in particular,
genuine zero-winding packets) in one exact PBBS factor, each of height
\(1\le s(P)\le H\), and include the complete deck of all \(N\) physical
phase lifts of every occurrence.  For \(s(P)\ge2\), write

\[
 \mathcal P(P)=(p_1,\ldots,p_{s(P)-1})
\]

and define its normalized port type by

\[
 \operatorname{type}(P)
 =\bigl(s(P),p_2-p_1,\ldots,p_{s(P)-1}-p_1\bigr)
 \in\{s(P)\}\times\mathbb Z_N^{\,s(P)-2}.         \tag{4.15}
\]

Let \(q_s\) be the number of height-\(s\) quotient occurrences and \(T_s\)
the number of occupied normalized types at height \(s\).  Put

\[
 R=N\sum_{s=1}^{H}q_s,\qquad
 M=N\sum_{s=1}^{H}q_s(2s+2).                     \tag{4.16}
\]

Here \(R\) is the number of physical packets and \(M\) counts their
charged owner occurrences with multiplicity.  Packets of height one have
empty ports and need no opening letters.  There is a partition of all
other physical packet lifts into at most

\[
 \boxed{
 c_{\rm type}=N\sum_{s=2}^{H}T_s
 \le N\sum_{s=2}^{H}(N-1)_{s-2}
 \le N\sum_{s=2}^{H}N^{s-2}
 =N\,{N^{H-1}-1\over N-1}
 <2N^{H-1}}                                      \tag{4.17}
\]

literal port-compatible chains.  All packet-internal two-parity targets
and all packet owners have a literal word of constructed length exactly

\[
 \boxed{
 L_{\rm int}
 =M+R+N\sum_{s=2}^{H}T_s(s-1).}                 \tag{4.18}
\]

In particular,

\[
 \boxed{
 L_{\rm int}-M
 <R+2HN^{H-1}.}                                   \tag{4.19}
\]

In particular, suppose the assigned physical packet-owner positions are
disjoint, so \(M\le W\), and

\[
 \alpha H\le s(P)\le H                            \tag{4.20}
\]

for one fixed \(\alpha>0\).  If
\(H=O_A(\sqrt m)\), then

\[
 \boxed{
 L_{\rm int}-M
 \le {W\over2\alpha H+2}+2HN^{H-1}
 =o_A(W).}                                        \tag{4.21}
\]

Appending the \(W-M\) uncharged middle owners as single letters therefore
gives a word of length \(W+o_A(W)\) covering every middle owner and every
packet-internal target.

#### Proof

Two packets of the same normalized type have ports differing by one
literal translation: if their first port labels are \(p_1,p'_1\), then

\[
 \mathcal P(P')=\rho^{p'_1-p_1}\mathcal P(P).
                                                               \tag{4.22}
\]

For every nonempty normalized type, order its quotient packets
arbitrarily as one directed path.  Apply Theorem 4.1 at each adjacent
pair.  Starting from any phase \(u\) of the first packet, the successive
phase offsets determine one physical lifted path.  Each edge map is a
translation permutation of \(\mathbb Z_N\), so the \(N\) initial phases
give exactly \(N\) disjoint lifted paths and use every phase lift of every
packet in that type exactly once.

Because the port labels are distinct, after translating \(p_1\) to zero
there are at most the falling factorial \((N-1)_{s-2}\) ordered
normalized types at height \(s\).  Summing the \(N\) lifted paths per
nonempty type proves (4.17).
Apply Corollary 4.2 separately on every type: every physical packet
contributes one excess position, and every one of the \(NT_s\) chains at
height \(s\) contributes its exact \((s-1)\)-letter opening.  This proves
(4.18), and (4.19) follows from \(s-1\le H\) and (4.17).

Under (4.20), every physical packet has at least \(2\alpha H+2\) assigned
owner positions, so \(R\le W/(2\alpha H+2)\).  Finally

\[
 \log(2HN^{H-1})=O_A(\sqrt m\log m)=o(m),
\]

whereas \(W=\exp(m\log4+o(m))\).  Thus the second term in (4.21) is
\(o(W)\), and the first is \(o(W)\) because \(H\to\infty\).
Every chain consists of literal nonzero packet words from Theorem 3.1,
joined only by exact equality of ordered singleton ports.  Hence no
fractional owner assignment or cross-factor synchronization enters.
\(\square\)

Theorem 4.5 is an exact internal-target fusion theorem.  It freely
reorders packet charts in a direct literal word, so it does not preserve
the original adjacency of two packets.  Consequently it does **not**
represent a target whose original owner window crosses a packet boundary.
It also does not supply the packet assignment (4.20).  Those are the two
remaining global clauses.

### Corollary 4.6 -- edge-simple, edge-disjoint residence packings satisfy the baseline ledger

In Theorem 4.5, suppose instead that every physical packet traverses
\(2s(P)+1\) distinct directed owner edges and that the physical packet arcs
are pairwise edge-disjoint on the owner cycles.  Let \(U\) be the number
of distinct owner positions in their union.  Then

\[
 \boxed{M-U\le R.}                                \tag{4.23}
\]

Consequently, under (4.20),

\[
\begin{aligned}
 L_{\rm int}+(W-U)
 &=W+(M-U)+(L_{\rm int}-M)\\
 &<W+2R+2HN^{H-1}
 =W+o_A(W).                                      \tag{4.24}
\end{aligned}
\]

Thus every complete phase lift of any physical internally edge-simple,
pairwise edge-disjoint Gaussian residence packing can be recoded at
coefficient one for all middle owners and all packet-internal targets.

#### Proof

A packet with \(2s+2\) owner positions traverses \(2s+1\) distinct owner
edges.  Hence the total number of used directed edges is exactly

\[
 E=M-R.
\]

Pairwise edge-disjointness makes these \(E\) edges distinct.  Their union
is contained in the owner-position union and therefore \(U\ge E\).  Thus

\[
 M-U=R+E-U\le R,
\]

which proves (4.23).  Now append each of the \(W-U\) owner positions
outside the packet union as one literal set-letter.  Under (4.20),
edge-disjointness also gives
\(R(2\alpha H+1)\le W\), hence \(R=O(W/H)=o(W)\).  Combine this with
(4.19) and \(HN^{H-1}=o(W)\).
\(\square\)

The physical hypothesis is not automatic from a quotient packing.  A
quotient-to-physical application of this corollary must verify all of the
following: each quoted trace contains its full \(2s+1\)-edge packet,
each trace is nonwrapping and edge-simple, distinct quotient traces are
edge-disjoint, one fixed rotation-equivariant exact factor is used, and
the complete \(N\)-phase deck is lifted.  Under those hypotheses, distinct
quotient edges have disjoint physical edge fibres, so the lifted packets
satisfy the corollary.  Short or winding quotient traces which fail these
conditions must be charged separately.  No implication from an arbitrary
quotient-edge packing to (4.23) is asserted.

## 5. Why a standalone all-phase seam cannot work

Let \(\rho\) be cyclic rotation on an odd ground set of size \(N\), and
put

\[
 \mathcal E_{N,K}
 =\{X\subseteq[N]:
 |X\triangle\rho^tX|\le K
 \text{ for some }t\not\equiv0\pmod N\}.          \tag{5.1}
\]

### Lemma 5.1 -- rotational exceptional-set bound

For every \(K\ge0\),

\[
 \boxed{
 |\mathcal E_{N,K}|
 \le (N-1)2^{N/3}\sum_{j=0}^{K}\binom Nj.}        \tag{5.2}
\]

If \(K=O_A(\sqrt N)\), the right side is
\(2^{N/3+o_A(N)}\).

#### Proof

Fix \(t\ne0\).  The permutation \(\rho^t\) has
\(\gcd(t,N)\) cycles, each of odd length at least three, and therefore at
most \(N/3\) cycles.  A set \(X\) is determined by the transition set

\[
 \{x:1_X(x)\ne1_X(\rho^t x)\}
\]

and one initial bit on every \(\rho^t\)-cycle.  There are at most
\(2^{N/3}\sum_{j\le K}\binom Nj\) choices with transition set of size at
most \(K\).  Sum over the \(N-1\) nonzero rotations.  For
\(K=O_A(\sqrt N)\), the logarithm of the binomial sum is
\(O_A(\sqrt N\log N)=o_A(N)\). \(\square\)

### Lemma 5.2 -- rigid orbit separation

Let \(T_1,\ldots,T_q\) be distinct sets of one common rank and suppose

\[
 |T_a\triangle T_b|\le2H\qquad(1\le a,b\le q).    \tag{5.3}
\]

If every \(T_a\notin\mathcal E_{N,2H}\), then the \(Nq\) sets

\[
 \rho^uT_a,\qquad u\in\mathbb Z_N,\quad1\le a\le q,\tag{5.4}
\]

are pairwise distinct.

#### Proof

Suppose \(\rho^uT_a=\rho^vT_b\), and put \(t=v-u\).  If \(t=0\), then
\(T_a=T_b\), hence \(a=b\).  If \(t\ne0\), then
\(T_a=\rho^tT_b\), and (5.3) gives

\[
 |T_b\triangle\rho^tT_b|
 =|T_b\triangle T_a|\le2H,                        \tag{5.5}
\]

contrary to \(T_b\notin\mathcal E_{N,2H}\). \(\square\)

### Lemma 5.3 -- equal-rank endpoint injection

If a literal word represents \(M\) distinct targets of one common rank,
then the word has length at least \(M\).

#### Proof

Choose one witness interval for every target.  Two intervals with the same
left endpoint are nested, so their ORs are comparable by inclusion.
Distinct equal-rank sets are incomparable.  Hence the left endpoints are
all distinct, and there are at least \(M\) word positions. \(\square\)

### Theorem 5.4 -- no short appended phase-deck chart

At a depth-\(q\) strongly clean Johnson cut, let
\(T_1,\ldots,T_q\) be either its \(q\) lower crossing targets or its
\(q\) upper crossing targets.  If the templates are outside
\(\mathcal E_{N,2H}\), then every standalone word which represents this
family over all \(N\) phase lifts has length at least

\[
 \boxed{Nq}.                                       \tag{5.6}
\]

#### Proof

At a strongly clean cut, the \(q\) same-sign depth-\(q\) targets are
distinct and have their common correct rank.  Shifting the window start by
one changes at most one entering and one leaving label, so any two are at
symmetric-difference distance at most \(2(q-1)\le2H\).  Lemma 5.2 gives
\(Nq\) distinct rotations, and Lemma 5.3 proves (5.6). \(\square\)

For the canonical PBBS correct lower occurrences, one target has at most

\[
 \binom{2q+1}{q}                                   \tag{5.7}
\]

oriented occurrences; complementation gives the same statement for upper
targets.  Thus the total number of correct occurrences supported on the
exceptional family (5.2), for \(q\le H=O_A(\sqrt N)\), is at most

\[
 2^{N/3+o_A(N)},                                   \tag{5.8}
\]

where the factor (5.7) contributes only \(e^{O_A(\sqrt N)}\).  This is
exponentially negligible compared with
\(B=2^{N-o(N)}\).

Consequently the \(N\)-phase deck does not make generic targets equal.  It
provides exactly the \(Nq\) baseline positions which a fused in-place
compiler is allowed to reuse.  It cannot reduce a separate appendage to
\(O(N+H)\).

The preceding obstruction has a completely explicit genuine-return
witness; no genericity assumption is needed.

### Theorem 5.5 -- explicit Gaussian-return \(Nq\) obstruction

Let \(s\ge3\), \(L\ge1\),

\[
 m=s+L,
 \qquad N=2m+1,
 \qquad
 D_0=1^s0^{s-1}(10)^L0.                           \tag{5.9}
\]

Then \(D_0\) is primitive, \(d(D_0)=1\), and it starts a genuine first
zero-winding return of odd gap \(2s+1\).  For every

\[
 2\le q\le\left\lfloor {s+1\over2}\right\rfloor, \tag{5.10}
\]

one cut of the complementary owner row has \(q\) floor-correct crossing
intersections \(T_0,\ldots,T_{q-1}\) of common rank \(m-q+1\).  Their
complete phase deck consists of exactly \(Nq\) distinct targets.
Consequently every literal word representing all of them has length at
least \(Nq\).

#### Proof

Every proper prefix of \(D_0\) has positive height: after
\(1^s0^{s-1}\) the height is one, each copy of \(10\) returns it to one,
and only the last zero returns to height zero.  Thus \(D_0\) is primitive.
Direct application of the normalized \(\tau\)-move gives

\[
 D_1=1^s0^s(10)^L,                                \tag{5.11}
\]

and, for \(2\le h\le s\),

\[
 D_h=1^{h-2}(10)^L1^{s-h+2}0^s.                  \tag{5.12}
\]

Let \(\delta_h\) be the first-maximum displacement and put
\(C_h=\sum_{j=0}^{h-1}d(D_j)\).  Inspection of (5.9)--(5.12) gives

\[
\begin{aligned}
 d(D_0)&=1,& d(D_1)&=2L+1,&
 d(D_h)&=1 &&(2\le h<s),\\
 \delta_0&=\delta_1=s,&
 \delta_h&=s+2L &&(2\le h\le s),                 \tag{5.13}
\end{aligned}
\]

and therefore

\[
 C_1=1,
 \qquad C_h=2L+h\quad(2\le h\le s).             \tag{5.14}
\]

For \(h=1\), \(C_h<\delta_h\); for \(2\le h<s\),
\(C_h=2L+h<2L+s=\delta_h\); and

\[
 C_s=2L+s=\delta_s.                               \tag{5.15}
\]

The exact return criterion now proves that this is the first
zero-winding return and that its gap is \(2s+1\).  Notice that the proof
uses the whole orbit (5.11)--(5.13), not primitive invariance.

At phase zero, its omitted labels are

\[
 b_j=s-j\quad(0\le j<s),
 \qquad
 a_0=0,\quad a_1=N-1,\quad
 a_j=2s+1-j\quad(2\le j\le s).                  \tag{5.16}
\]

The inactive cores are

\[
\begin{aligned}
 K&=\{2s,2s+2,\ldots,2s+2L-2\},\\
 K'&=\{2s+1,2s+3,\ldots,N-2\},                  \tag{5.17}
\end{aligned}
\]

and hence the active order (2.3) is

\[
 \Gamma=(s,s-1,\ldots,1,0,N-1,2s-1,\ldots,s+1). \tag{5.18}
\]

Let \(X_j\) denote the rank-\((m+1)\) complementary owners.  Cut their
row between \(X_{q-1}\) and \(X_q\).  The depth-\(q\) owner windows
crossing that edge are exactly

\[
 [X_k,X_{k+1},\ldots,X_{k+q}]
 \qquad(0\le k<q).                                \tag{5.19}
\]

Their intersections are

\[
 \boxed{
 T_k=\bigcap_{j=k}^{k+q}X_j
     =K'\cup I_k,\qquad
 I_k=[s+1-k,\,2s+1-q-k],\qquad0\le k<q,}          \tag{5.20}
\]

where brackets on the right denote the ordinary coordinate interval in
the displayed range.  The interval \(I_k\) has length \(s-q+1\), so

\[
 |T_k|=L+s-q+1=m-q+1.                             \tag{5.21}
\]

Thus these are precisely the floor-correct depth-\(q\) intersections.

The set \(K'\) has trivial translation stabilizer.  For \(L=1\) it is a
singleton.  For \(L>1\), its cyclic gap word has \(L-1\) gaps equal to
two and one unique wrap gap equal to \(2s+3\); a stabilizing translation
must fix that unique gap and hence every point.  In \(T_k\), the interval
\(I_k\) is the unique cyclic component having more than one point.
Therefore a translation carrying \(T_k\) to \(T_\ell\) must carry
\(I_k\) to \(I_\ell\) and \(K'\) to itself.  The preceding stabilizer
statement forces the translation to be zero, and then (5.20) forces
\(k=\ell\).  Each \(T_k\) has a full \(N\)-orbit, and the \(q\) such
orbits are disjoint.  Hence the phase deck has exactly \(Nq\) distinct
equal-rank targets.  Lemma 5.3 gives the asserted word-length lower
bound. \(\square\)

This obstruction occurs at the Gaussian return scale.  Indeed, for any
integer \(c\ge1\), taking

\[
 L=cs^2-s
 \quad\hbox{gives}\quad
 m=cs^2,\qquad s={1\over\sqrt c}\sqrt m.          \tag{5.22}
\]

For any fixed \(A>0\), choose \(c>A^{-2}\); then the residence and every
\(q\) in (5.10) lie below \(H=\lceil A\sqrt m\rceil\) for all large
\(s\).  The conclusion is nevertheless only an **absolute chart-length**
obstruction.  It rules out replacing this full phase deck by a separate
\(O(N+H)\) seam (or by a compiler whose exposed baseline has only
\(N\) positions).  It does not rule out an in-place recoding which uses
the already-paid \(\Theta(Ns)\) owner collar; the quotient compiler sought
in Section 6 is deliberately baseline-relative at that scale.

### Theorem 5.6 -- the Gaussian phase-port graph has only self-loops

Assume the hypotheses of Theorem 5.5 and \(L>1\).  For its canonical
circular chart (3.12), let \(\mathcal P_u\) be the missing ordered port in
phase \(u\), and let \(\mathcal Z_v\) be the phase-\(v\) circular word.
Then \(\mathcal P_u\) occurs as a consecutive singleton subword of
\(\mathcal Z_v\) if and only if \(u=v\), and then it is the designated
port.  Consequently verbatim ordered-port splicing among the \(N\) phase
charts has only self-loops and saves no opening toll: its total duplicated
port length is

\[
 \boxed{N(s-1).}                                  \tag{5.23}
\]

#### Proof

From (5.18) and (3.11),

\[
 \mathcal P=(s+2,s+3,\ldots,2s-1,N-1),           \tag{5.24}
\]

while

\[
 \mathcal B=(1,2,\ldots,s),\qquad
 \gamma_s=0,\qquad\gamma_{2s}=s+1.               \tag{5.25}
\]

Thus the circular word is

\[
 \mathcal Z=\mathcal P,0,K,\mathcal B,K',s+1.    \tag{5.26}
\]

Because \(|K|=|K'|=L>1\), neither core letter is a singleton.  The only
cyclic runs of singleton letters in \(\mathcal Z_v\) are

\[
\begin{aligned}
 \mathcal B_v&=(v+1,v+2,\ldots,v+s),\\
 \mathcal R_v&=(v+s+1,v+s+2,\ldots,
                 v+2s-1,v-1,v),
\end{aligned}                                     \tag{5.27}
\]

with all coordinates reduced modulo \(N\).  The successive-difference
word of \(\mathcal P_u\) is

\[
 (\,\underbrace{1,\ldots,1}_{s-3},\,2L+1\,),     \tag{5.28}
\]

where for \(s=3\) only the last entry remains.  No length-\((s-1)\)
subword of \(\mathcal B_v\) has (5.28).  The three possible
length-\((s-1)\) subwords of \(\mathcal R_v\) start at its first, second,
or third letter.  Only the second has difference word (5.28), and it is
exactly \(\mathcal P_v\).  Finally,
\(\mathcal P_u=\mathcal P_v\) forces \(u=v\) by equality of their first
letters.  Hence every phase opening is isolated from all other phases.
Linearizing each of the \(N\) circular charts therefore duplicates its
own \(s-1\) port letters, proving (5.23). \(\square\)

The theorem closes only the canonical **verbatim ordered-overlap**
architecture.  A more general safe-pin splice could insert letters whose
new coordinates are already absorbed by a core or earlier pins; such a
splice would require explicit containment identities and a separate
position ledger.  Likewise (5.23) is not an additive lower bound against
an arbitrary in-place recoding of the \(\Theta(Ns)\) owner collar.

For this family \(e_0=\delta_0=s\) and
\(e_s=\delta_s=s+2L\), so

\[
 \Lambda=e_0+e_s-2m=0.                            \tag{5.29}
\]

There is no contradiction with Section 8: Theorems 5.5--5.6 are local
architecture obstructions for one complete deck, whereas Theorem 8.5
shows that the aggregate number of all such no-overlap decks is small
enough to append independently at \(o(W)\) cost.

There is likewise no contradiction with Theorem 4.5.  A normalized type
containing only this one quotient packet lifts to \(N\) singleton chains,
exactly as Theorem 5.6 requires.  The saving in Theorem 4.5 arises only
when different quotient packets share the same normalized type and are
placed consecutively before lifting.

## 6. Exact long-block quotient accounting

The preceding lower bound dictates the correct global formulation.  A
compiler must be baseline-relative.

Fix integers \(H,b\) with

\[
 1\le H<b,\qquad b\log N=o(m).                     \tag{6.1}
\]

Call a quotient \(\tau\)-cycle short if its length is less than \(b\).
The voltage-itinerary bound gives, for the number \(Z_b\) of quotient
edges on short cycles,

\[
 Z_b\le (2b+2)N^{2b+2}=\exp(o(m)).                 \tag{6.2}
\]

Since \(B=\exp(m\log4-O(\log m))\), one has

\[
 N H^2 Z_b=o(W).                                   \tag{6.3}
\]

Every quotient cycle of length \(L\ge b\) can be partitioned cyclically
into \(\lfloor L/b\rfloor\) blocks, each of length between \(b\) and
\(2b-1\).  Hence the total number of long-cycle blocks is at most

\[
 {B\over b}.                                       \tag{6.4}
\]

### Definition 6.1 -- baseline-relative quotient cluster compiler

A compiler \(\operatorname{QCF}(H,b;\eta_m,C_A)\) assigns to every such
block of length \(\ell\) and all its \(N\) phase lifts a direct nonzero
literal word which

1. represents every original middle owner assigned to the block;
2. represents every selected correct lower intersection and upper union of
   depth at most \(H\) whose original owner window lies in the block;
3. represents all support-essential targets of depth at most \(H\) crossing
   either block boundary, using the original radius-\(H\) collars;
4. uses no owner position assigned to a different block; and
5. has length at most

   \[
      N\ell+\eta_mN\ell+C_ANH.                    \tag{6.5}
   \]

The definition is literal.  It does not ask that the recoded positions
remain wreaths or owners, because clauses 1--3 directly construct the OR
word.  If a proof instead stays inside exact factors, it must additionally
verify exact middle ownership.

### Theorem 6.2 -- quotient cluster fusion implies coefficient-one central cost

Assume \(\eta_m=o(1)\), \(H/b=o(1)\), and
\(\operatorname{QCF}(H,b;\eta_m,C_A)\).  Then the entire PBBS central
band through depth \(H\) has a literal word of length

\[
 \boxed{
 W+O(\eta_mW)+O_A(WH/b)+o(W)=W+o(W).}             \tag{6.6}
\]

#### Proof

On the short quotient cycles, append every required lower and upper target
literally.  There are only \(O(H^2)\) target occurrences per physical
edge, so (6.3) makes their complete cost \(o(W)\).

On the long cycles, sum (6.5).  The baseline terms sum to at most \(W\),
the relative terms sum to at most \(\eta_mW\), and (6.4) bounds the collar
terms by

\[
 C_ANH{B\over b}=C_AW{H\over b}=o(W).             \tag{6.7}
\]

Clauses 1--4 ensure that the block words may be concatenated without
losing a required target or counting one baseline owner twice.  This proves
(6.6). \(\square\)

For example, for fixed \(A\), one may take

\[
 b=H\omega(m),\qquad
 \omega(m)\to\infty,\qquad
 \omega(m)\log m=o(\sqrt m).                      \tag{6.8}
\]

Then both conditions in (6.1) and \(H/b=o(1)\) hold.  After the standard
diagonalization in \(A\) and the already proved product-SCD tail, Theorem
6.2 composes quantitatively into coefficient one.  The unproved input is
the compiler, not its accounting.

## 7. What exact sector overlap gives, and what it does not

For an audited zero-winding orbit, write

\[
 D_h=P_h1R_h0S_h,\qquad
 d_h=|S_h|+1,\qquad e_h=|P_h|+1.                  \tag{7.1}
\]

The exact dual packet identity splits

\[
 S_h1P_h=P_{h+1}1\overline{T_h},                  \tag{7.2}
\]

where \(T_h\) is Dyck and

\[
 \epsilon_h=|T_h|+1=d_h+e_h-e_{h+1}.             \tag{7.3}
\]

For a return of length \(s\), the sharp caps are

\[
 \operatorname{ht}(S_h)\le h,\qquad
 \operatorname{ht}(T_h)\le s-h-1.               \tag{7.4}
\]

If zero returns begin both at phase \(0\) and at phase \(h\),
\(0<h<s\), the exact double-zero equations are

\[
 \boxed{
 \sum_{t=0}^{h-1}d_t
   =\sum_{t=s}^{s+h-1}\epsilon_t,\qquad
 \sum_{t=0}^{h-1}\epsilon_t
   =\sum_{t=s}^{s+h-1}d_t.}                       \tag{7.5}
\]

Thus the early and post-return packet rectangles have their two side
lengths interchanged.  This is precisely the scalar geometry one would
want for a port splice that preserves the original quotient adjacency.

However, (7.5) equates only total lengths.  The ordered port in (3.11)
records actual physical omitted labels, equivalently the literal order of
the relevant \(S\)- and \(T\)-border pieces.  Two compositions may have the
same two sums in (7.5) and different ordered words.  Therefore neither
(7.5) nor the unit rotor (1.2) proves a *prescribed-adjacency* instance of
(4.1).  Theorem 4.5 bypasses this issue for packet-internal targets by
discarding the prescribed adjacency and grouping normalized port types.

The exact remaining lemma needed on the dense sector is:

> **Crossing-border fusion \(\operatorname{CBF}_A\) -- unproved.**  For
> some fixed \(\alpha>0\), assign the dense genuine-return sector to
> physical packets of heights in \([\alpha H,H]\), using pairwise disjoint
> owner-position slots of total mass at most \(W\), so the number of
> packets is \(r=O(W/H)\).  Every required target assigned to this sector
> must either be internal to one packet or belong to an explicitly
> identified crossing/exceptional family.  Starting from the
> normalized-port word of Theorem 4.5 and the untouched owner positions,
> represent the entire crossing/exceptional family with \(o_A(W)\)
> additional or replacement letters.

Theorem 4.5 pays all packet-internal targets at excess
\(O(W/H)+\exp(o(m))=o(W)\).  Therefore
\(\operatorname{CBF}_A\) immediately gives a complete central-band word
of length \(W+o_A(W)\).  The substantive unsolved part is its last
sentence: Corollary 4.2 does not cover a target whose original owner
window crosses a packet boundary, and the arbitrary type ordering erases
rather than preserves those adjacencies.

There is a support-only form which is often easier to test.

### Theorem 7.1 -- rainbow packet cover sufficient condition

Fix \(A,\alpha>0\) and \(H=\lceil A\sqrt m\rceil\).  Suppose one can
choose complete \(N\)-phase decks of internally edge-simple, pairwise
edge-disjoint physical rainbow packet arcs with heights in
\([\alpha H,H]\).  Let \(\mathcal X_A\) be the set of
distinct required central-band target sets through depth \(H\) which are
not packet-internal targets of the chosen arcs.  If

\[
 \boxed{|\mathcal X_A|=o_A(W),}                   \tag{7.6}
\]

then the complete central band has a direct literal word of length
\[
 \boxed{W+o_A(W).}                                \tag{7.7}
\]

#### Proof

Corollary 4.6 gives a word of length \(W+o_A(W)\) containing every middle
owner and every packet-internal lower intersection and upper union.
Append each nonempty set in \(\mathcal X_A\) once as a one-letter word.
This adds exactly \(|\mathcal X_A|=o_A(W)\) positions and represents every
remaining required target literally. \(\square\)

Thus the unresolved crossing statement can equivalently be attacked as a
support theorem: construct the edge-disjoint rainbow packet cover and
show that its crossing/exceptional target **support**, not its occurrence
count, is \(o(W)\).  Neither the asserted falsity of \((RP_A)\) nor the
normalized port catalog proves (7.6).

## 8. The exact \(\Lambda=0\) sector is independently harmless

The crossing-border theorem remains relevant to a genuinely dense
positive-overlap sector.  The corrected no-overlap chamber itself admits
a stronger resolution: there are few enough packets to pay for every
phase lift independently.

For a zero return of length \(s\), define its endpoint overlap by

\[
 \Lambda=e_0+e_s-2m.                              \tag{8.1}
\]

The exact return equations imply \(\Lambda\ge0\).  Let \(e_{m,s}\) be the
number of semilength-\(m\) quotient roots which start a first zero-winding
return of length \(s\) and satisfy \(\Lambda=0\).

### Lemma 8.1 -- exact no-overlap generating function

Let \(C_j(z)\) be the generating function for Dyck paths of height at most
\(j\), with \(C_0=1\).  Then

\[
 \boxed{
 E_s(z):=\sum_{m\ge s}e_{m,s}z^m
 =z^s\prod_{j=1}^{s-1}
 C_{\min(j,s-j)}(z)^2.}                           \tag{8.2}
\]

If

\[
 Q_0=Q_1=1,\qquad Q_{j+1}=Q_j-zQ_{j-1},
 \qquad C_j={Q_j\over Q_{j+1}},                   \tag{8.3}
\]

and \(H_q=C_q-C_{q-1}\), then

\[
 \boxed{
 E_1=z,\qquad
 E_{2q}=H_q^2,\qquad
 E_{2q+1}=z(C_qH_q)^2\quad(q\ge1).}              \tag{8.4}
\]

At the critical point,

\[
 \boxed{
 E_{2q}(1/4)={4\over(q+1)^2(q+2)^2},\qquad
 E_{2q+1}(1/4)={4\over(q+2)^4}\quad(q\ge1).}     \tag{8.5}
\]

#### Proof

In the chamber \(\Lambda=0\), invoke the audited injective-and-surjective
forward/dual packet-array reconstruction: cutting a first return into its
forward and dual sectors produces independent Dyck arrays, and the inverse
concatenation recovers one root and preserves the strict earlier-return
inequalities.  Its caps are

\[
 \operatorname{ht}(S_h)\le\min(h,s-h),\qquad
 \operatorname{ht}(T_h)\le\min(h+1,s-h-1).       \tag{8.6}
\]

The \(s\) displayed spine edges contribute \(z^s\).  Pairing the forward
and dual sector of each cap gives the squared factors in (8.2).  For
\(s=1\) both arrays are empty, giving \(E_1=z\).

The recurrence (8.3), together with the inductive determinant identity
\(Q_j^2-Q_{j-1}Q_{j+1}=z^j\), gives

\[
 H_j={z^j\over Q_jQ_{j+1}}.                      \tag{8.6a}
\]

Thus the product in (8.2) telescopes.  For \(s=2q\) it is

\[
 {z^{2q}\over Q_q^2Q_{q+1}^2}=H_q^2,             \tag{8.7}
\]

and for \(s=2q+1\) it is

\[
 {z^{2q+1}\over Q_{q+1}^4}=z(C_qH_q)^2.          \tag{8.8}
\]

At \(z=1/4\), the recurrence gives

\[
 Q_j(1/4)={j+1\over2^j},\qquad
 H_q(1/4)={2\over(q+1)(q+2)},                    \tag{8.9}
\]

and (8.5) follows. \(\square\)

### Lemma 8.2 -- uniform coefficient anti-concentration

There is an absolute constant \(C_*>0\) such that, for every \(m\) and
every \(s\ge2\),

\[
 \boxed{e_{m,s}\le C_*{4^m\over s^6}.}           \tag{8.10}
\]

#### Proof

Let \(Y_q\) be the integer-valued random variable with probability
generating function

\[
 \mathbb E z^{Y_q}={H_q(z/4)\over H_q(1/4)}.      \tag{8.11}
\]

For \(u\in[-\pi,\pi]\), choose

\[
 x=\sqrt{1-e^{iu}},\qquad \Re x\ge0,\qquad
 \rho={1-x\over1+x}.                              \tag{8.12}
\]

The recurrence (8.3), solved by its two characteristic roots, gives the
exact identity

\[
 H_q(e^{iu}/4)
 ={8x^2\rho^q\over
   (1+x)^3(1-\rho^{q+1})(1-\rho^{q+2})}.          \tag{8.13}
\]

On the chosen branch,

\[
 \Re x\ge {|x|\over\sqrt2},\qquad
 |x|^2=2|\sin(u/2)|,\qquad
 |\rho|\le\exp\!\left(-{|x|\over3\sqrt2}\right).\tag{8.14}
\]

Also, for an absolute \(c_0>0\),

\[
 |1-\rho^k|
 \ge1-|\rho|^k
 \ge c_0\min(1,k|x|).                             \tag{8.15}
\]

Divide (8.13) by (8.9).  Positivity of the coefficients in (8.11)
supplies the complementary trivial characteristic-function bound by one.
Consequently, for absolute \(c,C>0\),

\[
 |\mathbb Ee^{iuY_q}|
 \le
 \begin{cases}
 1,&q|x|\le1,\\
 C(q|x|)^2e^{-cq|x|},&q|x|\ge1.
 \end{cases}                                      \tag{8.16}
\]

Near zero, \(|x|\asymp\sqrt{|u|}\).  Split the integral at
\(|u|=\pi/2\), use (8.16), and in the nontrivial part substitute
\(y=q|x|\).  The region \(q|x|\le1\) has length \(O(q^{-2})\), and the
remaining integral is \(O(q^{-2})\).  Thus

\[
 \int_{-\pi}^{\pi}
 |\mathbb Ee^{iuY_q}|^2\,du\le {C\over q^2}.      \tag{8.17}
\]

For \(s=2q\), equation (8.4) says that the normalized critical
Boltzmann coefficient distribution is that of \(Y_q+Y_q'\).  Fourier
inversion and (8.17) give maximum lattice atom \(O(q^{-2})\).  Multiplying
by the total critical mass \(E_{2q}(1/4)=O(q^{-4})\) gives

\[
 [z^m]E_{2q}(z)=O(4^mq^{-6}).                     \tag{8.18}
\]

For \(s=2q+1\), the distribution is, up to a unit shift, the sum of two
independent \(H_q\)-variables and two independent \(C_q\)-variables.
The normalized \(C_q\) characteristic function has modulus at most one,
so (8.17) gives the same atom bound.  Equation (8.5) again contributes
\(O(q^{-4})\).  Adjusting the absolute constant for bounded \(q\) proves
(8.10). \(\square\)

No local limit theorem is hidden in this proof; (8.17) is a direct Fourier
upper bound.

### Lemma 8.3 -- killed-path sharpening

There are absolute constants \(C,a>0\) such that, for every \(m,q\ge1\),

\[
\begin{aligned}
 4^{-m}e_{m,2q}
 &\le {C\over(q+2)^6}
       \exp\!\left(-{am\over(q+2)^2}\right),\\
 4^{-m}e_{m,2q+1}
 &\le {C\over(q+2)^6}
       \exp\!\left(-{am\over(q+2)^2}\right).
\end{aligned}                                      \tag{8.19}
\]

#### Proof

Put \(L=q+2\), and define normalized coefficients

\[
 u_{q,n}=4^{-n}[z^n]H_q(z),\qquad
 v_{q,n}=4^{-n}[z^n](C_qH_q)(z).                  \tag{8.20}
\]

Let \(P\) be simple random walk on \(\{1,\ldots,L-1\}\), killed on
hitting \(0\) or \(L\), and put

\[
 k_L(t)=(P^t)_{1,L-1}.                            \tag{8.21}
\]

The sine expansion for \(t\ge L^2\), and the reflection/image formula
together with the elementary binomial second-difference bound for
\(t\le L^2\), give absolute \(D_0,c_0>0\) such that

\[
 \boxed{k_L(t)\le D_0L^{-3}e^{-c_0t/L^2}.}        \tag{8.22}
\]

Indeed,

\[
 k_L(t)={2\over L}\sum_{j=1}^{L-1}
 (-1)^{j+1}\sin^2{\pi j\over L}
 \cos^t{\pi j\over L}.                           \tag{8.23}
\]

For \(t\ge L^2\), pair \(j\) with \(L-j\), use
\(\sin(\pi j/L)\le j\sin(\pi/L)\), and bound the eigenvalues by
\(e^{-ctj^2/L^2}\).  For \(t\le L^2\), let
\(p_t(a)=\Pr(S_t=a)\) for unrestricted simple random walk.  Pairing
opposite terms in the interval image expansion gives

\[
 k_L(t)=\sum_{r\ge0}
 \bigl[p_t((2r+1)L-2)-2p_t((2r+1)L)
                  +p_t((2r+1)L+2)\bigr].         \tag{8.23a}
\]

The ratio of consecutive binomial coefficients, applied twice, yields

\[
 |\Delta_2^2p_t(a)|
 \le Ct^{-3/2}\left(1+{a^2\over t}\right)
                e^{-ca^2/t}.                    \tag{8.23b}
\]

Summing (8.23b) over the odd images and absorbing the polynomial factor
into the exponential gives

\[
 k_L(t)\le Ct^{-3/2}e^{-cL^2/t}
          \le C'L^{-3}\qquad(0<t\le L^2).         \tag{8.23c}
\]

When \(t<L-2\), the left side is zero.  This completes both time ranges
of (8.22).

The exact Green mass is

\[
 \sum_{t\ge0}k_L(t)
 =[(I-P)^{-1}]_{1,L-1}={2\over L},                 \tag{8.24}
\]

because

\[
 [(I-P)^{-1}]_{x,y}
 ={2\min(x,y)(L-\max(x,y))\over L}.
\]

The coefficient \(u_{q,n}\) is the probability that a killed
length-\(2n\) excursion from \(1\) to \(1\) visits \(L-1\).  Mark one
visit, apply the Markov property, and split its time at \(n\).  On each
side, the longer leg is bounded by (8.22), while summing the other leg
uses (8.24).  Hence, for absolute \(D,c>0\),

\[
 \boxed{u_{q,n}\le DL^{-4}e^{-cn/L^2}.}           \tag{8.25}
\]

After replacing the constant \(c\) in (8.25), if necessary, by
\(\min(c,1)\), put

\[
 a_{q,k}=4^{-k}[z^k]C_q(z),
\]

and also put \(z_L=e^{1/L^2}/4\).  Choose
\(\alpha\in(0,\pi/2)\) by
\(\cos\alpha=e^{-1/(2L^2)}\).  The continuant sine formula gives

\[
\begin{aligned}
 \sum_{k\ge0}a_{q,k}e^{k/L^2}
 &=C_{L-2}(z_L)\\
 &=2e^{-1/(2L^2)}
   {\sin((L-1)\alpha)\over\sin(L\alpha)}
 <2.                                               \tag{8.26}
\end{aligned}
\]

Indeed,
\[
 \cos{\pi\over2L}
 \le e^{-\pi^2/(8L^2)}
 <e^{-1/(2L^2)}=\cos\alpha,
\]
so \(0<L\alpha<\pi/2\), and the sine ratio in (8.26) is less than one.
Since \(v=a*u\), (8.25)--(8.26) give

\[
 \boxed{v_{q,n}\le DL^{-4}e^{-cn/L^2}.}           \tag{8.27}
\]

Also,

\[
 H_q(1/4)\le3L^{-2},\qquad
 (C_qH_q)(1/4)\le4L^{-2}.                         \tag{8.28}
\]

For \(E_{2q}=H_q^2\), split the coefficient convolution at \(m/2\).
On each half the longer factor uses (8.25), while all values of the other
factor sum to \(H_q(1/4)\).  Hence

\[
 4^{-m}e_{m,2q}
 \le6DL^{-6}e^{-cm/(2L^2)}.                       \tag{8.29}
\]

For \(E_{2q+1}=z(C_qH_q)^2\), use (8.27)--(8.28) in the same way.
When the coefficient is nonzero, \(m-1\ge2m/3\) outside finitely many
cases, which are absorbed by the absolute constant.  This proves (8.19).
\(\square\)

### Lemma 8.4 -- sharp aggregate bounds

Uniformly in every cutoff \(H\),

\[
 \boxed{
 \sum_{1\le s<H}e_{m,s}
 \le C_0{4^m\over m^{5/2}},\qquad
 \sum_{1\le s<H}s\,e_{m,s}
 \le C_1{4^m\over m^2}.}                         \tag{8.30}
\]

Consequently,

\[
 \boxed{
 \sum_{1\le s<H}(3s+2)e_{m,s}
 \le C_2{4^m\over m^2}.}                         \tag{8.31}
\]

#### Proof

For every \(p>1\), integral comparison under
\(y=\sqrt{am}/x\), plus twice the unimodal maximum to absorb the lattice
error, gives

\[
 \sum_{r\ge1}r^{-p}e^{-am/r^2}
 =O_{a,p}\bigl(m^{(1-p)/2}\bigr).                 \tag{8.32}
\]

Apply (8.19) with \(p=6\) for the first sum and \(p=5\) for the
\(s\)-weighted sum.  Comparing \(s\) with \(q+2\) changes only absolute
constants.  The finitely many smallest \(s\)'s are covered after another
constant adjustment.  This proves (8.30)--(8.31). \(\square\)

### Theorem 8.5 -- all \(\Lambda=0\) phase decks cost \(o(W)\)

For every fixed \(A>0\) and all sufficiently large \(m\) (so in
particular \(H=\lceil A\sqrt m\rceil\le m\)), all \(N\) physical phase
lifts of all \(\Lambda=0\) zero returns with \(s+1\le H\) have
independent literal two-core charts of total length at most

\[
 \boxed{
 \Delta_{\rm chart}
 \le C_2N{4^m\over m^2}
 =O\!\left({W\over\sqrt m}\right)
 =o(W).}                                           \tag{8.33}
\]

If one instead pays a completely endpoint-safe cut and the audited
dominance seam for every such quotient start, their marginal contribution
is at most

\[
 \boxed{
 \Delta_{\rm cut}
 \le C_A N{4^m\over m^2}
 =O_A\!\left({W\over\sqrt m}\right)
 =o_A(W).}                                         \tag{8.34}
\]

Both statements allow arbitrary overlap among the packets.

#### Proof

Each quotient packet has exactly \(N\) spatial lifts.  Apply the
\((3s+2)\)-letter chart of Theorem 3.1 after the corresponding ground
rotation to each lift.  Equation (8.31) gives the first inequality in
(8.33).  The Wallis bound \(B\ge c4^m/m^{3/2}\), together with \(W=NB\),
gives the displayed normalized estimate.

For the cut version, choose one terminal trace edge for every quotient
packet and lift the selected edge through all \(N\) phases.  Deduplicate
coincident fibres.  The number of additional physical cuts is at most

\[
 J_0\le N\sum_{s<H}e_{m,s}.                       \tag{8.35}
\]

At one physical cut, endpoint extension plus the complete lower/upper
dominance seam costs at most

\[
 H+(4H-1)=5H-1.                                   \tag{8.36}
\]

new letters.  Equations (8.30), (8.35), and \(H=O_A(\sqrt m)\) give
(8.34).

If several quotient packets share the selected edge, all their complete
decks use the same \(N\)-edge physical fibre, so deduplication only lowers
\(J_0\).  If their selected edges differ, (8.35) already pays separately.
Appending packet charts never removes or recodes the baseline word; every
witness stays within its own chart, so overlapping packets cause no
logical conflict.  For the cut ledger, (8.34) is a marginal statement:
adjoin these cuts to whatever cut set handles all other short-residence
classes.  Every window destroyed by a new cut is restored by that cut's
\((4H-1)\)-letter chart, even when it crosses several cuts. \(\square\)

Thus \(\Lambda=0\) is completely removed from the **fusion** gate.  This
does not locate the counterexample falsifying \((RP_A)\); it says that any
part of that counterexample lying in \(\Lambda=0\) is aggregately harmless.
The surviving dense fusion obstruction must use \(\Lambda>0\), positive
winding, or another return class.  The crossing-border/block compiler of
Sections 4--7 is needed only there.

## 9. Independent audit of the decisive steps

1. **No primitive invariance.**  Lemma 2.1 assumes an actual owner
   chronology and pairwise distinct omitted labels, then uses only
   (2.7)--(2.8).  A genuine first zero return supplies rainbowness by the
   simple-return theorem.  The false converse from \(d=1\) is nowhere
   invoked.

2. **Packet length.**  The open packet has the \(s+1\) owners in (2.4)
   and the \(s+1\) owners in (2.5), hence \(2s+2\) middle owners.  The
   circular word has all \(2s+1\) active singleton labels plus the two
   nonempty core letters, hence \(2s+3\) positions.

3. **No hidden wrap in the \(K\)-row.**  In (3.5)--(3.6), all active
   endpoints lie between \(0\) and \(2s-1\).  The only empty active
   intersection is represented by the nonempty letter \(K\).

4. **The \(K'\)-row wrap is exact.**  Formula (3.8) contains the terminal
   label \(\gamma_{2s}\) and the initial labels
   \(\gamma_0,\ldots\).  Its portal order is exactly
   \(\mathcal B,K',\gamma_{2s},\mathcal P\), which is why precisely the
   \((s-1)\)-letter string \(\mathcal P\) is duplicated in (3.2).

5. **Phase matching and component voltage.**  Equation (4.3) checks
   physical labels, not merely normalized sectors.  A phase shift is a
   bijection, so all \(N\) lifts remain integral.  But this does not make
   a projected port component lift to one component: the exact count is
   (4.7).  In particular zero cycle voltage gives \(N\) lifted cycles.
   Theorem 4.5 does not assume that bound: it deliberately chooses one
   projected path per normalized type, hence exactly \(N\) lifted paths
   per type.  Height two has the single empty-difference type, while
   height one has an empty port and no opening toll; these boundary cases
   agree with (4.17).  Complete \(N\)-phase decks are essential to the
   bijective lift, and the global \(M\le W\) corollary requires disjoint
   owner-occurrence charging; overlapping packets cannot subtract the same
   baseline position twice.  For physical internally edge-simple,
   pairwise edge-disjoint packet arcs, (4.23) repairs the only permitted
   endpoint double charges and is sufficient.  A quotient packing must
   separately verify the lift conditions stated after Corollary 4.6.

6. **Standalone lower bound.**  Theorem 5.4 counts distinct target values,
   not occurrences.  It therefore survives the support-redundancy audit.
   It applies only when those values are support-essential for the proposed
   standalone chart; intact witnesses elsewhere may remove requests.

7. **Gaussian return and floor baseline.**  Theorem 5.5 checks the entire
   orbit (5.11)--(5.15).  At the audited cut a depth-\(q\) target is the
   intersection of \(q+1\) rank-\((m+1)\) complementary owners, hence has
   rank \(m-q+1\), exactly as (5.20)--(5.21) state.  Replacing
   \(\bigcap_{j=k}^{k+q}X_j\) by an intersection of only \(q\) owners
   would be an off-by-one error.

8. **Phase-port obstruction.**  Theorem 5.6 assumes \(L>1\), so the two
   core letters cannot masquerade as singleton port letters.  Its
   difference-word test checks every possible length-\((s-1)\) singleton
   subword of the circular chart, not only its chosen opening.  The
   \(N(s-1)\) conclusion is restricted to verbatim canonical-port
   overlap; it is not an in-place-recoding lower bound.

9. **Block count.**  A cycle of length \(L\ge b\) uses
   \(\lfloor L/b\rfloor\) blocks.  Distributing the remainder makes every
   block length at most \(2b-1\); summing the floors gives (6.4).

10. **No-overlap aggregate.**  In Lemma 8.2 the small Fourier region
    \(q|x|\le1\) has size \(O(q^{-2})\), which is sufficient and sharp for
    the displayed \(L^2\) estimate.  Lemma 8.3 adds the killed-path factor
    \(\exp[-am/(q+2)^2]\); summing it is what upgrades the pointwise
    \(s^{-6}\) estimate to the cutoff-uniform bounds (8.30).  The physical
    ledger appends independent charts, so packet overlap creates no
    ownership or witness conflict.

11. **Implication scope.**  Theorem 6.2 is a complete quantitative
   implication from \(\operatorname{QCF}\) to a central word, and Theorem
   4.5 unconditionally handles packet-internal targets for any supplied
   Gaussian packet assignment.  Neither \(\operatorname{QCF}\) nor the
   crossing-border statement \(\operatorname{CBF}_A\) is proved for the
   full PBBS sector counterexample.  No constant-one conclusion follows
   from the present report alone.

## 10. Final proved and conditional boundary

### Proved

* the exact unit-deficit phase rotor (1.2);
* the rainbow fixed-core theorem (2.4)--(2.11), which needs no return
  converse;
* the two-core linear packet compiler of length \(3s+2\);
* its circular form of length \(2s+3\), exposing a single ordered
  \((s-1)\)-letter opening toll;
* the exact all-phase port splice and chain ledger (4.4)--(4.5);
* the exact lifted voltage-component count (4.7), which prevents any
  automatic \(c_{\rm lift}\le B\) inference;
* the normalized-port clustering theorem (4.15)--(4.21), which bypasses
  that obstruction and gives \(o(W)\) excess for all packet-internal
  targets of any supplied disjoint Gaussian packet assignment;
* its physical internally edge-simple, pairwise edge-disjoint packing
  corollary (4.23)--(4.24), including the exact shared-endpoint charge
  \(M-U\le R\);
* the generic \(Nq\) endpoint obstruction to a standalone phase-deck
  chart;
* the explicit Gaussian-return family (5.9), with exactly \(Nq\) distinct
  floor-correct phase targets below every fixed \(A\sqrt m\) cutoff after
  constant rescaling;
* the self-loop theorem for its canonical phase-port overlap graph, forcing
  the exact \(N(s-1)\) opening cost in that architecture;
* the long-block quotient accounting theorem (6.6);
* the precise distinction between scalar double-zero side exchange and
  literal ordered-border equality;
* the support-only rainbow-cover implication (7.6)--(7.7);
* the exact no-overlap generating function (8.2)--(8.5), its killed-path
  coefficient bound (8.19), and the resulting unconditional
  \(O_A(W/\sqrt m)=o_A(W)\) cost for the entire \(\Lambda=0\) chamber,
  with arbitrary packet overlap.

### Conditional

If the exact sector-shift counterexample supplies
\(\operatorname{CBF}_A\), or more generally the block compiler
\(\operatorname{QCF}\), then its dense short returns can be fused with
\(o(W)\) total literal overhead.  The normalized-port theorem already
pays the packet toll and all ordered openings at \(o(W)\); only original
crossing/exceptional windows remain.  Theorem 5.6 explains why many
packets of the same normalized type, rather than the \(N\) phases of one
packet alone, are needed for that saving.

### Unproved

* a disjoint assigned packet ledger \(r=O(W/H)\) which captures the dense
  sector's support-essential targets;
* coverage of every support-essential window crossing two packet charts;
* equivalently, the support estimate \(|\mathcal X_A|=o_A(W)\) in
  Theorem 7.1;
* a baseline-relative quotient block compiler satisfying (6.5); and
* the resulting coefficient-one theorem.

The exact boundary is therefore: sparse packing is false; bare
same-packet phase symmetry is insufficient; normalized cross-packet port
types do fuse every internal chart at \(o(W)\); and the whole
\(\Lambda=0\) chamber is independently \(o(W)\).  What remains is a
baseline-relative in-place compiler for the positive-overlap/other-return
crossing windows.  It must prove a safe-pin/cluster containment splice
with an \(o(W)\) position ledger, or recode long quotient blocks directly
while covering every crossing window.  Neither statement is proved here,
so coefficient one is not claimed.
