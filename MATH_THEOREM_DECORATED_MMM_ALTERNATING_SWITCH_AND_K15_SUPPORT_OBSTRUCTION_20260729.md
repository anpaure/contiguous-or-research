# Decorated MMM alternating switches and the k=15 global-support obstruction

Date: 2026-07-29

Status: exact switch-generation theorem, exact decoration interface, and a
rigorous support lower bound for the audited canonical `k=15` symmetric
carrier.  No decorated all-`k` existence theorem and no `k=15` optimal word
is proved here.  The numerical canonical-`k=15` input comes from the
independently replayed live-source audit in
`MATH_MERINO_MICKA_MUTZE_STRICT_SPIRAL_PROJECTION_20260729.md`; its downloaded
payload was not frozen, so applications of the numerical corollary retain
that provenance caveat.

## 1. The correct quotient switch space

Fix

\[
 k=2m+1,\qquad r=m+1,\qquad
 W=\binom{k}{r}=k\operatorname {Cat}_m,qquad
 N=\operatorname {Cat}_m.                                \tag{1.1}
\]

Let `rho` rotate `Z_k`.  Write `M_k` for the bipartite Middle Levels graph
between

\[
 \mathcal U=\binom{\mathbb Z_k}{r},\qquad
 \mathcal L=\binom{\mathbb Z_k}{r-1}.                    \tag{1.2}
\]

The action is free on both central layers, and also on inclusion edges.  In
fact, a set fixed by a nonidentity rotation is a union of cycles of some
length `d>1` dividing `k`, so its cardinality is divisible by `d`; but
`gcd(k,m)=gcd(k,m+1)=1`.  An inclusion edge cannot be inverted because its
two endpoints have different ranks, and fixing it would fix both endpoints.
Let

\[
 \overline M_k=M_k/\langle\rho\rangle                    \tag{1.3}
\]

be the quotient **multigraph**, retaining parallel inclusion-edge orbits and
their phase/voltage labels.  It has `N` upper and `N` lower vertices.

A spanning 2-factor `F` of `Mbar_k` has degree two at every upper and lower
necklace.  At a lower necklace `c`, its two selected inclusion edges expand
to two upper extensions of one physical representative of `c`; contracting
`c` gives one Johnson edge orbit of lower colour `c`.  Thus contraction of
`F` is exactly a rotation-invariant Johnson 2-factor which

* has weighted degree two at every upper necklace; and
* selects exactly one Johnson edge orbit over every lower necklace colour.

Conversely every such coloured Johnson factor expands uniquely at each
lower vertex to a spanning 2-factor of `Mbar_k`.

The MMM theorem supplies, for every unit shift, one connected such factor of
unit voltage.  The question here is how all other factors are generated from
it.

## 2. Alternating-cycle generation theorem

Let `F_0` be a fixed spanning 2-factor of `Mbar_k`.  Colour an edge of a
second spanning 2-factor `F_1` blue if it is in `F_1\F_0`, and colour an edge
red if it is in `F_0\F_1`.

At every upper **and lower** quotient vertex,

\[
 d_{\rm red}(v)=d_{\rm blue}(v),                          \tag{2.1}
\]

because both factors have degree two and common incidences cancel.

### Theorem 2.1 (complete raw switch generation)

The two-coloured symmetric difference `F_0 triangle F_1` decomposes into
edge-disjoint closed alternating even circuits.  Toggling the red and blue
edges of any one circuit preserves degree two at every upper and lower
necklace.  Toggling all circuits gives `F_1`.

Conversely, if `C` is an `F_0`-alternating even circuit in `Mbar_k`, then

\[
 F_0\triangle C                                          \tag{2.2}
\]

is another spanning 2-factor.  Its contraction preserves every middle owner
and the perfect lower-q1 rainbow exactly.

Support-minimal nonzero sign-compatible degree-preserving switches are
simple alternating cycles, including the parallel-edge 2-cycle convention.

#### Proof

At every vertex, pair each red incidence with a blue incidence.  Starting
from any unused red edge and following the paired blue edge, then the paired
red edge, and so on, produces a closed alternating trail.  Delete it and
repeat.  Toggling a trail removes and inserts one incidence of each colour at
every visit, hence leaves all degrees equal to two.  This proves generation.

