# Entry-neutral rotating-frame two-port seams: the exact phase-residence invariant

Date: 2026-07-25

Method: pure mathematics only. No computation, search, solver, or web access is
used.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad 1\le q\le H\le m-2,
\]

and fix one omitted source pair

\[
 A=\{a_1,a_2\}.
\]

The entry-neutral rotating-frame rainbow seam requested in
`DIFFUSE_COLLISION_FUSION_ATTACK_20260725.md` does **not** exist in the
exact recursive pair-omission Pascal/Gray model as stated.

The obstruction is an exact coordinate-residence invariant.  In the
switched realization of any owner-fixed upper spike from source phase
\(A\), every upper flag below depth \(q\) avoids \(A\), while the
depth-\(q\) flag contains one coordinate of \(A\).  Along a physical
middle-owner path, that coordinate therefore enters for the first time
exactly \(q\) transitions after the designated owner.  Physicality through
depth \(H\) keeps it present for at least \(H\) consecutive middle owners.
Every other designated phase-\(A\) owner, as well as every one of its
upper flags below depth \(q\), avoids all of \(A\).  Consequently two
switched spike starts \(t<t'\) on one physical Pascal/Gray path satisfy

\[
 \boxed{t'-t\ge q+H.}
 \tag{0.1}
\]

The recursive Gray braids of Theorems 4.1 and 9.1 in the recursive-pair
report impose the slightly stronger convention that every coordinate
residence is **greater** than \(H\).  Under that convention,

\[
 \boxed{t'-t\ge q+H+1.}
 \tag{0.2}
\]

Thus a physical module containing \(p\) switched occurrences from one
source-phase/depth stratum has at least

\[
 \boxed{1+(p-1)(q+H)}
 \tag{0.3}
\]

principal owner positions, and at least

\[
 1+(p-1)(q+H+1)
 \tag{0.4}
\]

under the strict recursive Gray residence hypothesis.  In particular, a
packet of \(p=H\) occurrences needs \(\Omega(H^2)\) owner positions, not
\(H+O(1)\).  Even a block of length \(cH+O(1)\) can contain only
\(c+O(1)\) such occurrences.

This theorem is independent of collision targets, multiplicities, packet
rainbowness, frame orientations, and entrance/exit choices.  It applies to
the switched realization alone, so identical two-port endpoint states
cannot repair it.  The shifted-cut Pascal/Gray construction preserves the
residence invariant at every seam and therefore cannot compile an
arbitrary abstract rainbow packet at unit density.

The exact escape is narrower than the requested lemma: occurrences from
different source phases may be globally interleaved so that useful states
of one phase serve as the \(A\)-occupied residence interval of another, or
one may abandon the phase-fixed \(q\)-clean owner tower and construct
targets by a different direct-OR mechanism.  Neither is an independently
concatenable entry-neutral packet.  No constant-one conclusion follows.

## 1. Physical owner paths and the residence lemma

Let

\[
 X_0,X_1,\ldots,X_{L-1}\in\binom{[n]}m
 \tag{1.1}
\]

be a simple middle-owner path.  At every valid start \(t\) and depth
\(h\), define its canonical lower and upper Pascal flags by

\[
 L_h(t)=\bigcap_{j=0}^{h}X_{t+j},
 \qquad
 U_h(t)=\bigcup_{j=0}^{h}X_{t+j}.
 \tag{1.2}
\]

Call the path **physical through depth \(H\)** when

\[
 |L_h(t)|=m-h,
 \qquad
 |U_h(t)|=m+h
 \tag{1.3}
\]

for every \(1\le h\le H\) and every valid start.  In particular every
successive pair is a Johnson edge.  Write

\[
 X_{s+1}=X_s-\{d_s\}+\{e_s\}.
 \tag{1.4}
\]

### Lemma 1.1 -- exact minimum coordinate residence

Suppose a coordinate \(x\) first enters at the edge

\[
 X_{r-1}\longrightarrow X_r,
 \qquad x\notin X_{r-1},\quad x\in X_r.
 \tag{1.5}
\]

If it later leaves and \(X_{r+s}\) is the first subsequent owner not
containing \(x\), then

\[
 \boxed{s\ge H.}
 \tag{1.6}
\]

Equivalently, every nonterminal membership run has at least \(H\) owner
states.  If the construction assumes residence greater than \(H\), then
\(s\ge H+1\).

#### Proof

The coordinate lies in

\[
 X_r,X_{r+1},\ldots,X_{r+s-1}
\]

and is absent from both \(X_{r-1}\) and \(X_{r+s}\).  If \(s<H\), the
window

\[
 X_{r-1},X_r,\ldots,X_{r+s}
\]

has \(s+1\le H\) transitions.  In those transitions \(x\) is first an
entering coordinate and later a departing coordinate.  Hence the
\(s+1\) departures remove at most \(s\) coordinates of the initial owner
\(X_{r-1}\).  Its intersection therefore has size at least

\[
 m-s>m-(s+1),
\]

contradicting (1.3) at depth \(s+1\).  Thus \(s\ge H\).  The final
sentence is just the integer interpretation of residence greater than
\(H\).  \(\square\)

This is the only physical fact needed below.  Notice that it is integral
and local; no averaging or target histogram is involved.

## 2. Exact visible action of one owner-fixed upper spike

Fix one source phase with omitted pair \(A\).  Every source row lies in

\[
 Q_A=[n]\setminus A,
\]

so all of its middle owners and all of its upper flags avoid \(A\).

Take one selected token occurrence \(i\), with old upper tower

\[
 U_0^0(i)\subset U_1^0(i)\subset\cdots\subset U_H^0(i),
 \qquad U_0^0(i)=Y_i.
 \tag{2.1}
\]

Let

\[
 b_i\in U_q^0(i)\setminus U_{q-1}^0(i)
 \tag{2.2}
\]

be the unique depth-\(q\) entering marker, choose

\[
 z_i\notin U_H^0(i)\cup A,
 \qquad B_i=\{b_i,z_i\},
 \tag{2.3}
\]

and let \(\theta_i\) exchange the coordinates of \(A\) with those of
\(B_i\).  Denote by \(a(i)\in A\) the image of \(b_i\).

The owner-fixed spike identities are

\[
 \theta_iY_i=Y_i,
 \qquad
 \theta_iU_h^0(i)=U_h^0(i)\quad(0\le h<q),
 \tag{2.4}
\]

and

\[
 \theta_iU_q^0(i)
 =U_q^0(i)-\{b_i\}+\{a(i)\}.
 \tag{2.5}
\]

The second coordinate of \(A\) does not appear in (2.5), because its
partner \(z_i\) was chosen outside \(U_H^0(i)\).

### Lemma 2.1 -- the forced first entrance

Suppose a physical path realizes the switched tower of occurrence \(i\)
at start \(t\); that is,

\[
 U_h(t)=\theta_iU_h^0(i)
 \qquad(0\le h\le H).
 \tag{2.6}
\]

Then

\[
 X_t,X_{t+1},\ldots,X_{t+q-1}
 \quad\hbox{all avoid }A,
 \tag{2.7}
\]

while

\[
 a(i)\in X_{t+q}\setminus X_{t+q-1}.
 \tag{2.8}
\]

Thus an actual coordinate of the fixed source pair enters for the first
time exactly \(q\) owner transitions after the designated occurrence.

#### Proof

For \(h<q\), equations (2.4) and (2.6) give

\[
 U_h(t)\cap A=\varnothing.
\]

Taking \(h=q-1\) proves (2.7).  Equations (2.5)--(2.6) give

\[
 U_q(t)\cap A=\{a(i)\}.
\]

Since the earlier union avoids \(A\), this coordinate first appears in
the last owner \(X_{t+q}\), proving (2.8).  \(\square\)

The statement uses actual ground coordinates, not names of moving frames.
Relabelling a recursive child or changing its omitted pair does not alter
the membership assertion (2.8).

## 3. The phase-residence separation theorem

We now permit arbitrary rotating frames, arbitrary recursive Gray seams,
arbitrary ordering of the packet occurrences, and arbitrary common
entrance and exit states.  The only requirements are those in the proposed
seam theorem: every designated occurrence has its fixed phase-\(A\)
central owner, its flags below \(q\) remain old, and its depth-\(q\) upper
flag is the occurrence-specific conjugate flag.

### Theorem 3.1 -- exact separation of switched phase-\(A\) spikes

Let \(t<t'\) be two designated switched spike starts on one path physical
through depth \(H\).  Both spikes come from the same omitted source pair
\(A\) and the same depth \(q\).  Then

\[
 \boxed{t'-t\ge q+H.}
 \tag{3.1}
\]

If every coordinate residence is greater than \(H\), then

\[
 \boxed{t'-t\ge q+H+1.}
 \tag{3.2}
\]

#### Proof

Apply Lemma 2.1 to the spike at \(t\), and put \(a=a(i)\).  The
coordinate \(a\) first enters at \(X_{t+q}\).

First suppose

\[
 0<t'-t<q.
\]

Set \(h=q-(t'-t)\), so \(1\le h<q\).  The owner \(X_{t+q}\) occurs in
the upper depth-\(h\) window beginning at \(t'\).  Consequently

\[
 a\in U_h(t').
\]

But the second occurrence is \(q\)-clean: all of its upper flags below
\(q\) equal old phase-\(A\) flags and hence avoid \(A\).  This is a
contradiction.

Next suppose

\[
 q\le t'-t<q+H.
\]

By Lemma 1.1, after entering at \(X_{t+q}\), the coordinate \(a\) remains
present through at least

\[
 X_{t+q},X_{t+q+1},\ldots,X_{t+q+H-1}.
\]

Hence \(a\in X_{t'}\).  The designated central owner at \(t'\) is fixed
pointwise by its helper conjugacy and belongs to the original phase-\(A\)
row, so it avoids all of \(A\).  This is again a contradiction.

The two excluded intervals cover every positive gap less than \(q+H\),
proving (3.1).  If residence is greater than \(H\), Lemma 1.1 retains
\(a\) for one additional owner, giving (3.2).  \(\square\)

Equivalently, with

\[
 \chi_A(s)={\bf1}_{\{X_s\cap A\ne\varnothing\}},
 \tag{3.2a}
\]

every designated switched start forces

\[
 \chi_A(t)=\cdots=\chi_A(t+q-1)=0,
 \qquad \chi_A(t+q)=1,
 \tag{3.2b}
\]

and the last (1) begins a run of length at least (H).  A later
designated start needs a new zero run of length (q).  Formula (3.1) is
exactly the minimum spacing between these two forced trace patterns.

Three features of this proof are worth making explicit.

1. The two spikes may use different helpers \(z_i\), different partner
   pairs \(B_i\), and opposite bijections between \(A\) and \(B_i\).
   The entering coordinate is always an element of the same fixed set
   \(A\).
2. The two spike occurrences need not be consecutive in either their old
   rows or their collision fibres.  The proof uses only their actual
   positions in the proposed switched realization.
3. No endpoint hypothesis is used.  Therefore giving the two realizations
   identical ordered entrance and exit states cannot weaken the bound.

### Corollary 3.2 -- exact density and length bounds

If a physical path of \(L\) owner positions contains \(p\ge1\) designated
switched phase-\(A\), depth-\(q\) spikes, then

\[
 \boxed{
 p\le 1+\left\lfloor\frac{L-1}{H+q}\right\rfloor,
 }
 \tag{3.3}
\]

or equivalently

\[
 \boxed{L\ge1+(p-1)(H+q).}
 \tag{3.4}
\]

Under residence greater than \(H\), replace \(H+q\) by \(H+q+1\).

#### Proof

Order the spike starts

\[
 t_1<t_2<\cdots<t_p.
\]

Theorem 3.1 gives \(t_{j+1}-t_j\ge H+q\).  Summing the \(p-1\) gaps
and using \(t_p-t_1\le L-1\) proves both formulas.  \(\square\)

At critical length \(L\le cH+C\), this gives

\[
 p\le 1+\frac{cH+C-1}{H+q}<c+2+\frac CH.
 \tag{3.5}
\]

Thus a critical block carries only \(O_c(1)\) same-phase, same-depth clean
spikes.  This is an occurrence-capacity theorem, not merely a component or
boundary estimate.

## 4. Refutation of the proposed entry-neutral packet

Take an abstract rainbow packet

\[
 \mathcal P=\{i_1,\ldots,i_p\},
 \qquad p\le H,
 \tag{4.1}
\]

inside one source phase \(A\) and one depth \(q\).  Rainbowness says that
no two occurrences lie in the same old collision fibre.  It imposes no
condition relevant to Theorem 3.1.

Suppose the requested two realizations existed.  In \(R^1(\mathcal P)\),
all \(p\) occurrence-specific conjugate towers are present on one physical
Pascal/Gray module.  Their central owners are distinct because the base
token matching is middle-simple, so they occupy \(p\) distinct principal
starts.  Corollary 3.2 yields

\[
 |R^1(\mathcal P)|_{\rm owner}
 \ge1+(p-1)(H+q).
 \tag{4.2}
\]

In every exact MTF/Pascal literalization, moving to the next principal
owner consumes one new physical update position.  Common entrance and
exit contexts can remove a bounded initialization term, but they cannot
compress the internal owner span in (4.2).  Hence a claimed uniform bound

\[
 |R^1(\mathcal P)|=p+C
 \tag{4.3}
\]

with \(C\) independent of \(H\) would imply

\[
 p+C\ge1+(p-1)(H+q).
 \tag{4.4}
\]

This already fails for \(p=2\) once \(H+q>C+1\).  Taking \(p=H\) gives
the stronger lower bound

\[
 |R^1(\mathcal P)|_{\rm owner}
 \ge1+(H-1)(H+q)=\Omega(H^2).
 \tag{4.5}
\]

Therefore the requested entry-neutral seam is false.  The conclusion is
stronger than a failure of identical ports: it remains false if the two
realizations are allowed unrelated entrance and exit states.

The only degenerate case not excluded is \(p=1\).  A one-occurrence helper
is exactly the already proved owner-fixed spike chart, and its independent
literalization may pay one separate source-row piece.  It has no bearing
on the desired \(H\)-to-one packet compression.

If a convention counts the terminal future context needed to expose the
last complete depth-(q\) tower, it adds another (q) transitions to the
owner span.  This only strengthens (4.2); it is deliberately omitted from
the stated lower bound so that no endpoint-counting convention is hidden.

## 5. Why recursive Pascal/Gray rotation does not evade the invariant

The recursive construction exposes a pair through the unique physical
Gray order

\[
 0\longrightarrow a\longrightarrow ab\longrightarrow b
 \longrightarrow0.
 \tag{5.1}
\]

The shifted-cut fusion of synchronized orientation cubes changes cut
indices so that successive child packets meet at a common orientation.
Its proof explicitly checks two facts:

* every active coordinate direction has no repeat within the protected
  horizon; and
* each exposed coordinate remains fixed across a whole child packet, whose
  length is greater than \(H\).

Those are precisely the hypotheses behind Lemma 1.1.  For a switched
phase-\(A\) spike, the pair-occupancy trace is zero through the first
\(q\) principal owners and becomes nonzero at the next one.  Before another
phase-\(A\) designated owner can occur, the trace must return to zero.
The Gray order cannot make that return before the entering coordinate has
completed its protected residence interval.

Changing the moving-frame name from \(A\) to \(B_i\) does not change the
actual trace

\[
 t\longmapsto X_t\cap A.
 \tag{5.2}
\]

Similarly, shifted cuts alter which edge of a Gray cycle is omitted, but
they do not alter membership runs of ground coordinates.  Every exact seam
in Theorems 4.1, 9.1, and 9.3 is a Johnson edge inside one physical owner
path, so Theorem 3.1 continues across the seam without a reset.

Thus the recursive construction supplies **entry-neutral packet fusion
only for synchronized states whose protected occupancy traces are already
compatible**.  An abstract rainbow partition based solely on collision
fibres does not provide that compatibility.

## 6. The exact surviving route

The negative theorem closes the proposed black-box implication

\[
 \text{abstract rainbow bin of size }H
 \quad\Longrightarrow\quad
 \text{one }H+O(1)\text{ phase-fixed two-port seam}.
 \tag{6.1}
\]

It does not close every possible rotating chronology.  Three logically
distinct escapes remain.

1. **Cross-phase age interleaving.**  While a coordinate of \(A\) resides,
   the intervening owner positions may be useful occurrences from other
   source phases.  A global schedule could therefore amortize the spacing
   without treating each rainbow packet as an independent module.  Such a
   schedule must be built before binning and must satisfy all phase
   residence traces simultaneously.
2. **Age-compatible packetization.**  Replace Theorem 1.1 of the diffuse
   collision report by a packet theorem whose colour classes are not only
   collision-rainbow but also have a bounded path-cover number in the
   phase/age compatibility digraph.  No such theorem is currently proved.
3. **Non-Pascal direct OR service.**  A literal crossing interval might
   realize a desired rank-\((m+q)\) target without assigning it as the
   canonical union of \(q+1\) consecutive middle owners.  That would be a
   different seam language and must reprove central ownership, lower flags,
   and the exact word-length ledger directly.

Owner-fixed spikes remain appropriate for genuinely heavy fibres because
they can be emitted as sparse separate pieces.  The theorem here explains
why they cannot be compressed, merely by rotating frames, into a dense
same-phase packet for the diffuse bounded-load sector.

## 7. Audit of constants, quantifiers, and implication scope

1. The generic physical bound is residence at least \(H\), not necessarily
   greater than \(H\).  This is why the unconditional separation constant
   is \(H+q\).  The recursive-pair Gray lemmas explicitly assume residence
   greater than \(H\), yielding the sharpened \(H+q+1\).
2. The first interval in the proof of Theorem 3.1 uses the next spike's
   depth
   \[
    h=q-(t'-t),
   \]
   which lies in \(\{1,\ldots,q-1\}\).  Hence the argument uses exactly,
   and only, the promised invariance of upper flags below \(q\).
3. At gaps from \(q\) through \(q+H-1\), the contradiction is with the
   next central owner itself.  Central-owner fixation is therefore
   essential and is exactly one of the owner-fixed helper identities.
   The pointed token and its upper tower also fix the forward orientation;
   reversing the local path would exchange the directed upper and lower
   data and is not the same occurrence.
4. The argument is valid for every \(1\le q\le H\).  At \(q=1\), the
   first interval is empty and the residence interval alone gives spacing
   at least \(H+1\).  The separately solved \(q=1\) seed does not rescue
   the requested packet compiler, although constant one does not require
   this spike mechanism at depth one.
5. No assertion is made that every global constant-one construction must
   consist of phase-fixed canonical Pascal towers.  The no-go is exact for
   the requested recursive pair-omission/Gray seam and for every stronger
   theorem retaining its six stated tower and port conditions.

## 8. Precise proved boundary

Proved:

* the minimum residence Lemma 1.1;
* the forced depth-\(q\) entry identity (2.8);
* the exact separation bounds (3.1)--(3.2);
* the packet length bounds (3.4) and (4.5);
* failure of the entry-neutral rotating-frame two-port rainbow seam at
  length \(|\mathcal P|+O(1)\), even without imposing common ports.

Not proved:

* a global cross-phase age-interleaving schedule;
* an age-compatible rainbow/path-cover packet theorem;
* a direct-OR seam which abandons canonical Pascal owner windows while
  retaining integrality and the complete lower/owner ledger;
* the constant-one theorem.

The exact missing object is therefore no longer the stated independent
rainbow-packet seam.  It is a **global phase-age scheduler** (or a genuinely
non-Pascal direct-OR substitute) which can use the forced \(H+q\) residence
intervals as useful work rather than paid packet overhead.
