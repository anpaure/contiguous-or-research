# Joint occurrence Pareto cuts and the exact downstream port state

Date: 2026-07-31  
Status: exact dimension-uniform occurrence theorem, conditional port-Hall
theorem, and hash-bound finite censuses; no `K17` word is claimed

## 1. One selector, two debts

Let the physical trace edges be partitioned into occurrence fibres

\[
                         E=\mathbin{\dot\bigcup}_Z E_Z,
\]

and let a transversal `S` retain exactly one member of every `E_Z`.  Write
`E_Z^uniq` for the occurrences whose parent upper union has no other
physical provider, and put

\[
                         u_Z=|E_Z^{\rm uniq}|.
\]

The deleted internal upper-provider debt is

\[
 D_{\rm up}(S)
 =\sum_Z\bigl(u_Z-|S\cap E_Z^{\rm uniq}|\bigr)
 =B_{\rm up}+\eta(S),                              \tag{1.1}
\]

where

\[
 B_{\rm up}=\sum_Z(u_Z-1)^+,
 \qquad
 \eta(S)=|\{Z:u_Z>0,\ S\cap E_Z^{\rm uniq}=\varnothing\}|. \tag{1.2}
\]

Thus `D_up` in this note always means deleted **upper-unique internal
providers**, not final child holes.  Equality `D_up=B_up` holds exactly when
the selected occurrence is upper-unique in every positive-`u_Z` fibre.

Let `P_min` be the minimum-parent-run packets.  In the flat odd-diamond
shore a packet survives internally precisely when all of its physical trace
edges are retained, so

\[
 D_{\rm res}(S)
 =\sum_{P\in\mathcal P_{\min}}[P\subseteq S].       \tag{1.3}
\]

Equations (1.1) and (1.3) use the same one-hot variables.

## 2. A general provider-face Pareto cut

Let

\[
 F_0=\{e:E_{Z(e)}=\{e\}\}
\]

be the occurrences forced by singleton fibres.  For every fibre with
`u_Z=1`, let `p_Z` be its sole upper-unique occurrence, and put

\[
 F_\uparrow=F_0\cup\{p_Z:u_Z=1\},
 \qquad
 J=\{p_Z:u_Z=1,\ |E_Z|>1\}.                       \tag{2.1}
\]

Every upper-floor transversal contains all of `F_up`.  Define the
conditional packet family and its maximum sacrificable incidence by

\[
 \mathcal H_\uparrow=\{P\in\mathcal P_{\min}:P\subseteq F_\uparrow\},
 \qquad
 \Delta=\max_{e\in J}|\{P\in\mathcal H_\uparrow:e\in P\}|. \tag{2.2}
\]

### Theorem 2.1 (provider-face Pareto cut)

Every occurrence transversal satisfies

\[
 \boxed{
 D_{\rm res}(S)
 \ge |\mathcal H_\uparrow|-\Delta\bigl(D_{\rm up}(S)-B_{\rm up}\bigr).}
                                                               \tag{2.3}
\]

In particular, every upper-provider minimizer has at least
`|H_up|` surviving minimum-run packets.

#### Proof

Singleton-fibre edges in `F_0` belong to every transversal.  If `u_Z=1`,
the edge `p_Z` is selected unless that fibre contributes one unit to
`eta(S)` in (1.2).  A singleton `u_Z=1` fibre cannot be sacrificed, while
choosing a nonunique occurrence in a `u_Z>=2` fibre pays one unit of `eta`
but removes no edge of `F_up`, because no individual occurrence of such a
fibre was placed in (2.1).

Consequently at most `eta(S)` members of `J` can be absent from `S`.  Every
packet in `H_up` not incident with one of those absent edges is still wholly
contained in `S`.  One absent edge destroys at most `Delta` members of
`H_up`, so at least `|H_up|-Delta eta(S)` conditional packets survive.
Substitute (1.1).  \(\square\)

This proof also shows the sharper set-function form.  If `A(S)` is the set
of sacrificed non-singleton `u_Z=1` fibres and

\[
 c(A)=|\{P\in\mathcal H_\uparrow:P\cap\{p_Z:Z\in A\}\ne\varnothing\}|,
\]

then

\[
              D_{\rm res}(S)\ge|\mathcal H_\uparrow|-c(A(S)),
 \qquad |A(S)|\le\eta(S).                           \tag{2.4}
\]

The coarse linear cut (2.3) is the degree bound
`c(A)<=Delta|A|`; (2.4) is the exact finite coverage oracle.

## 3. Exact finite specialization

The optimization-free literal audit gives:

