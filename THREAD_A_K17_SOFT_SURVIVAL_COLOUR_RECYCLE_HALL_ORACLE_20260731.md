# K17 soft survival, exact lower-colour recycling, and the residual Hall oracle

Date: 2026-07-31  
Lane: A, exact-equality mathematics  
Status: proved separation theorem and implementation-ready constraint system.
No K17 equality or unrestricted infeasibility claim is made.

## 0. Verdict

An accumulated hard-casualty CEGAR is logically sound if every old row is
retained and an unlimited literal replay eventually reports no hole.  A
positive-hole intermediate, however, is not an all-target certificate, and
the observed rotating casualty bank makes that formulation inefficient.  The
soft-all-old model is the sharper master because it contains an exact state
for every old source witness.  Its current primary objective is exactly
**old-source survival**, not literal final coverage: old targets recreated by
new seams are not yet credited.

There is a second, earlier obstruction.  The persisted 323-hole hard state
has 1,564 selected seams but only 1,527 distinct seam colours, hence repeat
excess 37.  Those 37 excess **fixed seam** occurrences are fatal under every
completion retaining that fixed bank.  It also has 1,061 selected seam
colours whose unique source
occurrence is currently uncut.  The latter are fatal only in the retained-
old-scaffold face: an unrestricted residual b-flow may cut an unprotected
old occurrence later.  Consequently the 323 seam assignment cannot be
frozen, but its target list remains useful as a provider/blocker pricing
seed.  In that particular artifact 312 of the 1,061 collisions hit exported
protected tails, so they are fatal on the fixed-scaffold face if that
certificate bank is frozen.

The practical theorem-faithful order is therefore:

1. jointly choose exact soft survival or literal replacement and one
   occurrence certificate for every covered upper target;
2. protect the selected certificate supports and enforce exact fixed-
   scaffold lower-colour compatibility, or final-cut recycling when the cut
   bank is already final;
3. export those protected occurrence certificates;
4. only then contract the partial chronology and invoke the residual
   Hall/rainbow completion oracle.

## 1. Authenticated live scope

The source factor is

```text
scratch/k17_pbbs_u_tripleflow_double_rainbow_q1_support7115_20260731.components
SHA-256 3f663cd2117ad6096b4cc9e6bc9d6fcf881382b4ee546dc64219bf94aafd5f2e
```

The soft producer was read remotely at SHA

```text
e6ee718e60fc113e7b24c71babb302f9f4d853443457638ddb636bd365437608
```

and uses the earlier quick4 result only as a hint.  It has exact source-
survival states for 39,388 source-covered targets and 194,424 first-hit
source-witness expressions.  The count includes the full set.  The proper
upper ledger has 39,387 targets; the full set should either be kept as a
conservative extra row or discharged separately by the final full-OR/path
condition.

That run completed only as `FEASIBLE`, not `OPTIMAL`:

```text
/home/amodo/or15/work/root_k17_fragment_seam_softall_20260731/result_hint.json
SHA-256 2c1a8557ca6d09b0c947f1f183a2b368badbb1995ac4372593e0cc5259ed4c4e
payload  45177a8c59b753be8159e722bb099635f4327ba70e4161bcd11cc4be76198245

/home/amodo/or15/work/root_k17_fragment_seam_softall_20260731/
    run_hint/candidate_round0.json
SHA-256 693ab993590301561bc69d61df1b8a5696a29127860277759763d909f8c527ce
payload  15f9b2cae3c8ae7fd9a4ae16a08b7eab2d4868b95410b04b3bcfd4f1a1133a0b
```

Its objective is 7,576,543,057,710 against best bound 21,826,797,152.  The
incumbent has 1,364 exact old-source deaths, 1,601 seams, 2,323 cuts, and
6,009 exported protected source tails.  Its 16-edge bounded replay reports
437 casualties with histogram

\[
                         11^{303}12^{131}13^3.
\tag{1.1a}
\]

There is no unlimited replay artifact.  Independently, its fixed scaffold
has 1,569 distinct seam colours, hence 32 repeated fixed-seam occurrences;
292 colour classes contain both a fixed seam and an exported
protected old tail, with five classes overlapping the two defects.  Thus 319
colour classes violate (3.4).  Its partial topology is 722 paths plus two
cycles of lengths 9 and 11.  It is therefore another useful pricing
incumbent, not a completable frozen scaffold.

