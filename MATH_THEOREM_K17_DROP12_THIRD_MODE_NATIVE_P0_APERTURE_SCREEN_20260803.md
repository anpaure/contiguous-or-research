# K17 drop-12 lossless third-mode native-P0 aperture screen

**Date:** 2026-08-03  
**Status:** unconditional constant-delta theorem on each of the 94 frozen
anchored pair survivors. This is a lossless necessary screen for a three-mode
occurrence packing, and an exact characterization of the stated partial
source-plus-partner-P0 gate. It does not enumerate third modes, certify the
third ticket, certify the partner's phase-1 ticket, replay suppliers, or
produce a K17 word.

All finite statements are bound to canonical compressed/final parent hashes

    e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb
    fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c

and to the exact 94-survivor replay whose ledger has SHA-256
f33f6ed5a7102ee3cc63a260a0608685a6776586c8014015ad8df56c0c4421c5.

## 1. Exact ticket semantics

For phase \(\phi\in\{0,1\}\), let \(R_\phi\) be the incumbent reservation
map from its 20 reserved physical rows to their flags. The maps have 17
shared rows and 23 union rows. A row reserved in phase \(\phi\) is
unavailable in that phase. A row reserved only in phase \(1-\phi\) is
available in phase \(\phi\) only at its incumbent flag. The 7,213 private
rows are unavailable in both phases.

For installed, pairwise endpoint-disjoint modes \(I\), let
\({\cal L}_I^\phi\) be the phase-\(\phi\) long-state bank after deleting
every donor \(d_x\), \(x\in I\), and inserting the four flagged states at
every host \(h_x\). In this definition the bank is already filtered by the
exact reservation rules: remove every private row and every row in
\(\operatorname{dom}R_\phi\); if
\(v\in\operatorname{dom}R_{1-\phi}\setminus
\operatorname{dom}R_\phi\), retain only its state at flag
\(R_{1-\phi}(v)\). All admissible incumbent LLR hosts remain in the bank.

For a short role \(x\), declared key

\[
 k=(q,\alpha,\beta),\qquad
 0\le q<9,\quad 0\le\beta\le\alpha<4,
\]

write \({\cal T}_x^\phi(k;I)\) for the literal tuples
\(t=(p,\alpha;s,\beta)\) in \({\cal L}_I^\phi\) satisfying the exact
incoming, outgoing, and common five-cell predicates. If \(p=s\), then
\(\alpha=\beta\). Let \(\operatorname{row}(t)=\{p,s\}\) be its physical
footprint and \(\operatorname{flag}(t)\) its induced row-to-flag map.

Two tuples in the same phase are compatible exactly when their physical
footprints are disjoint. Tuples in different phases are compatible exactly
when their flag maps agree on every reused physical row. These are the
current exact phase-capacity and cross-phase-coalescing semantics.

For a source \(e\), define its two-phase option set

\[
 {\cal O}_e(I)=
 \bigcup_k
 \left\{(t_0,t_1):
 t_\phi\in{\cal T}_e^\phi(k;I),\
 \operatorname{flag}(t_0)\cup\operatorname{flag}(t_1)
 \text{ is a function}\right\}.                       \tag{1.1}
\]

## 2. The one-delete/one-host delta identity

Fix one of the 94 ordered pair survivors \((e,f)\), where \(e\) is the
authenticated rank-improving source and \(f\) is its partner. Let \(g\) be
a fixed-bank-safe mode whose two endpoints are disjoint from all four
endpoints of \(e,f\).

Relative to the pair child, installing \(g\) changes either long bank by
exactly

\[
 {\cal L}_{efg}^\phi
 =
 \left({\cal L}_{ef}^\phi\setminus\{\text{all states at }d_g\}\right)
 \cup\{H_g^\phi(0),H_g^\phi(1),H_g^\phi(2),H_g^\phi(3)\}. \tag{2.1}
\]

For \(x\in\{e,f\}\), put

\[
\begin{aligned}
 {\cal S}_x^\phi(k;g)
   &:=\{t\in{\cal T}_x^\phi(k;ef):
                  d_g\notin\operatorname{row}(t)\},\\
 {\cal G}_{x\leftarrow g}^\phi(k)
   &:=\{t\in{\cal T}_x^\phi(k;efg):
                  h_g\in\operatorname{row}(t)\}.
\end{aligned}                                           \tag{2.2}
\]

### Lemma 2.1 (exact delta)

\[
 \boxed{
 {\cal T}_x^\phi(k;efg)
 =
 {\cal S}_x^\phi(k;g)
 \;\dot\cup\;
 {\cal G}_{x\leftarrow g}^\phi(k).}                    \tag{2.3}
\]

#### Proof

