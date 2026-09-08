# A literal h=2 twin-Ferrers bank for k=17

**Date:** 2026-08-01  
**Status:** explicit local construction plus an exact protected spanning
`ML_9` factor.  The two permanent-marker shortage
in the uniform twin-bank theorem is not an obstruction at k=17: a concrete
six-owner X-bank and nine-owner U-bank use all owners and both q1 palettes
disjointly from the fourteen-owner reset packet, cover its complete
twelve-target overlap leave, and have no short internal positive run.
The combined protected `ML_9` residual factor has seven components and both
q1 palettes complete.  Global component joining, exterior residence, deeper
upper targets, and the common lower compiler remain outside this theorem.

## 1. Labels and packet leave

Partition sixteen of the seventeen coordinates as

\[
 H=\{h_1,h_2\},\quad X=\{x_1,x_2,x_3\},\quad
 C=\{c_1,c_2,c_3\},
\]

\[
 U=\{u_1,u_2,u_3\},\quad Y=\{y_1,y_2,y_3\},
 \quad\{\alpha,\delta\},                                \tag{1.1}
\]

and leave one coordinate `z` unused.  Put

\[
 B_X=H\cup C\cup Y\cup\{\alpha,\delta\},
 \qquad B_U=(H\cup X\cup C\cup U\cup Y
                    \cup\{\alpha,\delta\})\setminus U. \tag{1.2}
\]

The coefficient-one three-overlap of the reset packet misses exactly the
two six-target triangles

\[
 Z^X_{i,j}=B_X\cup X[1,i]\cup X[j+2,3],                  \tag{1.3}
\]

\[
 Z^U_{i,j}=B_U\cup U[1,i]\cup U[j+2,3],
 \qquad0\le i\le j\le2.                                 \tag{1.4}
\]

Their joint rank histogram is

\[
 10^1,11^2,12^3,13^1,14^2,15^3.                         \tag{1.5}
\]

## 2. Deterministic six-owner X-bank

Set

\[
 V_0=B_X-\{h_1\},\qquad V_1=B_X-\{h_2\}.                \tag{2.1}
\]

Define

\[
\begin{aligned}
 L_0&=V_0,\\
 L_1&=V_0-\{c_1\}+\{x_1\},\\
 L_2&=V_0-\{c_1,c_2\}+\{x_1,x_2\},                   \tag{2.2}
\end{aligned}
\]

and

\[
\begin{aligned}
 R_0&=V_1,\\
 R_1&=V_1-\{y_1\}+\{x_3\},\\
 R_2&=V_1-\{y_1,y_2\}+\{x_3,x_2\}.                   \tag{2.3}
\end{aligned}
\]

Use the owner path

\[
 \boxed{{\cal P}_X=(L_2,L_1,L_0,R_0,R_1,R_2).}          \tag{2.4}
\]

Every owner has rank nine.  Every step in (2.4) is one exchange; the
central step exchanges `h_2` for `h_1`.

### Lemma 2.1 (complete X triangle)

For every `0<=i<=j<=2`, the interval from `L_i` to `R_(2-j)` in (2.4)
has union `Z^X_(i,j)`.

#### Proof

The left subinterval has union

\[
 V_0\cup X[1,i],
\]

because `L_0` restores both deleted transport coordinates.  The right
subinterval has union

\[
 V_1\cup X[j+2,3].
\]

Since `V_0 union V_1=B_X`, their union is (1.3). \(\square\)

The six literal target masks and their zero-based witness intervals are

\[
\begin{array}{c|c|c}
(i,j)&Z^X_{i,j}&\text{interval}\\ \hline
(0,0)&63739&[2,5]\\
(0,1)&63731&[2,4]\\
(0,2)&63715&[2,3]\\
(1,1)&63735&[1,4]\\
(1,2)&63719&[1,3]\\
(2,2)&63727&[0,3].
\end{array}                                               \tag{2.5}
\]

## 3. Deterministic nine-owner U-bank

Partition `B_U` as

\[
 Q=\{h_1,c_1,c_2,\alpha,\delta\},                        \tag{3.1}
\]

\[
 {\cal L}=(y_1,y_2,y_3,h_2),\qquad
 {\cal R}=(x_1,x_2,x_3,c_3).                             \tag{3.2}
\]