The persisted hard round-4 state is

```text
/home/amodo/or15/work/root_k17_fragment_seam_setcover_allcegar_20260731/
    run/candidate_round4.json
SHA-256 2c29f2f804ab5f08d3059fe3a3455fd9c174a30e35c18f450a9132422d22f15d
payload  19cf63f1d64e70e28cd72d191ddd754ba27f43b79a8deb97c199edeccfb72251
```

It has 323 bounded-horizon replay holes, with rank histogram

\[
                         11^{224}12^{94}13^5,
\tag{1.1}
\]

1,564 seams and 2,209 cuts.  Direct successor replay gives 645 path
components and 16 cyclic owners, split into two directed cycles of lengths 3
and 13.  Thus “16 cycles” must be read as 16 cyclic owners, not 16 cycle
components.  This topology correction does not rescue the state, because the
lower-colour obstruction of Section 3 already excludes its fixed seam bank.

The producer's `partial_upper` scan stops after 16 successor edges.  Positive
hole counts from it are therefore bounded-horizon diagnostics unless an
independent unlimited-interval replay is exported.  A zero count would still
be sound.

## 2. Exact soft source-survival theorem

Let \(E(F)\) be the occurrence-labelled source edges and let
\(z_e\in\{0,1\}\) mean that edge \(e\) is cut.  For every source-covered
target \(Y\), let \(\Omega_Y\) be the complete family of its inclusion-minimal
first-hit source witness spans.  This loses no survival information: every
source interval with OR \(Y\) contains an inclusion-minimal subinterval with
the same OR.  Introduce \(w_{Y,I}\) for \(I\in\Omega_Y\) with

\[
 w_{Y,I}=1
       \quad\Longleftrightarrow\quad
 z_e=0\quad(e\in I),
\tag{2.1}
\]

and put

\[
                   a_Y=\max_{I\in\Omega_Y}w_{Y,I}.
\tag{2.2}
\]

### Theorem 2.1 (exact old-source survival)

\(a_Y=1\) if and only if \(Y\) retains an old literal interval witness after
the selected cuts.

#### Proof

An old occurrence survives inside a fragment exactly when its span contains
no selected cut.  Equation (2.1) is precisely this condition, and (2.2) is
the disjunction over all inclusion-minimal old occurrences.  The preceding
minimal-subinterval observation makes that disjunction equivalent to the one
over all old occurrences. \(\square\)

The CP-SAT reification used by the soft lane is bidirectional and exact:

```text
w -> AND(not cut[e] for e in I)
BoolOr(w, *(cut[e] for e in I))
alive[Y] = Max(w[Y,*])
```

With \(A\) candidate seam variables, put \(S=A+1\) and

\[
             P=24310S+A+1.
\tag{2.3}
\]

Then

\[
 P\sum_Y(1-a_Y)+S\sum_e z_e+\sum_a x_a
\tag{2.4}
\]

lexicographically minimizes destroyed-old-witness targets, then cuts, then
seams.  The current scaling is within exact integer and floating-point range.
Only an `OPTIMAL` result, or a bound which closes the first tier, proves
optimality.  A `FEASIBLE` line proves only an incumbent.  If residual filler
variables are added to this objective, the lower-tier variable bound, and
hence \(P\), must be recomputed.

Crucially, \(a_Y=0\) does not imply that \(Y\) is a literal final hole: a new
seam or a multi-seam interval may recreate it.  Thus (2.4) is a rigorous
conservative pricing objective, not yet the literal-hole objective.

## 3. Exact lower-colour recycling in the two completion faces

The source factor is lower-rainbow.  For each lower colour \(c\), let \(e(c)\)
be its unique source-edge occurrence.  For a candidate seam \(a\), let
\(\lambda(a)\) be its lower intersection colour.

### Theorem 3.1 (final-cut partial recycle rows)

If \(z\) is the **final** cut bank, a selected partial seam bank has neither
a repeated lower colour nor a seam colour colliding with a final-surviving
source occurrence if and only if

