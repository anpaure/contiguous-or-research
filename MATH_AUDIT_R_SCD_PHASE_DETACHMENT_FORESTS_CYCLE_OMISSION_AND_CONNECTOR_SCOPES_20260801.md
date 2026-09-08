# Independent audit of the SCD phase-detachment forests, the missing cycle
# row, and the two different connector scopes

Date: 2026-08-01  
Lane: R / four-row SCD C-phase detachment  
Status: exact literal replay of the saved `m=4,...,8` witnesses; explicit
smallest cycle counterexample to automatic acyclicity; exact fixed-`M_0`
connector cut; finite orientation-free connector audit for the five frozen
forests.  No residence, deeper-shadow, or compiler conclusion is claimed.

## 0. Verdict

The five saved phase-detachment assignments are sound physical central
objects.  Independently reconstructing the Greene--Kleitman chains, the
matching `M_0`, every selected option, every retained provider edge, and
the physical owner graph gives, for each `m=4,...,8`:

1. every rank-`(m+1)` upper colour exactly once;
2. pairwise distinct rank-`(m-1)` lower colours;
3. no retained-tail or retained-head collision;
4. maximum physical owner degree two; and
5. no directed or undirected cycle.

Thus each saved object is a spanning path forest with exactly
`Cat_m` components.

The phase-only CNF does **not**, however, imply item 5.  Complete
enumeration at `m=4` gives 2,252 satisfying assignments, of which seven
contain a directed owner cycle.  An explicit five-cycle is given in
Section 3.  Consequently a physical cycle replay or explicit cycle/order
constraints are mandatory.  Retained-tail safety and degree two, unlike
acyclicity, are automatic for this precise option grammar.

There are two connector models and they must not be conflated.

* In the fixed-rooted model, a connector of missing lower colour `q` must
  leave the root `q`, hence one endpoint is literally `M_0(q)`.  The exact
  `z`-endpoint cocycle gives deficiency `I_m-1` for every `m>=4`; the joint
  flexible-detachment/rooted-path model is therefore impossible.
* In the orientation-free physical model, either free endpoint of each
  component may be used after reversing that component.  This is strictly
  larger and is not covered by the fixed-`M_0` cocycle.  For each of the
  five *frozen* forests it is nevertheless infeasible: `m=4,...,7` fail
  the endpoint/colour/component-degree master even before subtour rows,
  while `m=8` has six missing colours with no legal connector and one
  isolated component.  This finite statement does not exclude another
  phase assignment or a simultaneous physical rethread.

## 1. Inputs and independent reconstruction

The authenticated model hashes are

| `m` | saved assignment SHA-256 |
|---:|:---|
|4|`182bf5e4690f0c8b625992bbcb98fe01b96edca24cc719ccee4c3c301fe54aff`|
|5|`82e2e70ebf892c07682ec1525a18cc9c125e6bdc7f7c1b955bd150c5f9c0c273`|
|6|`a5d1e7f624cb9f31e9fe6677df58f015390240e866e13f8e47a5ca515bf74e75`|
|7|`031a9755e912a0221035fa549ea9f5241bfef6e0ca1f618b84590fbfd3c93af1`|
|8|`4a6a1fd1e93ec7a56401a9294924207132ac5144a41faebbc24d8eb50ce2aa00`|

The independent source is

`scratch/r_phase_detachment_model_replay_20260801/audit_phase_detachment_models.cpp`.

It does not call the encoder's decoder.  It reconstructs the increasing
Greene--Kleitman SCD from chain bottoms, rebuilds the root-to-owner
bijection `M_0`, independently regenerates the option order, reads only
the positive model literals, restores every unused provider edge, and
then recomputes intersections, unions, degrees and components from the
literal physical endpoints.

The final source SHA is recorded in the adjacent JSON payload.  It was
compiled with `g++ -O3 -std=c++17` and run on the H100 CPU under a
90-second/512-MiB cap.  The replay took 0.32 seconds and about 12 MiB RSS.

## 2. Exact saved-witness table

In the phase column, the entries are respectively long `a` C phase,
all `a` D phases, aligned `z`, and reverse `z`.

