# The nonflat K16 facet bridge and a conditional odd-to-even Pascal schedule

Date: 2026-07-31  
Lane: K, downstream RSB / odd-to-even Pascal transfer  
Status: exact algebraic normal form and independently replayed K15-to-K16
instance; conditional construction lemma; no all-dimension recurrence and no
compiler inheritance claim

## 0. Verdict

The two-rank depth-three row of the optimal K16 word is structured, not an
exceptional error term.  It is an exact **mixed-depth facet bridge** over the
optimal K15 carrier.

Write

\[
 V=[15],\qquad r=8,\qquad W=\binom{15}{8}=6435,
 \qquad z=15,
\]

and let

\[
             T=D^3(\texttt{answers/k15.word}).                 \tag{0.1}
\]

Then `T` is the 6,435-term rank-eight parent carrier.  In
`D^3(answers/k16.word)`:

* 6,435 unmarked terms are exactly one reordered copy of `T`;
* 6,386 marked rank-nine terms project to 6,386 distinct members of `T`;
* the remaining 49 marked terms project to 49 distinct rank-seven facets;
* at those first 6,386 starts, `D^2` gives 6,386 distinct marked rank-eight
  central targets; and
* those 6,386 `D^2` facets together with the 49 `D^3` bridge facets are
  exactly all \(\binom{15}{7}=6435\) facets.

Thus the K16 middle layer is delivered exactly once by

\[
 \underbrace{6386}_{z+\text{facet at depth }2}
 +\underbrace{6435}_{\text{old owner at depth }3}
 +\underbrace{49}_{z+\text{facet at depth }3}
 =12870.                                                     \tag{0.2}
\]

The number 49 has an exact source:

\[
                  49=45+(3+1).                               \tag{0.3}
\]

The 45 is the whole small physical component of the K15 carrier.  The four
are one complete depth-three opening collar in the large component.  The
ordinary marked parent-owner rail deletes precisely those 45+4 owners.
Consequently its two cyclic shift constants differ by exactly 45.

The 49 bridge facets and the 49 deleted parent owners have a 128-edge
containment graph with a perfect matching.  Together with the 6,386 literal
incidences \(D^2\subset D^3\), this completes a perfect facet-to-parent-owner
diamond matching.  This is the correct algebraic odd-to-even interface.

It is not yet an RSB recurrence.  Containment matching does not by itself
preserve the physical upper flag tower, residence, or the maximal-common-cap
lower compiler.  Those are three additional, occurrence-level hypotheses in
Theorem 5.1 below.

## 1. The abstract mixed-depth facet-bridge lemma

Let \(|V|=2r-1\), let \(z\notin V\), and put

\[
 {\cal U}=\binom Vr,\qquad {\cal F}=\binom V{r-1},\qquad
 |{\cal U}|=|{\cal F}|=W.                                  \tag{1.1}
\]

Let `A` be a word on \(V\cup\{z\}\).  Fix a depth \(d\).  Suppose three
disjoint sets of starts are declared:

\[
        O,\quad M,\quad B,\qquad |O|=W,\quad |M|=W-h,
        \quad |B|=h.                                       \tag{1.2}
\]

Call them respectively the old rail, ordinary marked rail, and bridge.
Assume:

1. \(D^dA_i\), \(i\in O\), are unmarked rank-\(r\) sets;
2. \(D^{d-1}A_i\), \(i\in M\), are marked rank-\(r\) sets, while
   \(D^dA_i\) are marked rank-\((r+1)\) sets; and
3. \(D^dA_i\), \(i\in B\), are marked rank-\(r\) sets.

Write

\[
\begin{aligned}
 u_i&=D^dA_i &&(i\in O),\\
 f_i&=D^{d-1}A_i\setminus\{z\},\quad
 U_i=D^dA_i\setminus\{z\} &&(i\in M),\\
 f_i&=D^dA_i\setminus\{z\} &&(i\in B).
\end{aligned}                                               \tag{1.3}
\]

### Lemma 1.1 (mixed-depth central exactness)

The declared windows deliver every rank-\(r\) child target exactly once if
and only if

\[
       \{u_i:i\in O\}={\cal U},\qquad
       \{f_i:i\in M\sqcup B\}={\cal F}                    \tag{1.4}
\]

as multisets.

#### Proof

Every rank-\(r\) child target either avoids \(z\), in which case it is a
member of \({\cal U}\), or contains \(z\), in which case deleting \(z\)
gives a member of \({\cal F}\).  The two classes are disjoint and both have
size \(W\).  Equations (1.3)--(1.4) are exactly these two bijections. \(\square\)