Deletion of \(d_g\) removes precisely the old tuples using that physical
row. The only newly available long state is at \(h_g\), so every tuple not
present after the deletion but present after installing \(g\) uses \(h_g\).
Conversely, every surviving old tuple and every valid host-using tuple is
present in the triple bank. The union is disjoint because \(h_g\) was an LR
row, not a long-state row, before \(g\) was installed. \(\square\)

The 94-pair exact replay proves

\[
 {\cal T}_f^0(k;ef)=\varnothing
 \quad\text{for every declared key }k.                 \tag{2.4}
\]

Therefore (2.3) collapses to

\[
 \boxed{
 {\cal T}_f^0(k;efg)
 =
 {\cal G}_{f\leftarrow g}^0(k).}                       \tag{2.5}
\]

In words: every partner native-P0 tuple created by a third mode uses the
third mode's new host. Merely deleting \(d_g\) can never help.

Consequently the gained partner menu has only the three incident-host forms

\[
 (H_g^0(\alpha),z^\beta),\qquad
 (z^\alpha,H_g^0(\beta)),\qquad
 (H_g^0(\alpha),H_g^0(\alpha)),                       \tag{2.6}
\]

where \(z\) ranges over the surviving pair bank after deleting \(d_g\), and
each displayed pair is retained only when the exact incoming, outgoing, and
five-cell predicates hold. The third form is the same-row case and therefore
requires equal flags. Thus the first third-mode screen never needs a full
unanchored regeneration of the partner's native-P0 menu.

## 3. The smallest lossless partial screen

Since every tuple in (2.5) occupies \(h_g\) in phase 0, a source tuple
coexisting with it in phase 0 cannot use \(h_g\). By Lemma 2.1, the source's
phase-0 tuple must therefore be an inherited pair tuple avoiding \(d_g\).
Only its phase-1 tuple may be newly supplied by \(h_g\).

Define the reduced source options

\[
\begin{aligned}
 \widehat{\cal O}_e(g):=
 \bigcup_k\{(t_0,t_1):\;&
 t_0\in{\cal S}_e^0(k;g),\\
 &t_1\in
 {\cal S}_e^1(k;g)\cup{\cal G}_{e\leftarrow g}^1(k),\\
 &\operatorname{flag}(t_0)\cup\operatorname{flag}(t_1)
   \text{ is a function}\}.
\end{aligned}                                           \tag{3.1}
\]

For \(o=(t_0,t_1)\in\widehat{\cal O}_e(g)\) and a partner-P0 tuple \(u\),
write \(o\sim_0 u\) when

\[
 \operatorname{row}(t_0)\cap\operatorname{row}(u)
 =\varnothing                                           \tag{3.2}
\]

and

\[
 \operatorname{flag}(t_0)\cup\operatorname{flag}(t_1)
 \cup\operatorname{flag}(u)
 \quad\text{is a function}.                            \tag{3.3}
\]

Finally put

\[
 {\cal A}_{e,f}(g)=
 \left\{(o,u):
 o\in\widehat{\cal O}_e(g),\
 u\in\bigcup_k{\cal G}_{f\leftarrow g}^0(k),\
 o\sim_0u\right\}.                                     \tag{3.4}
\]

The key indexed in \(\widehat{\cal O}_e(g)\) is common only between the two
phases of source \(e\). The independent key indexing the partner-P0 tuple
\(u\) need not equal the source key.

### Theorem 3.1 (third-mode native-P0 aperture)

Installing \(g\) creates a literal native-P0 tuple for \(f\) which can
coexist with at least one complete two-phase source option for \(e\), under
the exact phase-20 reservations and cross-phase flag coalescing, if and only
if

\[
 \boxed{{\cal A}_{e,f}(g)\ne\varnothing.}               \tag{3.5}
\]

#### Proof

Suppose the partial packing exists. By (2.5), its partner-P0 tuple \(u\)
uses \(h_g\). Phase-0 unit capacity forces the source's phase-0 tuple \(t_0\)
to avoid \(h_g\). Lemma 2.1 then puts \(t_0\) in
\({\cal S}_e^0(k;g)\). The source's phase-1 tuple lies in the full triple
menu, hence by Lemma 2.1 it lies in
\({\cal S}_e^1(k;g)\cup{\cal G}_{e\leftarrow g}^1(k)\).
The source key is common across phases. Same-phase capacity gives (3.2), and
the one-flag physical address gives (3.3). Thus \((o,u)\in{\cal A}_{e,f}(g)\).

Conversely, an element of \({\cal A}_{e,f}(g)\) consists of exact literal
tuples built from the triple long banks. Equation (3.1) gives a same-key
two-phase source option, (3.2) gives phase-0 capacity against the partner
tuple, and (3.3) gives global flag consistency. The state-bank definition
already enforces the private-row and phase-20 reservation rules. Hence these
three tuples form precisely the claimed partial packing. \(\square\)