|`m`|options|selected|retained|edges|upper distinct/missing|lower distinct/unused|components|max degree|cycles directed/undirected|phase counts|
|---:|---:|---:|---:|---:|:---|:---|---:|---:|:---|:---|
|4|38|6|9|21|21/0|21/14|14|2|0/0|0,5,0,1|
|5|262|28|28|84|84/0|84/42|42|2|0/0|0,21,0,7|
|6|1,572|120|90|330|330/0|330/132|132|2|0/0|23,61,19,17|
|7|8,704|495|297|1,287|1,287/0|1,287/429|429|2|0/0|108,222,45,120|
|8|45,698|2,002|1,001|5,005|5,005/0|5,005/1,430|1,430|2|0/0|473,814,137,578|

Every encoded error counter is zero: target multiplicity, provider
multiplicity, new-head multiplicity, new-tail multiplicity and unreleased
old head.  Every literal edge is Johnson, no physical edge is duplicated,
and both rooted indegree and rooted outdegree are at most one.

The component-size histograms, written `size:multiplicity`, are

```text
m=4: 1:4,2:3,3:3,4:4
m=5: 1:7,2:11,3:7,4:10,5:6,6:1
m=6: 1:2,2:33,3:43,4:30,5:9,6:6,7:8,8:1
m=7: 1:4,2:91,3:108,4:104,5:56,6:19,7:20,8:8,
     9:12,10:2,12:3,14:2
m=8: 1:8,2:275,3:291,4:290,5:211,6:125,7:91,8:45,
     9:34,10:23,11:8,12:8,13:7,14:3,15:3,16:2,17:2,
     18:1,19:1,20:1,21:1
```

### Proposition 2.1 (why retained-tail safety and degree two are automatic)

The original provider tails have signatures `aS` and `L`, hence contain,
respectively, `a` only or neither special coordinate.  Every second tail
created by an option has one of the forms

\[
                   zS,\qquad azR,\qquad zV.          \tag{2.1}
\]

It therefore contains `z` and cannot be an original provider tail.  The
CNF's new-tail at-most-one rows consequently imply final rooted outdegree
at most one even though no explicit retained-tail release row was written.
The old-head release clauses and new-head at-most-one rows give rooted
indegree at most one.  Since `M_0` is a bijection from roots to physical
owners, physical degree is at most two.

This proves that the retained-tail omission is benign for this grammar.
It does not prove acyclicity.

## 3. Acyclicity is not automatic

The natural owner potential

\[
                       \Phi(T)=\sum_{i\in T}i        \tag{3.1}
\]

is not monotone on the saved assignments.  The numbers of negative,
zero and positive selected/retained arrows are

\[
 (2,0,19),\ (15,0,69),\ (82,0,248),\
 (394,0,893),\ (1472,0,3533).                       \tag{3.2}
\]

Thus the canonical C-phase potential cannot audit these flexible models.

More decisively, complete `m=4` enumeration gives

\[
  2252\text{ encoded solutions}
   =2245\text{ forests}+7\text{ cyclic solutions}. \tag{3.3}
\]

There are zero retained-tail failures and zero degree failures among all
2,252 solutions.  One cyclic assignment selects variables

\[
                         2,14,18,22,26,32.           \tag{3.4}
\]

Its physical graph contains the directed five-cycle, displayed
undirected here,

\[
 a123-a234-a345-a145-a125-a123.                     \tag{3.5}
\]

The five lower colours are

\[
              a23,a34,a45,a15,a12,                  \tag{3.6}
\]

and the five upper colours are

\[
 a1234,a2345,a1345,a1245,a1235.                     \tag{3.7}
\]

They are all distinct.  The sixth selected option and the retained
background complete the remaining palette rows.  Thus (3.5) is a pure
topological counterexample satisfying every encoded phase-only row.

The correct repair is either a literal physical decoder, as used for the
five saved witnesses, or explicit lazy cycle/order constraints.  No
dimension-uniform automatic potential follows from the current rows.

## 4. Fixed-rooted connector model

Let the verified forest have directed components `P_i`, with source root
`s_i` and unused terminal lower root `q_i`.  A fixed-`M_0` connector is

\[
       q_i\longrightarrow s_j,
       \qquad M_0(q_i)\cap M_0(s_j)=q_i.             \tag{4.1}
\]

Its lower colour is automatically the private colour `q_i`.  A rooted
Hamilton path therefore needs `C-1` arcs, indegree and outdegree at most
one, and no directed subtour.

For the five frozen forests the exact port censuses are