The lemma is deliberately nonflat.  The ordinary marked targets are served
at depth \(d-1\), while the old rail and bridge are served at depth \(d\).

### Lemma 1.2 (the exact residual diamond Hall condition)

Assume Lemma 1.1 and that the \(U_i\), \(i\in M\), are distinct.  Sliding
one extra cell gives the literal incidences

\[
                         f_i\subset U_i\qquad(i\in M).       \tag{1.5}
\]

Put

\[
 {\cal U}_0={\cal U}\setminus\{U_i:i\in M\},\qquad
 {\cal F}_0=\{f_i:i\in B\}.                                \tag{1.6}
\]

Both sets have size \(h\).  The fixed incidences in (1.5) extend to a
perfect incidence matching \({\cal F}\to{\cal U}\) if and only if the
bipartite graph

\[
 G_0=({\cal F}_0,{\cal U}_0; fU\text{ whenever }f\subset U) \tag{1.7}
\]

has a perfect matching.  Equivalently, for every
\(X\subseteq{\cal F}_0\),

\[
                         |N_{G_0}(X)|\ge |X|.                \tag{1.8}
\]

#### Proof

The \(W-h\) fixed pairs use distinct facets and distinct owners by (1.4)
and the hypothesis.  Any completion must pair precisely the unused facets
to the unused owners along containment edges; conversely any perfect
matching of (1.7) completes the fixed pairs.  Hall's theorem gives (1.8).
\(\square\)

This matching is a **marginal diamond completion**.  For each bridge edge
\(f\subset U\), physical upper-q1 service additionally requires a literal
one-sided or two-sided extension of the chosen bridge occurrence whose OR is
\(\{z\}\cup U\).  Abstract containment is not such an occurrence.

### Lemma 1.3 (the one-switch equality schedule)

Let the child have \(2W\) middle targets and equality length

\[
                             L=2W+d.                         \tag{1.9}
\]

Fix \(0\le h\le W\) and put \(q=W-h\).  On the physical positions
\([0,L)\), start target \(i\) at position \(i\), and choose its interval

\[
 I_i=
 \begin{cases}
 [i,i+d-1],&0\le i<q,\\
 [i,i+d],&q\le i<2W.
 \end{cases}                                                \tag{1.10}
\]

The omitted starts and deadlines are exactly

\[
\begin{aligned}
 X&=\{2W,2W+1,\ldots,2W+d-1\},\\
 Y&=\{0,1,\ldots,d-2\}\cup\{q+d-1\}.
\end{aligned}                                               \tag{1.11}
\]

The deadlines are strictly increasing, and the union of any consecutive
family \(I_i,\ldots,I_j\) is one physical interval.  Hence (1.10) is a legal
chain-aligned equality-length P/Q schedule.  Its unique internal omitted
deadline determines the bridge size:

\[
              h=W+d-1-\max Y.                               \tag{1.12}
\]

#### Proof

For \(i<q\), the deadlines are \(d-1,d,\ldots,q+d-2\).  For
\(i\ge q\), they are \(q+d,q+d+1,\ldots,2W+d-1\).  Their complement in
\([0,L)\) is (1.11), and the one-unit gap at the switch makes the sequence
strict.  Consecutive intervals overlap because \(d\ge1\), so their union is
contiguous.  Equation (1.12) is \(q=W-h\) rewritten. \(\square\)

The lemma is the scalar Pascal schedule behind the nonflat row.  It proves
neither that the requested interval ORs can be realized by nonempty common
caps nor that the resulting carrier is upper-complete.

### Lemma 1.4 (all-depth upper transfer through the switch)

Let \(C_i=\bigvee_{p\in I_i}A_p\) for the intervals (1.10).  If an upper
target \(U\) is the union of a consecutive carrier block,

\[
                       U=C_a\cup C_{a+1}\cup\cdots\cup C_b,  \tag{1.13}
\]

then \(U\) is the OR of the one physical interval

\[
                             [a,\max I_b].                   \tag{1.14}
\]

Consequently, if the mixed-depth carrier sequence \(C\) is upper-complete at
every depth, then the physical word is upper-complete at every depth.

#### Proof

By Lemma 1.3, \(I_a\cup\cdots\cup I_b=[a,\max I_b]\).  Taking the OR over
the selected carrier rows and then over their physical windows gives the OR
over that union, proving (1.14). \(\square\)

Thus the upper RSB state does not have to remember separate physical
witnesses once it has certified both chain alignment and upper completeness
of the mixed carrier.  Constructing that upper-complete carrier remains a
global braid problem.

## 2. Exact K16 decomposition