This is smaller than rebuilding arbitrary triple menus:

* partner P0 is searched only in the \(g\)-host aperture;
* source P0 is searched only among surviving pair tuples;
* source P1 is the only source side requiring an old-or-\(g\)-host delta;
* only three ticket footprints enter the compatibility test.

The statistic of \(g\) relevant to this gate is exactly its deleted donor
row \(d_g\) and its eight phase/flag host states
\(\{H_g^\phi(a):\phi=0,1,\ 0\le a<4\}\). No other parent long state changes.
This is a constant-size **state delta**; it is not a claim that the
preindexed aperture query has constant running time.

### Corollary 3.2 (retaining the existing pair option)

For a fixed pair source option
\(o_e=(k_e,w_e^0,w_e^1)\in{\cal O}_e(ef)\), put

\[
 \eta_g(o_e)=
 {\bf1}\!\left[
 d_g\notin\operatorname{row}(w_e^0)
       \cup\operatorname{row}(w_e^1)\right]             \tag{3.6}
\]

and

\[
\begin{aligned}
 \Delta^0_{e\to f}(g;o_e):=
 \eta_g(o_e)
 \sum_k\#\{u\in{\cal G}_{f\leftarrow g}^0(k):\;&
 \operatorname{row}(u)\cap\operatorname{row}(w_e^0)
 =\varnothing,\\
 &\operatorname{flag}(u)\cup
 \operatorname{flag}(w_e^0)\cup\operatorname{flag}(w_e^1)
 \text{ is a function}\}.
\end{aligned}                                           \tag{3.7}
\]

Then

\[
 \boxed{\Delta^0_{e\to f}(g;o_e)>0}                    \tag{3.8}
\]

if and only if \(g\) creates a native-P0 tuple for \(f\) compatible with
retaining that literal source option unchanged.

All 94 exact replay rows have one source tuple in each phase and one
cross-phase-compatible source option. Therefore (3.8) is the cheapest exact
screen if “preserve” is deliberately restricted to that existing option.
Because the zero-edge output ledger records the count but not the rejected
source option's literal signature, an implementation of (3.8) must regenerate
and hash-bind that option; it must not infer the signature from the minus-one
final-witness columns.
It is not lossless for all triples, because \(g\) may delete the old
source-P1 tuple and create a replacement. Theorem 3.1 is the lossless version
that retains this repair branch.

## 4. Why three tempting smaller screens are unsound

The following are sharp counterexamples at the exact capacity-semantics
level. They are not claims that these toy signatures occur among the 94
physical K17 pairs.

### 4.1 Separate nonemptiness is insufficient

Let the \(g\)-host be \(z\). Suppose the new partner-P0 tuple has footprint
\(\{z,a\}\), while the only surviving source-P0 tuple has footprint
\(\{a,b\}\). The partner aperture and the source option are separately
nonempty, but they cannot coexist because both use \(a\) in phase 0.
Therefore (3.2) cannot be omitted.

### 4.2 Phase-local disjointness is insufficient

Suppose the partner-P0 tuple uses \(a\) at flag 0 and the source-P1 tuple
uses the same physical row \(a\) at flag 1. Their phase-local footprints are
disjoint, but the physical flag address cannot take both values. Therefore
(3.3) cannot be omitted.

### 4.3 Retaining only old source options is not lossless

Suppose the old source-P1 tuple uses \(d_g\), while the source-P0 tuple
survives. After installing \(g\), a new source-P1 tuple uses \(h_g\) at flag
\(a\), and the new partner-P0 tuple also uses \(h_g\) at flag \(a\).
The two uses are in opposite phases and are legal after coalescing. A screen
which only retains old source options rejects this valid partial packing.
The gained term \({\cal G}_{e\leftarrow g}^1\) in (3.1) is therefore
necessary.

## 5. Proof-safe execution order after the screen

For each of the 94 pairs, a bounded third-mode lane may:

1. enumerate only fixed-bank-safe \(g\) with six pairwise distinct endpoints;
2. apply (2.2)--(3.5);
3. only for survivors, generate the complete partner phase-1 menu and both
   phase menus for \(g\);
4. test the full three-color option compatibility problem with all phase
   capacities and one global flag map;
5. jointly materialize the three transfers and replay the complete supplier
   matching.

A positive result at (3.5) is not a three-mode occurrence certificate,
because the partner's phase-1 tuple and both tickets of \(g\) are not yet
priced. A negative result is an exact no-go for that ordered
\((e,f,g)\) triple: every complete occurrence packing would restrict to the
partial packing characterized by Theorem 3.1.

Thus the theorem is the smallest lossless screen at the newly identified
barrier. It replaces a broad triple materialization by one host-aperture,
one surviving source-P0 bank, one source-P1 delta, and one three-ticket
compatibility test.