\[
\begin{array}{c|rr}
 &\text{current }6390+45&\text{octahedral }r2\\ \hline
B_{\rm up}&505&405\\
\min_S D_{\rm res}(S)&180&150\\
|F_0|&3630&3630\\
|F_\uparrow|&4275&4365\\
|J|&645&735\\
|\mathcal P_{\min}|&1425&1350\\
|\{P:P\subseteq F_0\}|&165&135\\
|\mathcal H_\uparrow|&315&330\\
\Delta&2&2.
\end{array}                                                     \tag{3.1}
\]

The `315` packets are exactly `21` per old coordinate; the `330` packets
are exactly `22` per old coordinate.  In all `1425` current and all `1350`
octahedral packets, the four physical edges belong to four distinct
`Z`-fibres.  Hence there is no duplicated-literal loophole.  The complete
degrees of the sacrificable `u_Z=1` fibres into `H_up` are

\[
 \begin{array}{c|cc}
 \text{degree}&\text{current}&\text{octahedral}\\ \hline
 0&510&510\\
 1&105&180\\
 2&30&45.
 \end{array}                                                    \tag{3.2}
\]

In particular no selected nonunique replacement can destroy more than two
of the conditional packets: it changes one fibre choice, and that fibre's
sole upper-unique edge has conditional packet degree at most two.  Choices
in `u_Z>=2` fibres may increase `eta`, but they destroy none of these
particular conditional packets.

Combining Theorem 2.1 with the separately authenticated exact residence
minima gives the two supporting cuts

\[
\boxed{
\begin{aligned}
\text{current:}\quad
 D_{\rm res}(S)&\ge
 \max\{180,315-2(D_{\rm up}(S)-505)\},\\
 D_{\rm res}(S)+2D_{\rm up}(S)&\ge1325;             \tag{3.3}\\
\text{octahedral:}\quad
 D_{\rm res}(S)&\ge
 \max\{150,330-2(D_{\rm up}(S)-405)\},\\
 D_{\rm res}(S)+2D_{\rm up}(S)&\ge1140.            \tag{3.4}
\end{aligned}}
\]

Therefore the two marginal corners are impossible:

\[
 (D_{\rm res},D_{\rm up})\ne(180,505),
 \qquad
 (D_{\rm res},D_{\rm up})\ne(150,405).             \tag{3.5}
\]

More quantitatively, the Pareto cut alone proves that a current
residence-optimal transversal has `D_up>=573`, and an octahedral
residence-optimal transversal has `D_up>=495`.  The new exact octahedral
cap-`150` optimization strengthens the latter value to

\[
       \min\{D_{\rm up}(S):D_{\rm res}(S)\le150\}=555.        \tag{3.6}
\]

Conversely an upper-optimal transversal has respectively at
least `315` or `330` residence packets.  Thus the octahedral parent improves
both separate marginals but has the larger forced residence floor on its
upper-optimal face.  This is a literal integral-correlation effect, not a
comparison of scalar profiles.

## 4. The exact conditional Hall theorem for the port flow

Fix one occurrence transversal `S` and suppose its induced macro port graph
`P(S)` is a loopless linear forest on the port-colour deck `T`.  Put

\[
 d_T(S)=2-\deg_{P(S)}(T),                            \tag{4.1}
\]

and let `U` be the pure-owner deck.  In the containment graph `G` between
`U` and `T`, a residual degree completion chooses Boolean incidences
`y_UT` satisfying

\[
 \sum_{T\subset U}y_{UT}=2,
 \qquad
 \sum_{U\supset T}y_{UT}=d_T(S).                   \tag{4.2}
\]

### Theorem 4.1 (capacitated occurrence-conditional Hall)

Assuming `sum_T d_T(S)=2|U|`, (4.2) has an integral solution if and only if

\[
 \boxed{
 2|A|\le
 \sum_{T\in\mathcal T}
 \min\bigl(d_T(S),|N(T)\cap A|\bigr)
 \quad\text{for every }A\subseteq\mathcal U.}       \tag{4.3}
\]

#### Proof

Use the network with source-to-`U` capacity two, unit `U`-to-`T`
containment arcs, and `T`-to-sink capacity `d_T(S)`.  For a fixed source-side
owner set `A`, minimizing a cut over whether each `T` lies on the source or
sink side contributes respectively `d_T(S)` or `|N(T) intersection A|`.
The
minimum contribution is their minimum, giving (4.3).  Max-flow/min-cut and
integrality prove the equivalence.  \(\square\)

Hall feasibility does not imply one connected port cycle.  Let
`Pi(S)` be the component partition of the macro forest.  For every pure
owner `U`, introduce a Boolean variable