For `0<=s<=4`, put

\[
 M_s=Q\cup{\cal R}[1,s]\cup{\cal L}[s+1,4].             \tag{3.3}
\]

Define

\[
\begin{aligned}
 P_0&=M_0,\\
 P_1&=M_0-\{c_1\}+\{u_1\},\\
 P_2&=M_0-\{c_1,c_2\}+\{u_1,u_2\},                    \tag{3.4}
\end{aligned}
\]

and

\[
\begin{aligned}
 S_0&=M_4,\\
 S_1&=M_4-\{c_1\}+\{u_3\},\\
 S_2&=M_4-\{c_1,c_2\}+\{u_3,u_2\}.                    \tag{3.5}
\end{aligned}
\]

Use

\[
 \boxed{{\cal P}_U=(P_2,P_1,M_0,M_1,M_2,M_3,M_4,S_1,S_2).} \tag{3.6}
\]

Every owner has rank nine.  The middle path successively exchanges the
ordered `L` coordinates for the ordered `R` coordinates, and the two outer
segments are Johnson paths by (3.4)--(3.5).

### Lemma 3.1 (complete U triangle)

For every `0<=i<=j<=2`, the interval from `P_i` to `S_(2-j)` in (3.6)
has union `Z^U_(i,j)`.

#### Proof

The complete middle geodesic has union

\[
 Q\cup{\cal L}\cup{\cal R}=B_U.
\]

It restores every coordinate deleted in (3.4)--(3.5).  The two outer
segments contribute `U[1,i]` and `U[j+2,3]`, respectively, giving (1.4).
\(\square\)

The literal targets are

\[
\begin{array}{c|c|c}
(i,j)&Z^U_{i,j}&\text{interval}\\ \hline
(0,0)&65279&[2,8]\\
(0,1)&64767&[2,7]\\
(0,2)&63743&[2,6]\\
(1,1)&65023&[1,7]\\
(1,2)&63999&[1,6]\\
(2,2)&64511&[0,6].
\end{array}                                               \tag{3.7}
\]

## 4. Exact owner and q1 certificate

Under the coordinate order

```text
h1,h2,x1,x2,x3,c1,c2,c3,u1,u2,u3,y1,y2,y3,alpha,delta,z
```

the three owner paths are

```text
packet:
47331 45287 41199 33023 33247 33695 34591
18207 17983 17535 16639 18683 22771 30947

P_X:
63630 63686 63714 63713 61681 57593

P_U:
64259 63811 63587 61543 57455 49279 49405 50397 50845
```

All 29 masks are different.

There is also a short symbolic separation proof.  Every packet owner
contains both `h_1,h_2` and exactly one of `alpha,delta`.  Every X-bank and
U-bank owner contains both seam labels, so neither bank meets the packet.
The first three X-bank owners miss `h_1`, while every U-bank owner contains
`h_1`.  The only remaining possible X/U comparison is between their
`h_2`-missing terminal profiles.  Each such X-bank owner contains a nonempty
suffix of `Y`, whereas the `h_2`-missing U-bank owners contain no `Y` label.
Thus the two banks are disjoint as well.

The lower-q1 masks are

```text
packet:
45283 41191 33007 32991 33183 33567 1823
17951 17471 16511 16635 18675 22755
P_X:
63622 63682 63712 61665 57585
P_U:
63747 63555 61539 57447 49263 49277 49373 50333
```

and the upper-q1 masks are

```text
packet:
47335 45295 41215 33279 33759 34719 50975
18239 18047 17663 18687 22779 30963
P_X:
63694 63718 63715 63729 61689
P_U:
64323 63843 63591 61551 57471 49407 50429 50909
```

Each list has 26 pairwise distinct values.  Since every adjacent owner pair
has intersection rank eight and union rank ten, these lists prove exact
global lower- and upper-q1 simplicity for the protected 29-owner bank.

The separation is not an artefact of decimal encoding.  Every X-bank q1
value contains both `alpha,delta` and misses at least one of `h_1,h_2`.
Packet q1 values contain only one seam label except at its central exchange,
whose profile contains the full `X,U` banks.  Every U-bank q1 value contains
both seam labels.  Its first six edges contain both markers except for the
single middle exchange, while its last two have the explicit `X,C,U`
profile and miss `h_2`; none equals an X-bank value because the latter
retains the corresponding `Y` signature.  Ordered exchanges separate values
within each row.