\[
 \boxed{
      \sum_{a:\lambda(a)=c}x_a\ \le\ z_{e(c)}
      \qquad\text{for every lower colour }c.}
\tag{3.1}
\]

#### Proof

The multiplicity of \(c\) in the partial chronology is

\[
           1-z_{e(c)}+\sum_{a:\lambda(a)=c}x_a.
\tag{3.2}
\]

It is at most one exactly when (3.1) holds.  Since \(z_{e(c)}\) is Boolean,
(3.1) also makes the seam occurrences of colour \(c\) unique. \(\square\)

For a final linear path with \(H=1,E=0\), introduce boundary variables
\(b_c\in\{0,1\}\) and strengthen (3.1) to

\[
 z_{e(c)}-\sum_{a:\lambda(a)=c}x_a=b_c,
       \qquad \sum_c b_c=1.
\tag{3.3}
\]

For an arbitrary residual b-flow, the present cut bank need not be final.
Let \(f_a\) mark a fixed selected seam and let \(h_e\) mark a source edge
which is protected and must remain through every completion.

### Theorem 3.2 (immutable fixed-scaffold face)

The fixed resources have no lower-colour multiplicity obstruction if and
only if

\[
 \boxed{
     \sum_{a:\lambda(a)=c}f_a+h_{e(c)}\le1
     \qquad\text{for every }c.}
\tag{3.4}
\]

#### Proof

The left side is exactly the immutable multiplicity of colour \(c\).
An unprotected old source edge contributes no \(h_e\), because the residual
flow may release it later.  When every currently uncut old edge is frozen,
\(h_{e(c)}=1-z_{e(c)}\), and (3.4) becomes (3.1).
\(\square\)

The hard 323 state violates (3.4) already through fixed-seam repeat excess
37.  This is the current minimal exact obstruction.  Its 1,061
currently uncut source occurrences are an additional obstruction only for
those occurrences which are frozen/protected; they are not an unrestricted
completion no-go.  No Hall calculation on the frozen 323 seam bank is
meaningful.

## 4. Literal all-target extension and the assignment \(\psi\)

For a target \(Y\), let \({\cal P}_Y\) be an occurrence-labelled provider
catalogue.  A provider \(o\in{\cal P}_Y\) records:

* every selected seam in its interval;
* every source edge which must remain uncut;
* its destination head \(h(o)\); and
* an authentication of every orientation, option-state, topology and local-
  residence condition on which this occurrence depends, plus whether its
  proof specifically requires the destination departure key.

Any such condition which is not already fixed by the catalogue must be added
as another literal in \(p_{Y,o}\); the helper's basic `Provider` class assumes
that all variable conditions have been reduced to its seam and uncut-edge
supports.

Let \(p_{Y,o}\) be the exact conjunction of these conditions and define

\[
       s_Y=\max_{o\in{\cal P}_Y}p_{Y,o},\qquad
       q_Y=\max(a_Y,s_Y).
\tag{4.1}
\]

### Theorem 4.1 (exact catalogue coverage)

\(q_Y=1\) if and only if \(Y\) has a retained source witness or one of the
literal occurrences in \({\cal P}_Y\).  Therefore

\[
           P\sum_Y(1-q_Y)+S\sum_e z_e+\sum_a x_a
\tag{4.2}
\]

is the exact literal-hole objective relative to the supplied provider
catalogue.  An all-target feasibility model must impose \(q_Y=1\) for every
target, or prove that the primary term in (4.2) has optimum zero; a positive
`FEASIBLE` incumbent is not an all-target certificate.

#### Proof

Each \(p_{Y,o}\) is bidirectionally reified as the conjunction defining one
literal occurrence.  Hence \(s_Y\) is exactly their disjunction, and \(q_Y\)
is exactly the disjunction of retained-source and catalogue occurrences.
The objective claim follows once its two lower tiers are bounded below the
coefficient of one uncovered target. \(\square\)

For an original source hole, set \(a_Y=0\).  More generally define the
service-debt state

\[
                         \delta_Y=(1-a_Y)s_Y.
\tag{4.2a}
\]

Whenever \(\delta_Y=1\), select one true provider certificate and define