If a support-minimal alternating circuit repeats a vertex, cutting at two
visits gives a proper nonempty alternating subcircuit, a contradiction.
Thus a minimal circuit is a simple even cycle (or two parallel edges).
\(\square\)

### Corollary 2.1a (one global Euler packet)

If the red/blue symmetric-difference support is connected, then all of its
edges can be ordered as one closed alternating Euler trail.  Toggling that
entire trail is therefore one valid global factor switch.  This does **not**
assert that the trail is support-minimal.

Indeed, start with the circuit decomposition in Theorem 2.1.  Connectedness
implies that, unless only one circuit remains, two circuits share a vertex.
Cross the two red--blue incidence pairings at that vertex to splice those
circuits into one alternating circuit, and iterate.

### Incidence-kernel form

Let `B` be the ordinary vertex--edge incidence matrix of `Mbar_k`.  A signed
vector

\[
 z\in\{-1,0,1\}^{E(\overline M_k)}                       \tag{2.3}
\]

is a raw exact switch from `F_0` precisely when

\[
 Bz=0,\qquad
 z_e=-1\Rightarrow e\in F_0,\qquad
 z_e=+1\Rightarrow e\notin F_0.                          \tag{2.4}
\]

Then `1_(F_0)+z` is a binary spanning 2-factor.  Every such `z` is a
sign-compatible sum of the alternating circuits in Theorem 2.1.

The lower-vertex rows of (2.4) are essential.  Working only with the
contracted upper Johnson graph preserves upper degree, but can lose the
one-choice-per-lower-colour ledger.

### Contracted direct-hybrid test

Suppose two contracted coloured factors choose, for every changed lower
colour `c`, an old Johnson edge `e_c` and a new edge `f_c`.  Let

\[
 \partial e\in\mathbb Z^{V_U}
\]

be its upper-endpoint incidence vector, counting a loop twice, and put

\[
 \Delta_c=\partial f_c-\partial e_c.                     \tag{2.5}
\]

Switching exactly a set `S` of the changed colours produces another raw
degree-two coloured factor if and only if

\[
 \sum_{c\in S}\Delta_c=0.                                \tag{2.6}
\]

Therefore the direct contracted overlay is genuinely one indivisible
switch only if

\[
 \{x\in\{0,1\}^{C_*}:\Delta x=0\}
   =\{0,\mathbf1\}.                                      \tag{2.7}
\]

Connectedness of the red/blue support graph does **not** imply (2.7).  The
expanded alternating-cycle theorem is still more flexible: switching one
inclusion-edge circuit may mix one old and one new incidence at a lower
necklace, creating a third contracted Johnson choice which occurs in neither
endpoint factor.

Here is a concrete abstract warning that connected support is insufficient.
On vertices `1,...,6`, take

\[
 F_0=(1,2,3,4,5,6,1),\qquad
 F_1=(1,4,3,5,2,6,1).                             \tag{2.7a}
\]

Their exclusive red/blue support is connected, but it is the disjoint sum of
the two balanced packets

\[
 \{12,45\}_{\rm red}\leftrightarrow\{14,25\}_{\rm blue},
 \qquad
 \{23,56\}_{\rm red}\leftrightarrow\{26,35\}_{\rm blue}. \tag{2.7b}
\]

Give the two old/new pairs in each displayed packet their own lower colours.
The first proper packet already changes `F_0` into the Hamilton cycle
`(1 4 3 2 5 6 1)`.  Thus even connected spanning support can have a proper
colour-closed binary-kernel switch.

### Theorem 2.2 (exact coherent direct-switch group)

There is a complementary exact classification when switches are restricted
to the directed darts of two displayed quotient Hamilton cycles.

Orient the cycles `F_0,F_1`.  Let

\[
 \sigma_j:V_U\to V_U
\]

be their successor permutations after contracting lower vertices, and let

\[
 \chi_j:V_U\to C
\]

send each tail to the lower colour of its outgoing dart.  Each `chi_j` is a
bijection.  Define

\[
 \pi=\sigma_1^{-1}\sigma_0,qquad
 \kappa=\chi_1^{-1}\chi_0,qquad
 \Gamma=\langle\pi,\kappa\rangle.                        \tag{2.8}
\]

