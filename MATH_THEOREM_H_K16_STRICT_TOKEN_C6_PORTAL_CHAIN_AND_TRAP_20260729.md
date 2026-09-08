# K16 strict-token portal chain and the radius-three trap

## 1. Scope and verdict

This note concerns the fixed physical overlay between

- the radius-five q1-perfect factor
  `scratch/k16_q1_endpoint_resume1_static_portal_radius5_20260729.json`, and
- the resident endpoint
  `scratch/k16_pbbs_oriented_noaa_softq1_resume1_20260729.json`.

The grouped obstruction in that overlay can be escaped by an explicit
degree-balanced alternating (C_6) which preserves **every lower and upper q1
load exactly**.  The resulting overlay is nevertheless infeasible.  Its new
six-row core admits a second strict-token (C_6), but the core after that move
has only the inverse (C_6) among all radius-three strict-token circuits
through its core edges.  Thus the natural local strict-token core chase is
trapped in a two-cycle.

This is not a no-go for larger circuits, non-strict q1-preserving moves, a
larger endpoint universe, or a joint rethreading which changes the resident
factor.

## 2. Exchange notation

Work in the Johnson graph (J(16,8)).  For an edge (e=XY), put

\[
 \lambda_-(e)=X\cap Y,
 \qquad
 \lambda_+(e)=X\cup Y.
\]

If (F) is a spanning 2-factor, (D\subseteq F), and
(A\subseteq E(J(16,8))\setminus F), define

\[
 F[D\to A]=(F\setminus D)\cup A.
\]

Call the exchange **strict-token** when

\[
 \sum_{e\in D}{\bf 1}_{\lambda_-(e)}
 =
 \sum_{e\in A}{\bf 1}_{\lambda_-(e)},
 \qquad
 \sum_{e\in D}{\bf 1}_{\lambda_+(e)}
 =
 \sum_{e\in A}{\bf 1}_{\lambda_+(e)}.
 \tag{2.1}
\]

If additionally

\[
 \deg_D(v)=\deg_A(v) \quad\hbox{for every rank-eight vertex }v,
 \tag{2.2}
\]

then (F[D\to A]) is again a spanning 2-factor and every physical lower and
upper q1 load is unchanged.  This follows directly by subtracting the
incidence vectors in (2.1) and (2.2).

An alternating (C_{2r}) automatically satisfies (2.2).  We call (r) its
replacement radius.

## 3. The original six-row core

Let (Q_3) be the radius-five q1 factor and (R_1) the resident factor.  In
the fixed-common overlay, write (b_e=1) when a (Q_3\setminus R_1) edge is
removed and (a_e=1) when an (R_1\setminus Q_3) edge is added.  Put

\[
\begin{array}{lll}
 x=b_{(50531,51042)}, & z=b_{(52547,56642)},
 & k=(50531,52547),\\
 s=b_{(55491,55619)}, & t=b_{(55619,63747)},
 & r=a_{(55619,56579)},\\
 && h=a_{(53575,55619)}.
\end{array}
\]

The edge (k) is common and hence fixed in this overlay.  Exact provider
lists give

\[
 x=s=t=0,
 \qquad z\le r.
 \tag{3.1}
\]

Indeed, upper colours (51043,55747,63811) have their displayed source edge
as their only overlay provider, while upper colour (56643) has precisely
the source provider ((52547,56642)) and the resident replacement
((55619,56579)).  Thus only three of the four upper rows are singleton rows;
the fourth is the coupling (z\le r).

The coordinate-zero length-two motif has closure

\[
 \{(50531,51042),k,(52547,56642)\}.
\]

Since (k) is fixed, residence requires

\[
 x+z\ge1.
 \tag{3.2}
\]

Degree balance at vertex (55619) is

\[
 r+h=s+t.
 \tag{3.3}
\]

Consequently

\[
 1\le x+z\le x+r\le x+r+h=x+s+t=0,
\]

a contradiction.  The fixed-common hypothesis is essential.

## 4. First strict-token portal

Consider the alternating cycle

\[
 50475,50979,50531,51042,50538,50986,50475.
 \tag{4.1}
\]

Delete its first, third and fifth edges,

\[
 D_1=\{
 (50475,50979),(50531,51042),(50538,50986)
 \},
\]

and add the other three,

\[
 A_1=\{
 (50475,50986),(50531,50979),(50538,51042)
 \}.
\]

The token ledgers are literally

\[
 \lambda_-(D_1)=\lambda_-(A_1)
   =\{50467,50474,50530\},
 \tag{4.2}
\]

\[
 \lambda_+(D_1)=\lambda_+(A_1)
   =\{50987,51043,51050\}.
 \tag{4.3}
\]

Hence this is a strict-token exchange.  It deletes the core edge
((50531,51042)), so the motif in Section 3 disappears.  All three added
edges lie outside (Q_3) and outside each of the three saved resident
endpoints; this is a genuine exterior portal, not an internal overlay
circuit.