The retained inputs are

```text
answers/k15.word
SHA-256 f35da2f0c98ec07de3e5318554157af490558e881be5c8bbcb5e3d1c8c08b14b

answers/k16.word
SHA-256 890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe
```

Index `T` from 0 to 6,434.  Its two physical components occupy

\[
 C=T[0,6390),\qquad S=T[6390,6435),                         \tag{2.1}
\]

of lengths \(p=6390\) and \(s=45\).  Put

\[
             d=3,\qquad a=5109,\qquad b=6426.               \tag{2.2}
\]

The deleted primary collar is

\[
                    Q=T[5109,5113),                         \tag{2.3}
\]

of length \(d+1=4\).

### Theorem 2.1 (literal two-shift/four-chunk identity)

Read the marked rank-nine terms of `D^3(answers/k16.word)`, delete \(z\),
and number them \(j=0,\ldots,6385\).  They are exactly

\[
 \begin{cases}
 T_{j+5113},&0\le j<1277,\\
 T_{(j+5158)\bmod6435},&1277\le j<6386.
 \end{cases}                                                \tag{2.4}
\]

Thus the two shifts differ by

\[
                         5158-5113=45=s.                    \tag{2.5}
\]

The omitted parent-owner indices are exactly

\[
                       [5109,5112]\sqcup[6390,6434],         \tag{2.6}
\]

namely \(Q\sqcup S\).

The 6,435 unmarked `D^3` terms are exactly the four chunks

\[
\begin{array}{c|c|c}
\text{parent indices}&\text{length}&\text{global shift}\ \hline
[5112,6389]&1278&5112\\
[0,5111]&5112&5157\\
[6426,6434]&9&36\\
[6390,6425]&36&6426.
\end{array}                                                 \tag{2.7}
\]

In particular, this is one rotation of each of the two parent components,
not one cyclic rotation of all 6,435 owners.

#### Proof

The literal equalities are independently replayed by the audit in Section
6.  Their indexing also explains the shifts.  The ordinary marked owner
list is

\[
       T[a+d+1,p)\ \Vert\ T[0,a).                           \tag{2.8}
\]

The first piece has length \(p-a-d-1=1277\) and shift
\(a+d+1=5113\).  After wrapping inside the primary component rather than
inside all \(W\) terms, its global modulo-\(W\) shift increases by the
satellite length \(s\), giving 5158.  Its complement is exactly (2.6).

The old rail is the primary rotation

\[
             T[a+d,p)\ \Vert\ T[0,a+d)                     \tag{2.9}
\]

followed by the satellite rotation

\[
             T[b,W)\ \Vert\ T[p,b),                        \tag{2.10}
\]

which gives (2.7). \(\square\)

### Theorem 2.2 (exact 45+4 facet bridge)

For the final K16 word, the sets in Lemma 1.1 are consecutive start banks

\[
 O=[6390,12825),\quad M=[0,6386),\quad
 B=[6386,6390)\sqcup[12825,12870).                          \tag{2.11}

\]

They satisfy (1.4).  Moreover

In the four-spiral carrier anatomy, \(M\) is the first 6,386 terms of the
6,390-term marked large block.  The bridge is exactly its last four terms
together with the entire 45-term marked small block.

\[
 |B|=4+45=49,                                               \tag{2.12}
\]

The mixed-depth occurrence sequence is not merely a set partition.  In its
literal order,

\[
 D^2A[0,6386)\ \Vert\ D^3A[6386,12870)                     \tag{2.13}
\]

is byte-for-byte the endpoint-rerooted target file
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word, whose
SHA-256 is
c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906.

The rank histogram of the full depth-three row is

\[
                    8^{W+49}\,9^{W-49}
                    =8^{6484}\,9^{6386}.                    \tag{2.14}
\]

Lemma 1.3 with \(q=W-h=6386\) gives

\[
 X=\{12870,12871,12872\},\qquad
 Y=\{0,1,6388\},                                            \tag{2.15}
\]

which is exactly the frozen optimal K16 schedule.  Thus the internal
deadline hole, the two-rank derivative histogram, and the 49-term facet
bridge are three forms of the same integer \(h\).

The residual graph (1.7) has

\[
 |{\cal F}_0|=|{\cal U}_0|=49,\qquad |E(G_0)|=128,          \tag{2.16}
\]

and a perfect matching.  Its degree histograms are

\[
\begin{aligned}
 \deg_{{\cal F}_0}&:1^1 2^{17}3^{31},\\
 \deg_{{\cal U}_0}&:1^1 2^{18}3^{29}4^1.
\end{aligned}                                               \tag{2.17}
\]