\[
 z_{U,\{T,T'\}},\qquad T\ne T',\quad T,T'\subset U,
\]

meaning that the two chosen facets of `U` are `T,T'`.  A connected
completion exists exactly when

\[
\begin{aligned}
 \sum_{\{T,T'\}\subset N(U)}z_{U,\{T,T'\}}&=1
 &&(U\in\mathcal U),\\
 \sum_{U,\{T,T'\}\ni T}z_{U,\{T,T'\}}&=d_T(S)
 &&(T\in\mathcal T),                                  \tag{4.4}\\
 \sum_{U,\,|\{T,T'\}\cap W|=1}z_{U,\{T,T'\}}&\ge1
 &&\left(\varnothing\ne W=\bigcup\mathcal C'
          \ne\mathcal T,\ \mathcal C'\subseteq\Pi(S)\right).
\end{aligned}
\]

Indeed only unions of macro components are not already crossed by a macro
edge.  The last rows say that every proper component cut is crossed by a
pure-owner edge.  With all degrees equal to two, connectedness makes the
completed graph one cycle.

For topology alone, the weakest exact quotient of the macro port graph is

\[
                         (d(S),\Pi(S)).              \tag{4.5}
\]

The degree rows and Hall inequalities use `d`; the connected cut rows use
only `Pi`.  The full internal edge set of a linear-forest component is not
needed downstream.  The demand vector alone is insufficient: on four port
vertices, the forests `{12,34}` and `{13,24}` have the same degrees.  If the
only completion is `{13,24}`, the first union is connected while the second
is two doubled components.

## 5. Weakest joint regenerative export

The exact occurrence state relevant to the later stages is the quotient

\[
 \boxed{
 \Sigma(S)=
 \bigl(
   \mathcal R(S),\mu^{\rm int}_S,d(S),\Pi(S),\Lambda(S)
 \bigr),}                                             \tag{5.1}
\]

where

* `R(S)={P:P subseteq S}` is the occurrence-labelled surviving run-packet
  family;
* `mu_int_S(Y)=|{e in S:U_e=Y}|` is the complete labelled internal
  parent-upper load vector (the deleted upper-unique set is only one
  projection of this vector);
* `(d(S),Pi(S))` is the exact topological port signature from (4.5); and
* `Lambda(S)` is the full occurrence-labelled open-stub collar: endpoint
  set, shore/tag, fixed neighbouring endpoint and allowed pure-owner
  incidences, from which every upper turn created by a completion is
  computed.

Relative to run compensation, immediate parent-upper service, and connected
port completion inside this odd-diamond template, two transversals with the
same (5.1) are interchangeable.  Each coordinate of (5.1) is necessary in
general.  A scalar run count cannot say which actuator hits the survivors;
a scalar provider count cannot say which labels remain or can be recreated;
indeed all selected occurrences of a nonunique upper target may disappear,
which the globally-unique ledger does not record.  The demand vector `d`
cannot decide connectivity without `Pi`, and undecorated stubs cannot
determine upper-turn labels.  Deeper shadows and the literal compiler still
require their own chronology/cap state.

Accordingly the exact Pareto problem is an epsilon-constraint problem on one
common selector, not a product of marginal optimizers.  For each residence
or actuator budget, minimize the final labelled upper holes over `S` and
over pair variables (4.4), using the same `R(S)`, `mu_int_S`, and
`Lambda(S)`.
This enumerates all integral Pareto points; a single weighted scalarization
need not expose unsupported points.

A smallest abstract correlation witness already uses two binary fibres.
Take `E_1={a,a'}`, `E_2={b,b'}`, make `a,b` the unique-provider rewards,
and take the single residence packet `{a,b}`.  Selecting `{a,b}` gives
`(D_res,D_up)=(1,0)`; either mixed choice gives `(0,1)`.  Both marginal
minima are zero, but no common transversal attains them.  The literal cuts
(3.3)--(3.4) are the frozen-parent strengthening of this elementary gate.

## 6. Reproducibility

```text
python3 -m py_compile \
  scratch/audit_odd_diamond_joint_occurrence_pareto_20260731.py
python3 scratch/audit_odd_diamond_joint_occurrence_pareto_20260731.py
```

The audit fails closed on the two source hashes

```text
f765d52aa68810af0e4897c6881f46ecf016b86394341a97f894dc6b53058151
13c5ecaddc94bd4a240c9b2ce348f5db4508cb340658b2b0f4797b8c80472dfb
```

and writes

```text
scratch/odd_diamond_joint_occurrence_pareto_20260731.audit.json
```

with hashes of every packet and forced-edge list used in (3.1)--(3.4).
The independent occurrence-coherence replay and the exact octahedral
cap-`150`/minimum-upper witness are respectively

```text
scratch/odd_diamond_occurrence_coherence_independent_20260731.audit.json
SHA-256 592bc21769d18d827eebc3e69d690656d28f7442e91b07ae5dc2c66b5fbba6a6

scratch/k17_octa_occurrence_res150_minupper_20260731.json
SHA-256 bdf0681da82958d089a3ce684e9029b362c6986aaad7440ed399400ee5ea590e
```