Let

\[
 F_1=Q_3[D_1\to A_1].
\]

Literal replay gives a spanning Johnson 2-factor with four components,
component lengths

\[
 11325,515,515,515,
\]

zero lower and upper q1 holes, and 2250 positive-run residence violations
with length histogram

\[
 1^{135},2^{915},3^{1200}.
\]

There is no pointwise static blocker against (R_1).  Nevertheless the full
degree/q1/inherited-residence overlay is infeasible.

## 5. The translated core at vertex 49819

Put

\[
 e_1=(37531,37785),\quad
 e_2=(37531,41627),\quad
 e_3=(41627,41657),
\]

and

\[
 f=(49819,53787),\qquad g=(49819,49881),
 \qquad \rho=(33467,49819).
\]

In (F_1\cup R_1), the complete relevant provider rows are

\[
\begin{array}{c|c|c}
\hbox{colour}&F_1\setminus R_1&R_1\setminus F_1\\ \hline
L33435&\{e_2\}&\{\rho\}\\
L37529&\{e_1\}&\varnothing\\
L41625&\{e_3\}&\varnothing\\
L49691&\{f\}&\varnothing\\
U49883&\{g\}&\varnothing.
\end{array}
\tag{5.1}
\]

The coordinate-one length-two motif has closure

\[
 \{e_1,e_2,e_3\}.
 \tag{5.2}
\]

The last four singleton rows in (5.1) forbid removal of (e_1,e_3,f,g).
The two selected (F_1)-edges at vertex (49819) are exactly (f,g).
Degree balance therefore forbids every resident addition at that vertex, in
particular `rho`.  The first row in (5.1) then forbids removal of `e_2`.
No edge of (5.2) can be removed, contradicting residence.  This is a
solver-free proof of infeasibility for the full (F_1/R_1) overlay.

## 6. Second strict-token portal

There is a strict-token alternating cycle

\[
 41147,57499,57529,58009,41657,41627,41147.
 \tag{6.1}
\]

Its deleted and added shores are

\[
 D_2=\{
 (41147,57499),(41627,41657),(57529,58009)
 \},
\]

\[
 A_2=\{
 (41147,41627),(41657,58009),(57499,57529)
 \}.
\]

They have the identical token ledgers

\[
 \lambda_-(D_2)=\lambda_-(A_2)
   =\{41115,41625,57497\},
 \tag{6.2}
\]

\[
 \lambda_+(D_2)=\lambda_+(A_2)
   =\{41659,57531,58041\}.
 \tag{6.3}
\]

Thus

\[
 F_2=F_1[D_2\to A_2]
\]

is again a q1-load-identical spanning 2-factor.  It deletes (e_3), hence
destroys (5.2).  Literal replay gives the same four component lengths, zero
q1 holes, and 2251 short positive runs with histogram

\[
 1^{135},2^{914},3^{1202}.
\]

Again there is no pointwise static blocker against (R_1), but the complete
overlay remains infeasible.

## 7. The second translated core

In (F_2\cup R_1), define

\[
 c_1=(37051,41147),\quad
 c_2=(37531,41627),\quad
 c_3=(41147,41627).
\]

The exact provider rows are

\[
\begin{array}{c|c|c}
\hbox{colour}&F_2\setminus R_1&R_1\setminus F_2\\ \hline
L32955&\{c_1\}&\varnothing\\
L33435&\{c_2\}&\{\rho\}\\
L49691&\{f\}&\varnothing\\
U41659&\{c_3\}&\varnothing\\
U49883&\{g\}&\varnothing.
\end{array}
\tag{7.1}
\]

The coordinate-thirteen length-two motif has closure

\[
 \{c_1,c_2,c_3\}.
 \tag{7.2}
\]

Rows (L32955,U41659,L49691,U49883) lock (c_1,c_3,f,g).
As before, (f,g) are the two selected edges at vertex (49819), so degree
balance forbids `rho`.  Row `L33435` then locks `c_2`, contradicting
(7.2).  Thus the obstruction has moved again but retained the same locked
socket (49819).

## 8. Exact radius-three trap

At `F_1`, the complete replacement-radius-two census through the five blue
core edges is:

| target edge | alternating C4 candidates | strict-token candidates |
|---|---:|---:|
| `(37531,37785)` | 10 | 0 |
| `(37531,41627)` | 14 | 0 |
| `(41627,41657)` | 8 | 0 |
| `(49819,49881)` | 10 | 0 |
| `(49819,53787)` | 6 | 0 |

First consider replacement radius two at the current factor (F_2).  Every
two-edge degree-balanced switch in a simple graph is one alternating (C_4).
Enumerating both orientations of the first deleted edge and every possible
nonfactor Johnson continuation gives the complete census