For `S subseteq V_U`, take the outgoing dart of `F_1` at tails in `S` and
the outgoing dart of `F_0` elsewhere.  The result is a directed one-in,
one-out, one-of-each-colour cycle cover if and only if

\[
 \pi(S)=S=\kappa(S),                                     \tag{2.9}
\]

equivalently, `S` is a union of `Gamma`-orbits.  It is one quotient Hamilton
cycle if and only if its mixed successor permutation is one cycle.

If `alpha_j(v)` is the voltage of the chosen outgoing dart at `v`, its total
voltage is

\[
 v_S=v_0+\sum_{v\in S}
       \bigl(\alpha_1(v)-\alpha_0(v)\bigr)\pmod k.        \tag{2.10}
\]

Thus transitivity of `Gamma` on the effective noncommon tails is a sharp
obstruction to every proper coherent tailwise direct switch.  This theorem
does not classify the more general alternating inclusion-edge switches of
Theorem 2.1, which may create mixed choices.

#### Proof

Outdegree one is automatic.  For a target `w`, let
`u_j=sigma_j^(-1)(w)`.  Its mixed indegree is one exactly when

\[
 \mathbf1_S(u_1)=\mathbf1_S(u_0).
\]

Since `u_1=pi(u_0)`, this is `pi(S)=S`.  Repeating the same argument on the
unique tails carrying a fixed lower colour gives `kappa(S)=S`.  These two
invariances are equivalent to being a union of `Gamma`-orbits.  The
Hamilton and voltage assertions follow from the mixed successor map and
termwise replacement in the voltage sum.  \(\square\)

## 3. Connectivity and voltage are extra global gates

An alternating toggle preserves the central owner ledgers, but it need not
preserve quotient connectivity.  The new 2-factor can split into several
cycles.

Choose a section of the cyclic cover and give every directed inclusion dart
`a` its voltage `alpha(a) in Z_k`, with

\[
 \alpha(\bar a)=-\alpha(a).                              \tag{3.1}
\]

For oriented quotient 2-factors, let `x_a` be their directed incidence
vectors.  If `x'` is another directed 2-factor, then