\[
                         \psi(Y)=h(o).
\tag{4.3}
\]

The partition--Hall interpretation of \(\psi\) is restricted to an
authenticated **one-seam** provider catalogue: the provider has exactly one
selected seam, that seam is the unique incoming seam at \(h(o)\), and the
whole fibre is contained in its literal service set.  Under those hypotheses
\(\psi\) is exactly the assignment required by the partition--Hall theorem.
A multi-seam provider remains a valid column in (4.1), but its chronology is
a hyperarc/automaton object and cannot be reduced to the head map (4.3).

For the live multi-cut model, an old or one-seam catalogue is a safe
sufficient architecture but not necessary: a proper target can cross several
short fragments.  An unrestricted no-go requires all literal multi-seam
occurrences, or a direct final-word replay.  The current producer also keeps
only one shortest support per initial-hole target and seam; incomparable
supports must be retained for an exact provider catalogue.

## 5. Blocker-clutter separation

Let \(B\subseteq E(F)\) hit every span in \(\Omega_Y\).  Every all-target
solution satisfies

\[
 \boxed{
       \sum_{e\in B}(1-z_e)+s_Y\ge1.}
\tag{5.1}
\]

Indeed, if all edges of \(B\) are cut, every old witness is destroyed, so a
literal replacement is necessary.  Conversely, the family of (5.1) over all
inclusion-minimal blockers, together with exact provider variables, is the
exact Boolean-feasibility projection of Theorem 4.1.  No convex-hull claim is
made.

At an integral incumbent, test all old spans.  If none survives and no
provider is selected, greedily shrink the incumbent cuts to an
inclusion-minimal blocker and emit (5.1).  At a fractional node, minimize
\(\sum_{e\in B}(1-z_e)\) over transversals of the circular-interval witness
family; a value below \(1-s_Y\) separates the row.

For the authenticated frozen-650 kernel,

\[
             \tau:\quad
             1^{483}\,2^{134}\,3^{26}\,4^4\,5^2\,6^1.
\tag{5.2}
\]

Its deterministic maximal, not maximum, support-disjoint set has size 528
and distribution

\[
                       1^{436}2^{81}3^{10}4^1.
\tag{5.3}
\]

These supports yield 528 parallel blocker rows and the valid aggregate

\[
 \sum_{Y\in I}\sum_{e\in B_Y}(1-z_e)
       +\sum_{Y\in I}s_Y\ge528.
\tag{5.4}
\]

The displayed blockers use 632 distinct tails.  This is a useful packing
cut, not an Aharoni--Haxell obstruction: one seam can service many targets.
The 323 target list should likewise seed (5.1) or provider-column generation,
not become another permanent hard bank.

## 6. Residual topology, Hall, and key exchange

After fixing a partial seam bank which passes (3.4), contract its forced
directed paths.  Every forced directed cycle is a subtour obstruction and
must be opened or rethreaded before a spanning path exists.

For a fixed root, terminal, provider assignment \(\psi\), exact option
states and a **strict colour-back** filler catalogue, retain a tail-to-head
arc precisely when:

1. it is Johnson and has the prescribed source cut colour;
2. it services every target in the assigned destination fibre;
3. its option and exact residence states agree; and
4. if the destination is key-active, it is key-forward.

Call the resulting graph \(G_\psi\).  A maximum matching either saturates
the residual left shore or returns, by alternating reachability, an exact
Hall obstruction

\[
                       X\subseteq L,
              \qquad |N_{G_\psi}(X)|<|X|.
\tag{6.1}
\]

### Proposition 6.1 (fixed-catalogue residual separator)

Assume \(|L|=|R|\), the residual shores omit exactly the prescribed root and
terminal, and in the strict catalogue the tail colours are the distinct
missing colours other than the prescribed boundary colour.  Then residual
degree completion exists if and only if \(G_\psi\) has a matching saturating
\(L\).  If the admissible skeleton is acyclic, that completion is one spanning
path; otherwise degree completion additionally requires the exclusion of
every directed subtour.

#### Proof