## 5. Internal residence

No positive run wholly internal to `P_X` has length below four.  In fact,
every nonconstant X-bank run meets a path boundary.

In `P_U`, the only nonconstant positive runs meeting neither boundary are

\[
 c_1:\ [2,6]\quad\text{of length }5,
 \qquad c_2:\ [1,7]\quad\text{of length }7.             \tag{5.1}
\]

All other nonconstant runs meet a boundary.  Thus both paths satisfy the
depth-three clipped residence condition.  Exterior collars or compatible
joins are still required at their clipped ends.

## 6. Phase commonality

Packet reversal permutes the contiguous gaps of the ordered X and U banks.
Equations (1.3)--(1.4) range over every such gap.  Therefore the same static
paths `P_X,P_U` cover the overlap leave in either global packet orientation.
No second bank and no fixed-address phase-intersection compiler are needed.

## 7. Exact protected ML9 factor gate

The incidence lift of the opened packet has 26 protected edges.  The lifts
of `P_X` and `P_U` add respectively 10 and 16, for a total protected bank
of

\[
 26+10+16=52                                             \tag{7.1}
\]

incidence edges.  All protected lower and owner vertices are pairwise
compatible by Section 4, and their maximum protected degree is two.

The exact protected subgraph extends to a spanning degree-two factor of
`ML_9`.  Solve the integral bipartite residual b-flow with demand

\[
 \sum_v(2-d_P(v))
\]

on each shore.  The exact residual demand is

\[
                   48568=2\binom{17}{8}-52.             \tag{7.2}
\]

The retained flow saturates all `48568` units.  Starting from that factor,
Boolean-incidence `C6` switches preserve every degree and all 52 protected
incidences.  A deterministic neutral/improving walk used

```text
valid C6 switches       582783
accepted                99415
strictly improving       5823
```

and closed the rank-ten hole count exactly.

### Theorem 7.1 (protected q1-complete seven-factor)

There is a spanning two-factor of `ML_9` which:

1. contains every incidence of the packet, `P_X`, and `P_U` paths above;
2. uses every rank-nine owner and every rank-eight lower colour with degree
   two;
3. covers all `binom(17,10)=19448` immediate-upper colours; and
4. has exactly seven components, of owner sizes

   \[
             14305,8615,1362,18,4,3,3.                  \tag{7.3}
   \]

The protected 29-owner subsystem is therefore embedded literally in one
upper-q1-complete bounded-component host.  This is stronger than the
general small-protected-factor theorem at `m=9`, where its asymptotic edge
threshold is unavailable.

### Theorem 7.2 (exact downstream obstruction of this factor)

The cyclic positive-run census of the seven components is

\[
       \#\operatorname{run}_1=0,\qquad
       \#\operatorname{run}_2=3073,\qquad
       \#\operatorname{run}_3=2710.                       \tag{7.4}
\]

Even after independently choosing the best linear opening of every
component, `5760` short internal runs remain.  Hence the unchanged factor
has no depth-three antecedent and no terminal depth-three compiler cells.
This is a residence failure before Hall, not a measured compiler
deficiency.

Its complete cyclic upper-deck holes beyond q1 are

\[
 \begin{array}{c|rrrrrrr}
 \text{rank}&11&12&13&14&15&16&17\\ \hline
 \text{holes}&1502&295&9&0&0&0&0.
 \end{array}                                               \tag{7.5}
\]

Thus the twin bank pays all twelve packet-opening casualties exactly, but
the arbitrary residual flow does not supply the other exterior all-width
witnesses.  Any k=17 completion must rethread the unprotected bulk while
retaining the 52 protected incidences, or replace this residual factor.

### Lemma 7.3 (the protected fixed-`M_0` projection is a forest)

Use the spanning two-factor `F` from Theorem 7.1 and alternately colour
every component as `M_0` and `M_1`.  Orient each protected owner path in
the direction induced by this colouring.  No prescribed direction is
needed: reversing a protected path preserves its complete interval deck,
and the packet's two phases and both Ferrers triangle families are
reversal-closed.  Along the resulting oriented owner path

\[
 Z_0-I_0-Z_1-I_1-\cdots-I_{s-1}-Z_s,
\]