#### Proof

On \(M\), the 6,386 values `D^2 A` are distinct marked rank-eight
targets.  On \(B\), the 49 values `D^3 A` are distinct marked rank-eight
targets.  After deleting \(z\), these two banks are disjoint and their union
is all \(\binom{V}{7}\).  On \(O\), the values `D^3 A` are exactly all
\(\binom V8\).  Concatenating these literal banks in start order gives the
retained endpoint-rerooted target file, proving (2.13).  Lemma 1.1 applies.

The `D^3` owner projections on \(M\) are the 6,386 parent owners in (2.4),
so (2.6) is the residual owner set.  Direct containment gives (2.16)--(2.17),
and an augmenting-path replay finds matching size 49.  The rank count in
(2.14) is the partition into \(O\sqcup B\) versus \(M\). \(\square\)

An immediate invariant is worth recording.  In every mixed-depth normal
form with bridge size \(h\),

\[
 N_r(D^dA)-N_{r+1}(D^dA)=2h.                               \tag{2.18}
\]

Thus the K16 histogram itself forces \(h=(6484-6386)/2=49\).

## 3. The general two-component indexing law

The arithmetic above does not depend on 6,435.

### Proposition 3.1 (satellite jump law)

Let a parent carrier order consist of a primary cyclic component of length
\(p\) followed by a satellite component of length \(s\), so \(W=p+s\).
Choose a primary collar

\[
                         Q=[a,a+b)                            \tag{3.1}
\]

of length \(b\).  If the ordinary marked owner rail is

\[
             T[a+b,p)\ \Vert\ T[0,a),                       \tag{3.2}
\]

then it has length \(W-(s+b)\), omits exactly \(Q\sqcup S\), and its two
global modulo-\(W\) shift constants differ by exactly \(s\).

If the old rail is one rotation of each parent component and the bridge has
one facet for each omitted owner, then the depth-\(d\) rank histogram is

\[
            r^{W+s+b}\,(r+1)^{W-s-b}.                       \tag{3.3}
\]

#### Proof

The two pieces in (3.2) have total length \(p-b=W-s-b\), and their omitted
indices are precisely \([a,a+b)\) and the satellite.  Before the wrap the
shift is \(a+b\).  After the wrap, expressing a primary-component rotation
modulo \(W\) inserts the skipped satellite length \(s\), so the shift is
\(a+b+s\).  The rank count is Lemma 1.1: the old rail and bridge have rank
\(r\), while the ordinary marked depth-\(d\) owners have rank \(r+1\).
\(\square\)

For K16, \(b=d+1=4\).  Proposition 3.1 does **not** assert that every
odd-to-even lift must use \(b=d+1\).  It says that once a protected
depth-\(d\) opening collar of that length and the entire satellite component
are assigned to the bridge, both 49 and the shift jump 45 are forced.

## 4. What the matching proves, and what it does not

The perfect matching in Theorem 2.2 completes the exact lower-facet versus
parent-owner diamond incidence.  It has two immediate uses.

1. It supplies the right finite carrier-side state for a Pascal recursion:
   ordinary incidences are frozen, and only the \(h\)-by-\(h\) residual
   containment graph is live.
2. If each selected residual edge \(f\subset U\) has a literal bridge socket
   extending the physical occurrence of \(\{z\}\cup f\) to an interval with
   OR \(\{z\}\cup U\), then every tagged upper-q1 target is served exactly
   once.

Neither statement gives deeper upper service.  For that, one needs either:

* an occurrence-labelled nested ray above every selected bridge socket; or
* an independently upper-complete child carrier chronology together with a
  chain-aligned physical schedule that transfers every consecutive carrier
  interval to a physical interval.

K16 uses the second route.  The endpoint-rerooted true-four-filter carrier
is independently audited to cover every upper rank, and its P/Q schedule is
chain-aligned.  The 49-by-49 matching is therefore an algebraic explanation
of the nonflat middle interface, not the proof of its all-depth upper tower.

The lower compiler is still further removed.  A matching between facets and
parent owners does not choose one common physical letter assignment for
overlapping lower intervals.  The optimal K16 compiler required the exact
maximal-common-cap matching on 347,677 residual target-cell incidences and is
strongly asymmetric.  No inheritance of that matching from K15 is proved.

## 5. Conditional odd-to-even facet-bridge recurrence

Let \(k=2r\) and assume a deadline plateau

\[
                         d(2r-1)=d(2r)=d.                    \tag{5.1}

\]

Suppose an optimal odd parent supplies a rank-\(r\) all-depth carrier on
\(V=[2r-1]\), decomposed into a primary component and a satellite bank.
The literal full double