\[
\begin{array}{c|r|r}
\hbox{target edge}&\hbox{alternating }C_4\hbox{ candidates}&
\hbox{strict-token candidates}\\ \hline
(37051,41147)&14&0\\
(37531,41627)&13&0\\
(41147,41627)&10&0\\
(49819,49881)&10&0\\
(49819,53787)&6&0.
\end{array}
\tag{8.1}
\]

Thus no strict-token (C_4) can hit any blue edge of the Section 7 core.

We exhaustively classified every replacement-radius-three alternating circuit
through every blue edge appearing in each translated core, retaining only
circuits satisfying the exact two-ledger identity (2.1).

For the Section 5 core, the complete census is

\[
\begin{array}{c|r|r}
\hbox{target edge}&\hbox{alternating }C_6\hbox{ candidates}&
\hbox{strict-token candidates}\\ \hline
(37531,37785)&371&0\\
(37531,41627)&438&0\\
(41627,41657)&406&1\\
(49819,53787)&322&0\\
(49819,49881)&432&0.
\end{array}
\tag{8.2}
\]

The unique strict-token candidate is precisely (D_2\to A_2).

For the Section 7 core, the complete census is

\[
\begin{array}{c|r|r}
\hbox{target edge}&\hbox{alternating }C_6\hbox{ candidates}&
\hbox{strict-token candidates}\\ \hline
(37051,41147)&432&0\\
(37531,41627)&424&0\\
(41147,41627)&421&1\\
(49819,49881)&435&0\\
(49819,53787)&322&0.
\end{array}
\tag{8.3}

The unique strict-token candidate deletes (A_2) and adds (D_2).  It is
exactly the inverse of the second portal and returns (F_2) to (F_1).
Therefore the rule

> hit the current six-row core by a strict-token alternating (C_6) through
> one of its blue edges

is trapped in the two-cycle

\[
 F_1 \longleftrightarrow F_2.
\tag{8.4}
\]

The census is performed by explicit generation of every simple alternating
(C_6) through the named edge, followed by literal lower- and upper-token
multiset comparison.  The saved verifier separately reconstructs both
factors, both provider cores, and the inverse relation.

## 9. Exact remaining gate

The first unclosed local gate is now sharply scoped.

> **Non-inverse locked-socket portal lemma.**  Starting from (F_2), find a
> degree-balanced q1-preserving exchange which destroys the motif (7.2) and
> also prevents the locked-socket proof at vertex (49819), without returning
> to (F_1).

A strict-token solution must have replacement radius at least four, hence an
alternating (C_8) or a union of smaller circuits not confined to the current
core-edge (C_6) catalogue.  Alternatively one may use q1 slack rather than
exact token equality, introduce an exterior provider for one of the five
rows in (7.1), or change (R_1) simultaneously.

The generic core-circuit script has a replacement-radius parameter and the
radius-four command is prepared, but it was deliberately not launched after
the H100 resource moratorium.  No (C_8) existence or nonexistence claim is
made here.

Breaking only the displayed motif is insufficient: Sections 5 and 7 show
that the carrier can recreate a new length-two motif tied to the same remote
socket.  A successful portal must alter both the motif closure and the
socket/provider mechanism.

## 10. Audited artifacts

Construction and replay:

```text
scratch/materialize_k16_portalq1_strict_token_c6_20260729.py
scratch/k16_portalq1_strict_token_c6_20260729.json
scratch/k16_portalq1_strict_token_c6_20260729.audit.json
scratch/materialize_k16_portalq1_strict_token_c6x2_20260729.py
scratch/k16_portalq1_strict_token_c6x2_20260729.json
scratch/k16_portalq1_strict_token_c6x2_20260729.audit.json
```

Core certificates and bounded classifications:

```text
scratch/k16_strict_token_c6_resume1_q1_motif_core_20260729.json
scratch/k16_strict_token_c6x2_resume1_q1_motif_core_20260729.json
scratch/search_k16_strict_token_core_chain_20260729.py
scratch/k16_strict_token_core_chain_20260729.json
scratch/search_k16_strict_token_from_core_generic_20260729.py
scratch/k16_strict_token_core_chain_round3_20260729.json
scratch/search_k16_strict_token_core_c4_census_20260729.py
scratch/k16_strict_token_core_c4_round2_20260729.json
scratch/k16_strict_token_core_c4_round3_20260729.json
scratch/audit_k16_strict_token_c6_chain_trap_20260729.py
scratch/k16_strict_token_c6_chain_trap_20260729.audit.json
```

The final lightweight replay has SHA-256

```text
e760fd7fef1028eda0c3851c1565c82aec9887cd6b4d61dadde04faefe431755
```

and its output has SHA-256

```text
b947955bda222b856c006779feb38c3db735bd7143a104eb20488a85b8494007
```