one has

\[
 M_0(I_i)=Z_i,\qquad I_iZ_{i+1}\in M_1.                 \tag{7.6}
\]

For the q1 colour `R_i=Z_i union Z_(i+1)`, its ordered-diamond tail and head
are

\[
 \psi(R_i)=Z_i,\qquad\phi(R_i)=Z_{i+1}.                  \tag{7.7}
\]

The fixed-`M_0` Catalan link of `I_iZ_(i+1)` is

\[
 \lambda_i=\{I_i,M_0^{-1}(Z_{i+1})\}.
\]

For `i<s-1`, `M_0^{-1}(Z_(i+1))=I_(i+1)`.  For the last
edge it is a residual lower vertex `J` outside every protected lower bank.
Thus the links of this path are exactly

\[
 I_0-I_1-\cdots-I_{s-1}-J.                              \tag{7.8}
\]

The three protected paths have disjoint lower vertices, and their terminal
preimages `J` are distinct because `M_0` is a matching.  Their complete
link projection is therefore a vertex-disjoint union of three paths.  On
the protected bank, tail injectivity, head injectivity, upper-colour
injectivity and graphic independence all hold simultaneously.

This removes the rooted lower/head/graphic correlation only for the 26
protected q1 colours.  Eleven of the twelve Ferrers targets have rank above
ten and are already delivered by longer intervals in the banks, so they do
not enter the q1 matching at all.  Extending (7.8) to the remaining global
upper palette while retaining graphic acyclicity remains open.

## 8. Scope

This construction removes the k=17 four-permanent-marker obstruction and
gives a coefficient-one local repair of all twelve reset-overlap casualties.
It does not prove `nu(17)=24313`.  The remaining tasks are:

1. join or reselect the seven components while retaining the protected paths;
2. eliminate the `5760` unavoidable-under-opening short runs of this frozen
   factor, or choose a different protected factor;
3. supply the `1502+295+9=1806` deeper upper targets still absent;
4. make the clipped bank boundaries resident in one literal source; and
5. only then expose and solve the zero-spare k=17 lower common-cap compiler.

## 9. Construction artifact

The deterministic candidate is generated and checked by

```text
scratch/audit_k17_h2_analytic_twin_bank_20260801.cpp
SHA-256 00353aa4571e20e9a931d54653d00d182916918a088d4bc5768249934f035203

scratch/k17_h2_analytic_twin_bank_20260801.audit.txt
SHA-256 e1ccf4492c7980a127aff58356ce3b2224da6ac287b22edd4152cbce8f85d7dd
```

It was compiled and run on H100 with `g++ -std=c++20 -O3 -DNDEBUG` and
returned

```text
PASS_K17_H2_ANALYTIC_TWIN_BANK
owners=29 lower_q1=26 upper_q1=26 X_targets=6 U_targets=6
```

The H100 binary SHA-256 was
`6064f00f921091c3b6f33b4b1f19553a33139b8f8aad94d5e459d7586a5a1135`.
The combined factor artifacts are:

```text
scratch/search_k17_reset_twin_ferrers_bank_ml9_20260801.cpp
SHA-256 7daae18e958634e9a32e2dac6d38006e8b55ea18284c18c2f22de7f024ad36bc

scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv
SHA-256 7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df

scratch/verify_k17_reset_twin_ferrers_bank_ml9_factor_20260801.cpp
SHA-256 5fe2128850bfd9672f55c370131a46a6f2f993215a22a3d523a703dc74e51c3d

scratch/verify_k17_reset_twin_ferrers_bank_ml9_factor_20260801.out
SHA-256 d49405282c791e408a20e2ff378aa66317e61c567129f50dd5f2b64ebd8ad9df
```

The verifier independently reconstructs both Boolean shores, checks all
48,620 incidences and all protected flags, verifies degree two, both q1
palettes, the seven literal components, every protected target, the
residence census and every deeper upper hole.  Its retained verdict is

```text
PASS_K17_RESET_TWIN_FERRERS_ML9_FACTOR rows=48620 protected=52 q1=19448 components=7 sizes=14305,8615,1362,18,4,3,3 run1=0 run2=3073 run3=2710 best_open_remaining=5760 deep=1502,295,9 targets=12
```