Every legal strict completion chooses one admissible outgoing arc at each
residual tail and one incoming arc at each residual head, hence is a
saturating matching.  Conversely, a saturating matching supplies those two
degree conditions; strict colour-back and distinct tail colours supply every
required residual colour exactly once.  Hall's theorem gives (6.1) as the
exact obstruction.  After expanding contracted forced paths, the prescribed
root and terminal are the only possible path endpoints.  An acyclic degree
completion is therefore one spanning path.  In the general graph, its only
additional components can be directed cycles, which are exactly the subtours
to be excluded. \(\square\)

This is an exact ordinary Hall oracle for residual **degree completion**
because strict colour-back prescribes the colour from the tail.  It proves a
spanning path only when the admissible graph is already an acyclic skeleton;
otherwise directed subtour rows must be separated lazily.  If remote global
colour recycling is allowed, ordinary Hall is only necessary.  Write

\[
                  F_c=\sum_{a:\lambda(a)=c}f_a
\]

for the immutable fixed-seam multiplicity, and let \(z_{e(c)}\) now be the
**eventual** source-edge release variable, not the current scaffold cut.  Let
\(L^*,R^*\) be the potential residual shores, and let \(\alpha_i,\beta_j\)
be exact activation states: they equal one precisely when the eventual cuts
and fixed seams expose tail \(i\) or head \(j\) for residual completion.  The
fixed and residual seam sets are disjoint.  Conditional on exact activation
linkage, the arbitrary-recourse degree and colour rows are

\[
 \sum_j x_{ij}=\alpha_i\quad(i\in L^*),\qquad
 \sum_i x_{ij}=\beta_j\quad(j\in R^*),\qquad
 (1-z_{e(c)})+F_c+
       \sum_{ij:\lambda(ij)=c}x_{ij}+b_c=1\quad(c\in{\cal C}),
 \qquad \sum_c b_c=1,
 \qquad z_e+h_e\le1\quad(e\in E(F)).
\tag{6.2a}
\]

Here \({\cal C}\) is the whole source lower-colour palette, arcs with colours
outside it are forbidden, and \(h_e=1\) means that the old edge is protected.
The equivalences defining \(\alpha,\beta\) are part of the physical endpoint
model; omitting them leaves only a relaxation.  Thus (3.4) is the immutable
feasibility precheck, while (6.2a) actually pays every remote colour by an
eventual old-edge release.

If \(z,F,\alpha,\beta\) have first been fixed, let
\(L=\{i:\alpha_i=1\}\), \(R=\{j:\beta_j=1\}\), and define

\[
             {\cal C}_{\rm miss}=\{c:z_{e(c)}-F_c=1\}.
\]

Then the colour rows in (6.2a) reduce exactly to

\[
 \sum_{ij:\lambda(ij)=c}x_{ij}+b_c=1
       \quad(c\in{\cal C}_{\rm miss}),\qquad
 \sum_c b_c=1,
\tag{6.2b}
\]

with every residual arc of a colour outside \({\cal C}_{\rm miss}\) forced
to zero.  The remaining degree rows are
\(\sum_{j\in R}x_{ij}=1\) for \(i\in L\) and
\(\sum_{i\in L}x_{ij}=1\) for \(j\in R\).  In particular,
\(|{\cal C}_{\rm miss}|=|L|+1=|R|+1\).  Equations (6.2a) and (6.2b) are
tail/head/colour rainbow assignments, not bipartite matchings.  The helper's
fixed-palette routine implements (6.2b); an integrated arbitrary-recourse
master must use (6.2a).

There is an exact key-exchange law.  Write

\[
 t_i=c_i\cup\{\kappa_i\},
\tag{6.3}
\]

and suppose a Johnson incoming seam repairs a key-active destination \(j\).
Then
\(\kappa_j\in t_i\) and its new lower colour is

\[
 d_{ij}=t_i\cap s_j
       =t_i\setminus\{\kappa_j\}
       =(c_i\cup\{\kappa_i\})\setminus\{\kappa_j\}.
\tag{6.4}
\]

Hence

\[
                       d_{ij}=c_i
               \quad\Longleftrightarrow\quad
                       \kappa_i=\kappa_j.
\tag{6.5}
\]