|`m`|`C`|arcs|zero out|zero in|max bipartite matching|required|shortfall|Hall witness `|S|/|N(S)|`|
|---:|---:|---:|---:|---:|---:|---:|---:|:---|
|4|14|18|3|5|9|13|4|8/3|
|5|42|62|9|18|24|41|17|33/15|
|6|132|209|39|50|72|131|59|77/17|
|7|429|832|101|157|243|428|185|271/85|
|8|1,430|2,997|339|633|772|1,429|657|960/302|

These frozen objects fail before subtours.

There is also an all-dimensional, phase-independent cut for the joint
flexible rooted model.  Put

\[
 c=\operatorname {Cat}_{m-1},\qquad
 I_m={2m-3\choose m-3}-{2m-3\choose m-4},\qquad
 C=2c+I_m.                                           \tag{4.2}
\]

For any selected phase forest in this grammar, the number of unused lower
roots containing `z` is `C-c`, while exactly `c` component-source owners
contain `z`.  A rooted path may omit only one unused lower root.  Hence

\[
       (C-c)-1\le c                                  \tag{4.3}
\]

is necessary, and its exact deficiency is

\[
                 C-2c-1=I_m-1.                      \tag{4.4}
\]

This proves the fixed-rooted no-go for every `m>=4`, independently of the
finite solver.

## 5. Orientation-free physical endpoint model

For a physical path forest `F`, let `d_F(u)` be the degree of owner `u`
and `b(u)=2-d_F(u)` its free endpoint capacity.  Contract the `C`
components.  For every pair of owners `u,v` in different components form
a candidate connector when

\[
 |u\mathbin\triangle v|=2,qquad
 q=u\cap v\text{ is an unused lower colour},qquad
 b(u),b(v)>0.                                        \tag{5.1}
\]

This catalogue allows arbitrary component reversal and is strictly larger
than (4.1).  With one Boolean variable `x_e` per candidate, the exact
Hamilton-compatible connector system is

\[
\begin{aligned}
 &\sum_{e\ni u}x_e\le b(u) &&(u\text{ an owner}),\\
 &\sum_{e:\,q(e)=q}x_e\le1 &&(q\text{ an unused lower colour}),\\
 &1\le\sum_{e\ni K}x_e\le2 &&(K\text{ a contracted component}),\\
 &\sum_e x_e=C-1,\\
 &\sum_{e\in E(\mathcal S)}x_e\le|\mathcal S|-1
        &&(\varnothing\ne\mathcal S\subseteq[C]).          \tag{5.2}
\end{aligned}
\]

The last row is contracted graphic independence.  The preceding rows and
the total force degree sequence `1,1,2,...,2`; with the graphic row this is
one spanning path.  Distinct lower colours are explicit, while connector
upper colours may repeat.

The complete frozen catalogues are

|`m`|components|candidate edges|available/unused colours|zero components|weak components|base master verdict|
|---:|---:|---:|:---|---:|---:|:---|
|4|14|55|14/14|0|1|INFEASIBLE|
|5|42|283|42/42|0|1|INFEASIBLE|
|6|132|1,295|132/132|0|1|INFEASIBLE|
|7|429|5,440|429/429|0|1|INFEASIBLE|
|8|1,430|21,936|1,424/1,430|1|2|INFEASIBLE by inspection|

For `m=4,...,7`, the CP-SAT model containing all rows of (5.2) except the
graphic inequalities is already infeasible; hence no subtour round is
reached.  The authenticated result files are

```text
full_connector_m4.solve.json  b3d66f9960f38d3b96cba5a284e460f9e8334c6f242f1c654b8619c0b78359ab
full_connector_m5.solve.json  85d6024063545e13680f8bb2e155630b6ed1bdfe25bc03293ba3d45696491a61
full_connector_m6.solve.json  7bced973a071cc5f2046a96b1e6eed2d371e93abdc09c53064ccbfbd448de217
full_connector_m7.solve.json  b15431ea0be3336fd5c24450a6dec77b18f7995e3aa105728cb238c882b430ac
```

These four finite negative verdicts have no independent DRAT certificate;
their exact scope is the displayed finite 0--1 master.  At `m=8` no solver
is needed.  The six unusable lower colours are

```text
{1,2,4,5,7,10,z}   {1,3,4,7,8,10,z}
{3,4,5,7,8,10,z}   {2,5,6,7,8,10,z}
{2,3,4,8,9,10,z}   {1,2,4,5,7,13,z}.
```