\[
       A\ \Vert\ \{z\}\ \Vert\ (\{z\}\cup A)
\]

has length \(2(W+d)+1\), whereas the child target length is \(2W+d\).
Thus an equality lift must save \(d+1\) cells.  The closed splice deletes
one tagged endpoint for free and has length \(2(W+d)\); it still has to save
exactly \(d\) cells.  Lemma 1.3 is the exact middle-schedule form of that
remaining \(d\)-cell compression.  It does not itself construct the common
letters.

### Theorem 5.1 (conditional equality-length facet-bridge lift)

Assume there is a word of length

\[
                         2W+d=B(2r)                          \tag{5.2}

\]

and a chain-aligned middle schedule satisfying all five conditions below.

1. **Mixed-depth central partition.**  Lemma 1.1 holds for some bridge bank
   \(B\).
2. **Residual diamond completion.**  The graph (1.7) has a perfect matching,
   and every selected bridge edge has a physical upper-q1 socket.
3. **All-depth upper transfer.**  Every upper target has an occurrence in
   the child carrier whose consecutive carrier block maps to one contiguous
   physical interval.  It is enough to give occurrence-labelled nested rays
   at the bridge and retain the parent all-depth witness atlas elsewhere.
4. **Residence.**  The exact start/deadline event stream, including every
   bridge and seam collar, obeys the depth-\(d\) safe-corridor inequalities.
5. **Lower common cap.**  After all protected socket pins, the exact
   target-cell incidence system has an injective assignment whose maximal
   common caps are nonempty and reproduce every middle row.

Then the child word is universal and

\[
                              \nu(2r)=B(2r).                  \tag{5.3}

\]

#### Proof

Condition 1 gives every middle target exactly once.  Conditions 2--3 give
every upper target as a literal interval; condition 2 alone only handles the
tagged q1 face, while condition 3 supplies the rest.  Condition 4 proves the
scheduled central occurrences survive the physical braid.  Condition 5
gives every lower target in one common word rather than in incompatible
rankwise assignments.  The length is (5.2), and the deadline lower bound is
\(B(2r)\). \(\square\)

This is a genuine construction theorem, but its hypotheses are not yet
proved uniformly.  The new gain over a flat Pascal lift is that the child is
allowed to transfer \(W-h\) tagged targets at depth \(d-1\) and the other
\(h\) through a depth-\(d\) facet bridge.  The optimal K16 word is the first
exact endpoint of this form with

\[
           h=s+d+1=45+4=49.                                 \tag{5.4}

\]

For a recursive RSB state, the facet bridge therefore adds the finite tuple

\[
  (\text{component rotations},Q,
    G_0,\text{selected sockets},
    \text{upper rays},\text{run collars},
    \text{common-cap boundary relation}).                   \tag{5.5}

\]

The first three fields are the new algebraic compression.  The last four
remain occurrence-level.  In particular, 45 is finite in K16 but no theorem
currently bounds the total satellite bank uniformly in \(r\).  The K16
certificate does not prove a bounded-width all-even induction.

## 6. Independent audit

The lightweight exact replay is

```text
scratch/audit_k16_nonflat_facet_bridge_pascal_normal_form_20260731.py
```

It recomputes `D^2` and `D^3` from both literal answer words, verifies
(2.4)--(2.14) and the mixed-depth carrier equality (2.13), reconstructs the
128-edge containment graph, and proves its
matching size 49 by augmenting paths.  The canonical sorted matching-pair
payload has SHA-256

```text
5aff68bdb102b665560ad76cb2ae420e90d5d3ffd0f99d847b0e78ec1085de16
```

The audit is intentionally scoped to the algebraic facet bridge.  Full
literal universality of `answers/k16.word` is independently certified in
`MATH_CERTIFICATE_K16_OPTIMAL_12873_TRUEFF_COMMONCAP_20260731.md`.

## 7. Precise remaining theorem

The candidate odd-to-even recursion is no longer “make `D^d` flat.”  It is:

> Find a primary/satellite decomposition, a protected opening collar, and a
> mixed-depth facet partition for which the residual containment matching
> can be realized by occurrence-labelled all-depth sockets, while the same
> braid state admits an accepting maximal-common-cap lower assignment.

The marginal residual matching is small in K16 and completely solved.  The
two unproved correlations are (i) socket-to-deep-ray compatibility and (ii)
socket-to-common-cap compatibility.  Any uniform RSB theorem must control
those two correlations; carrier rank counts and the 49-by-49 matching alone
cannot do so.