\[
 v(x')-v(x)
 =\sum_a\alpha(a)(x'_a-x_a)\pmod k.                      \tag{3.2}
\]

Thus directed alternating-circuit charges add exactly.  Nevertheless the
terminal object is one physical Hamilton cycle only when

1. the switched quotient 2-factor is connected; and
2. its recomputed voltage is a unit modulo `k`.

Neither condition follows from (2.4).  Formula (3.2) applies after coherent
orientations have been chosen; reversing the terminal cycle negates its
voltage and does not change primitivity.

## 4. Exact segment rethreading theorem

Let `T` and `T'` be the physical upper Johnson Hamilton cycles obtained by
contracting two connected unit-voltage factors.  Let `b` be the number of
lower necklace colours at which their contracted Johnson choices differ.
Then each cycle loses and gains exactly `b` quotient Johnson edge orbits,
hence

\[
 e=kb                                                       \tag{4.1}
\]

physical edges.

### Theorem 4.1 (global segment normal form)

If `b>0`, the common physical graph

\[
 H=E(T)\cap E(T')                                         \tag{4.2}
\]

is exactly a disjoint union of `e=kb` paths, allowing isolated vertices as
zero-edge paths.  The new Hamilton cycle `T'` is obtained by independently
orienting these same retained paths and joining their `2e` ports with the
`e` inserted seams in one cyclic order.

Equivalently, after contracting the retained paths, the inserted seams form
a connected 2-factor on the port quotient.  Connectivity of this port
factor is necessary and sufficient for the rethreading to be Hamiltonian.
The identical quotient-scale statement has `b` retained path components;
the physical lift has `kb`.

#### Proof

The old Hamilton cycle has `W` vertices and `W-e` common edges.  A proper
subgraph of one simple cycle has no cycle component: a cycle component would
already use both old incidences at each of its vertices and hence would be
the whole old cycle, contrary to `b>0`.  Thus `H` is a forest of paths.  A
forest on `W` vertices with `W-e` edges has exactly `e` components.

At every internal vertex of a common path, both old incidences remain, so
the new cycle must traverse that path intact, in one of its two orientations.
Only the ports can be rejoined.  The final assertion is immediate after
contracting the paths.  \(\square\)

This theorem explains why a switch with a small edge ledger can still change
chronology globally: it is a permutation and reversal of retained segments,
not merely a local edit near their original locations.

## 5. Exact decoration equations

Write the directed physical Johnson cycle as

\[
 T_{i+1}=T_i-\{a_i\}+\{b_i\},\qquad i\pmod W.             \tag{5.1}
\]

### 5.1 Residence four

A coordinate inserted by edge `i` has a run of length `t` precisely when
its first later deletion is on edge `i+t`.  Therefore

\[
 \text{residence at least four}
 \quad\Longleftrightarrow\quad
 b_i\ne a_{i+t}\qquad(1\le t\le3)                       \tag{5.2}
\]

for every `i`.  Perfect lower-q1 rainbow makes the `t=1` inequality
automatic: if `b_i=a_(i+1)`, then

\[
 T_i\cap T_{i+1}=T_{i+1}\cap T_{i+2},                   \tag{5.3}
\]

repeating a lower colour.

For a maximal cyclic 1-run `R=T_(s+1),...,T_(s+ell)`, include both bracket
transitions and call

\[
 \operatorname{span}(R)=\{e_s,e_{s+1},\ldots,e_{s+\ell}\} \tag{5.4}
\]

its closed edge span.  Reversal preserves the word `0 1^ell 0`.

### Lemma 5.1 (residence switch criterion)

Let `D^-` and `D^+` be the deleted and inserted physical seams.  The switched
cycle is residence-four if and only if

1. every old run of length at most three has
   `span(R) cap D^- != empty`; and
2. no new-seam collar contains a new run of length at most three.

After item 1, every new short run must use an inserted seam, so item 2 is
checked entirely within edge radius four of `D^+`.  This statement includes
multiple nearby seams and reversed retained segments.

#### Proof

If an old short run has an all-common closed span, Theorem 4.1 retains that
path, possibly reversed, and the same short run survives.  Conversely, after
all old short spans are hit, any short run wholly inside a retained segment
would also have been an old short run.  Hence every remaining possible
defect crosses an inserted seam.  \(\square\)

### 5.2 Lower q2

Under (5.2),

\[
 Q_i=T_i\cap T_{i+1}\cap T_{i+2}
    =T_i\setminus\{a_i,a_{i+1}\},\qquad |Q_i|=r-2.       \tag{5.5}
\]

Let `c_2(S)` count `T'` triples lying wholly inside retained common segments
and having intersection `S`.  Let `b_2^+(S)` count triples using at least one
inserted seam and having intersection `S`.  Then exactly

\[
 L_{T'}^{(2)}(S)=c_2(S)+b_2^+(S).                        \tag{5.6}
\]

Thus q2 is complete if and only if the right side is positive for every
rank-`r-2` target.  If the old cycle was q2-complete, the vulnerable targets
are exactly those whose every old witness crossed a deleted seam, and each
needs a new boundary witness.

For one isolated new seam `A|B`, the two boundary triples are

\[
 \operatorname{pred}(A)\cap A\cap B,qquad
 A\cap B\cap\operatorname{succ}(B).                      \tag{5.7}
\]

Adjacent seams are handled by enumerating the distinct length-two paths
containing at least one new seam; (5.6) automatically avoids double counting.

### 5.3 Upper shadows

For every upper target `U`, let `c_U` count witnesses whose entire vertex
interval lies inside one retained segment, and let `b_U^+` count new
witnesses crossing at least one inserted seam.  Then

\[
 U\text{ is covered in }T'
 \quad\Longleftrightarrow\quad c_U+b_U^+>0.              \tag{5.8}
\]

If the old cycle was upper-complete, preservation is therefore equivalent
to supplying a new seam-crossing witness for every target all of whose old
witnesses crossed deleted seams.  If the old cycle had holes, those holes
also require new seam-crossing witnesses.

There is an exact finite segment algebra for (5.8).  For each oriented
retained segment `P`, store

* its total union `Tot(P)`;
* all nonempty prefix and suffix unions, with their lengths; and
* all internal interval unions `Int(P)`.

For concatenated segments `A*B`,

\[
\begin{aligned}
 \operatorname{Tot}(A*B)
   &=\operatorname{Tot}(A)\cup\operatorname{Tot}(B),\\
 \operatorname{Pref}(A*B)
   &=\operatorname{Pref}(A)\cup
     \{\operatorname{Tot}(A)\cup p:p\in\operatorname{Pref}(B)\},\\
 \operatorname{Suff}(A*B)
   &=\operatorname{Suff}(B)\cup
     \{s\cup\operatorname{Tot}(B):s\in\operatorname{Suff}(A)\},\\
 \operatorname{Int}(A*B)
   &=\operatorname{Int}(A)\cup\operatorname{Int}(B)\cup
     \{s\cup p:s\in\operatorname{Suff}(A),\ p\in\operatorname{Pref}(B)\}.
                                                               \tag{5.9}
\end{aligned}
\]

Reversal exchanges prefix and suffix signatures and preserves internal
unions.  Multiplying (5.9) in the new cyclic segment order, including the
wrap suffix--prefix products and restricting to intervals of length at most
`W`, computes every upper shadow exactly.

Consequently fixed-width shadows are confined to bounded seam collars, but
unrestricted upper interval unions genuinely depend on the global segment
order.

For completeness, at every fixed depth `q` the exact signed load ledger is
seam-local.  For upper q1,

\[
 \lambda'_1(U)=\lambda_1(U)-d^-_U+d^+_U,                 \tag{5.10}
\]

where `d^-_U,d^+_U` count deleted and inserted seams of union colour `U`.
More generally, common `q`-edge windows cancel after allowing segment
reversal, and only windows meeting a seam change.  For `1<=q<W`, one seam
lies in exactly `q` cyclic `q`-edge windows, so `b` quotient seam orbits
create at most `qb` new quotient-window occurrences, before deduplicating
multi-seam windows.
There is no bounded-influence analogue for unrestricted upper intervals:
one seam combines arbitrarily long suffix and prefix signatures in (5.9).

### 5.4 Exact cut survival

Let the final cyclic carrier be upper-complete.  For an upper target `U`, let
`W(U)` be its family of *based* cyclic witness intervals: a start together
with a vertex length between one and `W`.  Let `E(I)` be the internal cycle
edges crossed by that based interval; in particular a length-`W` interval
crosses `W-1` edges and remembers its omitted boundary edge.  Define its
mandatory cut set

\[
 M(U)=\bigcap_{I\in\mathcal W(U)}E(I).                    \tag{5.11}
\]

Cutting cycle edge `c` preserves `U` if and only if `c notin M(U)`.  Hence a
single cut preserves every upper target if and only if

\[
 c\notin\bigcup_U M(U).                                   \tag{5.12}
\]

Indeed, a witness survives precisely when it does not cross the cut.  This
is the exact last-witness cut condition required after the cyclic switch
theorem; cyclic completeness alone does not imply that the union in (5.12)
is proper.

## 6. Decorated global switch theorem

### Theorem 6.1 (necessary and sufficient terminal switch conditions)

Let `F_0` be an MMM quotient factor and let `z` be a sign-compatible sum of
alternating circuits as in (2.4).  Put `F=F_0+z`.  Its physical upper lift is
a rotation-symmetric Hamilton carrier with

* residence at least four;
* complete lower q2 support; and
* complete upper interval support at every rank

if and only if all of the following hold:

1. `F` is one quotient cycle;
2. its voltage is a unit modulo `k`;
3. the two residence conditions of Lemma 5.1 hold;
4. (5.6) is positive for every physical rank-`r-2` target; and
5. (5.8), equivalently the cyclic segment product (5.9), is positive for
   every physical upper target.

Because the terminal object is rotation-invariant with unit voltage, items
4--5 may be checked on the **actual** translation orbits of the targets.
For composite `k`, noncentral orbits need not have size `k`.

Conversely every rotation-symmetric carrier with those three decorations is
obtained from `F_0` by such a sum `z` and satisfies items 1--5.

#### Proof

Theorem 2.1 proves completeness of the raw alternating switch space.
Connectedness and unit voltage give one physical Hamilton lift.  Lemma 5.1,
(5.6), and (5.8) are exact identities for the three decorations.  The
converse follows by taking the symmetric difference with `F_0` and applying
Theorem 2.1.  \(\square\)

The theorem is constructive as an interface, but not an existence proof:
the hard problem is to choose one common sum of alternating circuits that
satisfies all five terminal conditions.

## 7. A 38-orbit lower bound for canonical k15 repair

Now put

\[
 k=15,\qquad r=8,\qquad N=429,\qquad d=3.                \tag{7.1}
\]

The audited published shift-one MMM carrier has

* 550 missing physical rank-nine upper targets;
* 550 missing physical rank-six q2 targets; and
* 1,980 cyclic residence defects, all of lengths two or three.

### Lemma 7.1 (rank-six/rank-nine orbit inventory)

The action of `C_15` on either rank 9 or rank 6 has exactly

\[
 333\text{ orbits of size }15,qquad
 2\text{ orbits of size }5.                              \tag{7.2}
\]

Every invariant missing family of size 550 in either rank therefore consists
of exactly

\[
 36\text{ full orbits and both short orbits},             \tag{7.3}
\]

for a total of 38 missing target orbits.

#### Proof

A rank-nine set can have stabilizer order three, but not order five or
fifteen.  Burnside gives

\[
 \frac1{15}\left(\binom{15}{9}
       +2\binom53\right)=335                              \tag{7.4}
\]

orbits.  If `a` and `b` are the numbers of size-15 and size-5 orbits, then

\[
 15a+5b=5005,\qquad a+b=335,
\]

so `(a,b)=(333,2)`.  Complementation gives rank six.  For an invariant
550-set family, `15a'+5b'=550` with `0<=b'<=2`; reduction modulo 15 forces
`b'=2`, then `a'=36`.  \(\square\)

### Lemma 7.2 (upper rank nine is already an edge gate)

If a consecutive interval of rank-eight Johnson vertices has union `U` of
rank nine, then every adjacent pair inside that interval has union `U`.
Consequently a rank-nine target is covered by an arbitrary consecutive
interval if and only if it is the union colour of some Johnson edge.

#### Proof

The interval has at least two vertices.  The union of any adjacent Johnson
pair has rank nine and is contained in `U`, hence equals `U`.  The converse
is immediate.  \(\square\)

### Theorem 7.3 (global-support obstruction)

Let `F'` be any rotation-invariant rainbow Johnson Hamilton carrier which is
obtained from this canonical carrier by changing `b` lower-necklace choices.
If `F'`

1. is residence-four;
2. covers every rank-six q2 target; and
3. covers all upper targets,

then

\[
 \boxed{b\ge38}.                                         \tag{7.5}
\]

Equivalently, its contracted quotient symmetric difference has at least 76
Johnson edge-orbits, and it changes at least `38/429` of the lower-colour
choices.

#### Proof

The 38 missing rank-nine target orbits in Lemma 7.1 have no old edge witness.
By Lemma 7.2 each must be supplied by a newly inserted quotient Johnson edge.
One inserted edge orbit has one union orbit, so `b>=38`.

For comparison, the other two gates independently give the weaker bounds

\[
 b\ge33\quad\text{(residence)},\qquad
 b\ge19\quad\text{(lower q2)}.                            \tag{7.6}
\]

Indeed the 1,980 short runs form `1980/15=132` free run orbits.  Index a run
by its unique insertion edge.  A deleted quotient edge can lie in the closed
span only of runs starting at one of the preceding three edges or at itself,
so it hits at most four blocker orbits.  Hence `b>=ceil(132/4)=33`.

The 550 missing q2 targets form 38 rank-six orbits.  A newly inserted
quotient edge changes the centered q2 motif only at its two endpoints, hence
can introduce at most two missing q2-orbit witnesses.  Thus
`b>=ceil(38/2)=19`.  The upper bound `b>=38` dominates.  \(\square\)

This rules out every single local `C4`, `C6`, `C8`, or other packet, and
every compound packet, whose **total** contracted support changes at most 37
lower choices.  It does not rule out a 38-orbit or larger compound switch,
nor a route through intermediate factors.

## 8. What the known k11 comparison actually proves

The stored comparison reports:

| Quotient factors | Shared choices | Changed lower colours | Contracted symmetric difference | Reported upper-support components |
|---|---:|---:|---:|---:|
| published MMM shift-one vs fresh `equi2_k11_rnd34` | `1/42` | `41/42` | 82 edges | one, spanning all 42 vertices |
| fresh `equi2_k11_rnd34` vs `D^3(sigma_sat_k11_465)` | `0/42` | `42/42` | 84 edges | one, spanning all 42 vertices |

The second row is frozen and independently recomputed.  The first retains
the live-download provenance caveat of the MMM baseline.

Independently of that comparison, the stored endpoint
`equi2_k11_rnd34.json` is locally certified to have 42 quotient choices, one
per lower orbit, one Hamilton lift, directed voltage `2 mod 11`, residence at
least four, and no upper or lower q2/q3 holes.  Thus its decoration is real;
only its exact overlay with the dynamically downloaded MMM endpoint has the
stated provenance limitation.

These facts prove two genuinely global statements.

1. A direct switch to the displayed target changes respectively 41 and 42
   of the 42 lower choices.  By Theorem 4.1, the corresponding physical
   rethreadings cut respectively `11*41=451` and `11*42=462` seams.  At
   quotient scale the retained graphs have respectively 41 components
   (one common edge and 40 isolated vertices) and 42 components (all
   isolated); their physical lifts have 451 and 462 components.
2. The exclusive contracted upper-edge support has one connected component
   spanning every quotient vertex, so it cannot be split by taking unions
   of its ordinary connected support components.

More exactly, in the first row the two endpoints of the sole common edge
have exclusive-overlay degree two and the other 40 vertices have degree
four.  Its reported connected support has cyclomatic number
`82-42+1=41`.  In the second row the exclusive overlay is 4-regular on all
42 vertices and has cyclomatic number `84-42+1=43`.  Red and blue degrees
agree everywhere, so connectedness gives an
alternating Euler tour using every changed edge by Corollary 2.1a (applied
to the contracted direct overlay).  The full direct difference is therefore
one valid quotient-global Euler packet.

They do **not** prove that the direct difference is one support-minimal
alternating circuit.  The function named `alternating_components` in
`scratch/compare_knuth_and_good_quotient.py` computes ordinary connected
components using only upper quotient endpoints.  It neither expands the
lower incidence vertices nor tests (2.7).  A connected balanced overlay can
contain proper alternating circuits, and a lower-vertex circuit switch can
create mixed Johnson choices absent from both direct endpoints.

The audit required depends on the intended indivisibility claim:

* direct endpoint-hybrid indivisibility is **exactly** the binary-kernel
  condition (2.7);
* raw inclusion-support minimality requires the support-minimal
  sign-compatible circuits after expanding both shores; and
* decorated indivisibility requires checking every proper sign-compatible
  circuit **sum** for connectivity, unit voltage, residence, q2, and upper
  support.  Failure of each atom separately would not rule out a successful
  compound sum.

Even such an audit would not rule out a chain of small switches using choices
outside the direct overlay.  What is already proved is that both known good
`k=11` endpoints are quotient-global rethreadings of the displayed baseline,
not bounded direct edits.

## 9. Exact remaining symmetric-carrier theorem

For the canonical `k=15` MMM factor `F_0`, the precise unresolved symmetric
carrier statement is:

> Find a sign-compatible sum `z` of alternating circuits in
> `Mbar_15` whose support changes at least 38 lower necklaces, such that the
> terminal factor `F_0+z` is connected, has unit voltage, passes the
> residence criterion (5.2), has positive q2 loads (5.6) on every actual
> rank-six orbit, and has complete upper segment signature (5.8)--(5.9).

This is necessary and sufficient for a decorated rotation-symmetric carrier
with the requested three gates.  A coefficient-one contiguous-OR theorem
would still require a cut retaining the physical upper witnesses and one
exact common lower compiler word; neither is inferred here.

The positive algebraic theorem is that alternating circuits generate every
raw owner-exact symmetric factor.  The sharp obstruction is that the known
canonical `k=15` factor cannot be decorated by any switch of total support at
most 37 lower choices, while the existing `k=11` comparison does not yet
certify circuit-minimality despite its spanning connected overlay.