Thus common-key conservation is exact only on locally colour-back,
key-active arcs.  A remote-colour seam may change the key, but (3.1) or
(6.2a) must pay its new colour against a deleted source token; (3.4) says
only that such payment has not already been made impossible by immutable
resources.  A destination with no key-requiring assigned provider is a
**key-legal** reset site; palette, topology, option-state, and residence
legality are still separate.  Safe-opening activity and key activity remain
distinct.

The 323 hard state has 645 path components and two directed cycles, on 3 and
13 owners.  If its seams had passed (3.4), freezing them would require at
least two protected cycle openings, producing 647 chains and hence 646
filler seams.  Since (3.4) fails, these numbers are topology diagnostics only,
not a residual-completion claim.

## 7. H100 integration contract

The next sound producer should use the following order.

1. At minimum add the fixed-seam uniqueness part of (3.4), and add its
   protected-old term for every exported witness edge.  Use (3.1) only when
   the master cut variables are final.  The old 650/323 fixed seam
   assignments are infeasible because of repeated seam colours; use only
   their target lists for pricing.
2. Keep the exact \(w\leftrightarrow\bigwedge\neg z\) and `alive=Max(w)`
   state for all old targets.  In a pure soft run, disable the old
   `add_retention_target` loop; otherwise hard rotation silently resumes.
3. If optimizing literal rather than source-survival holes, add complete
   provider occurrences and use \(q_Y\), not \(a_Y\), in the primary tier.
   Impose every \(q_Y=1\), or certify a zero optimum in that tier, before
   calling the result all-target.
4. Persist one selected old witness for every \(a_Y=1\), and one selected
   provider for every serviced debt.  Export their support tails.  This is
   mandatory if a later stage may add cuts; it is provenance-only if the cut
   bank is frozen.  For ordinary partition--Hall, forbid chosen providers
   outside the authenticated one-seam catalogue.  Define head activity as the
   OR of chosen key-requiring debt providers and impose key-forward on every
   selected incoming arc at an active head.  That incoming-arc universe must
   include already-fixed provider seams as well as residual filler arcs; a
   guard over residual arcs alone is incomplete.
5. Export the script, source and hint hashes; objective scales and tuple;
   predicted-dead target hash; unlimited-replay hole hash; solver status and
   best bound.  Resource termination is `UNKNOWN`, never infeasibility.
6. Open every forced cycle, then run either the strict \(G_\psi\) Hall oracle
   or the full coloured assignment (6.2a)/(6.2b), followed by exact subtour
   and terminal residence-state checks.  If eventual releases alter the
   residual shores, link every tail/head activation in (6.2a) bidirectionally
   to the final cuts and fixed seams; fixed RHS-one shore rows are then
   invalid.

The implementation helpers in

```text
scratch/threadA_k17_softall_partition_hall_oracle_20260731.py
```

encode exact survival, catalogue coverage, one-certificate export, integral
blocker separation, canonical Hall-witness extraction, one-seam \(\psi\)
restriction, chosen-provider key-activity guards, key-exchange
classification, final-cut recycling, fixed-scaffold compatibility, and the
fixed-palette and arbitrary-recourse coloured residual assignments.

## 8. Proved boundary

There is no current Hall obstruction to an authenticated soft-all-old,
lower-recyclable incumbent because neither available incumbent reaches that
face.  The minimal obstruction for the persisted 323 state is earlier and
exact: fixed-seam repeat excess 37 violates (3.4).  Of its 1,061 current
source-edge collisions, 312 already involve exported protected tails (307
additional bad classes beyond the repeated-seam classes), for 344 bad fixed-
scaffold colour classes altogether; the rest are conditional on those old
edges later being protected.  The completed soft
incumbent likewise has 32 repeated seam occurrences and 292 protected-old
collisions, in 319 bad colour classes altogether.  Both target/death lists
remain useful for column generation, but both seam assignments must be
modified or released and cannot be frozen unchanged before Hall separation.

Once a new incumbent satisfies the appropriate form of (3.1)/(3.4),
Theorems 2.1 and 4.1 together with Section 5 make every casualty rotation
globally visible.  Imposing every \(q_Y=1\), or proving zero primary loss,
prevents it.  Section 6 then gives the exact next Hall/rainbow separator.
Common-cap/compiler feasibility and the final deadline staircase remain
separate gates.