The isolated two-owner component is

\[
 \{1,2,4,5,7,8,10,11\}
   --\{1,2,4,5,7,8,10,z\}.                         \tag{5.3}
\]

No endpoint-only connector touches it.

## 6. Audit of the joint flexible-detachment/rooted-path solver

The source

`scratch/solve_threadD_scd_detachment_hamilton_path_20260801.py`

has SHA-256

`4ba3a26b7fd94a185d70f9d49708b864e71ba5861fdc913ae216014e5affd4b7`.

Its catalogue builder has SHA-256

`d4b4b1fa56857bb73134528f44557bd969ad9ffd18d966947c5f8c93c0a30998`.

The following points are valid.

1. Every target chooses exactly one option, and every original provider is
   either retained or switched exactly once.
2. Every retained provider occurs in both combined endpoint-degree rows.
3. The original-head release implications are present.
4. Condition `M_0(q) intersection M_0(s)=q` is sufficient for a literal
   rooted Johnson connector; equal owner ranks then force symmetric
   difference two.
5. Exact indegree/outdegree with one start and one end gives one path plus
   possible directed cycles.  The strict integer order kills every such
   cycle, hence leaves one spanning path.
6. The base edges retain every upper colour exactly once.  Final exact
   outdegree uses every lower root except the end exactly once.  Connector
   upper repeats are allowed and already belong to the complete base
   upper palette.
7. Bijectivity of `M_0` transfers rooted degree at most two to physical
   owner degree at most two.

No missing retained-provider, owner-degree, palette, or connectivity row
was found within this fixed-rooted scope.

The completed path-mode verdicts are

|`m`|roots|options|connector menu|status|wall seconds|result SHA-256|
|---:|---:|---:|---:|:---|---:|:---|
|4|35|38|105|INFEASIBLE|0.008|`84572e4ba4790dd355f2f605fb66517ec01a321a6f2b60d36e8d7efdf24e104c`|
|5|126|262|504|INFEASIBLE|0.038|`43863cc1fce371dfce015bd5b85c6ef1a81b0087b693f4eb1dc1ec95bd337892`|
|6|462|1,572|2,310|INFEASIBLE|2.34|`4e349c0ce8f54c4ad201a21b117526db9b54ad713360433d9a107c7deb64d4cf`|
|7|1,716|8,704|10,296|INFEASIBLE|11.69|`e461f34b26150918c23598586415c6571a9a9bcdff7e2095dd3c8b49ebc74bf5`|
|8|6,435|45,698|45,045|INFEASIBLE|53.54|`9303b0e1e707769e8288b591ccfad77545a6922098ebe8e0446684875e16c9a9`|

The `m=9` run terminated without a JSON result, exit record, or nonempty
log.  Its status is therefore **UNKNOWN/ABORT**, not UNSAT.  Formula (4.4)
already proves the fixed-rooted no-go at `m=9`, but that mathematical fact
must not be misreported as a solver result.

### Scope correction

The joint solver does **not** choose arbitrary free physical endpoint
pairs.  It fixes the root-owner map `M_0` and insists that a connector of
colour `q` leave the endpoint `M_0(q)`.  Reversing an undirected physical
component generally changes which endpoint is assigned to the lower root
and is outside this model.  Therefore any statement that “component
reversal cannot help” must be read as **`M_0`-preserving rooted reversal**.
Unrestricted physical reversal is governed by (5.2), not by (4.4).

## 7. Exact boundary

Proved or independently replayed:

1. all five saved phase assignments are exact upper-rainbow,
   lower-injective physical path forests;
2. retained-tail safety and cap two are structural for this grammar;
3. acyclicity is not structural, with a literal `m=4` counterexample;
4. the fixed-rooted component connector has an all-dimensional `z` cut;
5. the five frozen forests also fail the larger orientation-free
   endpoint-only connector gate.

Not proved:

1. infeasibility of (5.2) over every flexible phase assignment;
2. infeasibility after simultaneous release/rethread or an enlarged ear
   grammar;
3. residence, deeper-shadow preservation, common-cap compilation, or a
   literal all-width word.

The correct constructive next object is therefore a **joint
orientation-free phase selection and connector/rethread**, or an actuator
which changes the endpoint/lower-hole ledger.  Neither the frozen-forest
port search nor the fixed-rooted `M_0` solver is that object.
