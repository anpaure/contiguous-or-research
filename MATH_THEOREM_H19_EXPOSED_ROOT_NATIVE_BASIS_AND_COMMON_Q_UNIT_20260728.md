# Exposed-root native bases and the exact Hall-19 former-shore common-Q unit

Date: 2026-07-28

Status: proved general overlap-safe common-`Q` theorem and independently
replayable finite certificate.  The final Hall-19 DM shore has one genuine
two-exposed-root native-basis component.  Separately, the remote discharge of
the old component rooted at `24610` gives a 658-pin literal partial matching
on the 677-target former critical shore.  The verifier performs no carrier
enumeration, SAT, or search for a solution; it recomputes three deterministic
bipartite maximum matchings.

## 1. Exact simultaneous common-`Q` theorem

Let \(V\) be a finite ordered set of physical positions and let \(\Omega\) be
the coordinate set.  A **controller cap** is a pointwise nonempty word

\[
                     P=(P_p)_{p\in V},\qquad P_p\subseteq\Omega.       \tag{1.1}
\]

Let

\[
                  \mathcal E=\{(I_a,S_a):a\in A\}                    \tag{1.2}
\]

be any family of exact interval pins.  The intervals \(I_a\) may overlap
arbitrarily.  For each coordinate \(x\in\Omega\), put

\[
 H_x(P)=\{p\in V:x\in P_p\},\qquad
 B_x=\bigcup_{a:\,x\notin S_a}I_a,
 \qquad K_x=H_x(P)\setminus B_x.                                  \tag{1.3}
\]

Define

\[
 A_p=\{x:p\in K_x\}
     =P_p\cap\bigcap_{a:\,p\in I_a}S_a.                           \tag{1.4}
\]

### Theorem 1.1 (overlap-safe common-`Q` criterion)

Among all words \(C\) satisfying \(C_p\subseteq P_p\), the word \(A\) in
(1.4) is the unique coordinatewise maximal word compatible with every
negative part of every pin in \(\mathcal E\).  It is a literal simultaneous
realization of all pins,

\[
                         \bigcup_{p\in I_a}A_p=S_a\qquad(a\in A),    \tag{1.5}
\]

if and only if

\[
 \boxed{I_a\cap K_x\ne\varnothing
        \quad\text{for every }a\in A\text{ and }x\in S_a,}         \tag{1.6}
\]

and

\[
 \boxed{A_p\ne\varnothing\quad\text{for every }p\in V.}          \tag{1.7}
\]

If \(P\) is the pointwise maximal controller allowed by the central
constraints, then \(A\) is the maximal common-Q word for the complete
central-plus-pin system.

#### Proof

If \(p\in I_a\), exactness of the pin forces every feasible \(C_p\) to be a
subset of \(S_a\): otherwise its interval union contains a forbidden
coordinate.  It also forces \(C_p\subseteq P_p\).  Hence every feasible word
is coordinatewise contained in (1.4), and \(A\) satisfies all negative pin
conditions.

For \(x\in S_a\), the coordinate occurs in the \(a\)-th interval union under
\(A\) exactly when \(I_a\cap K_x\ne\varnothing\).  Thus (1.6) is precisely
the full collection of positive pin conditions.  Condition (1.7) is
precisely literal nonemptiness.  These conditions are therefore necessary
and sufficient, and maximality has already been proved.  \(\square\)

This theorem includes central windows, exceptional windows, and exact point
pins by putting all of them into \(\mathcal E\).  A positive point
requirement \((p,x)\) is the special condition \(p\in K_x\).  Merely
checking that \(A_p\ne\varnothing\) does not replace it.

### Native protected specialization

For an interval \(J\), write

\[
                         \tau_P(J)=\bigcup_{p\in J}P_p.             \tag{1.8}
\]

If a protected pin is native, \(S_J=\tau_P(J)\), its negative blockers make
no change to \(P\): when \(x\notin S_J\), already
\(H_x(P)\cap J=\varnothing\).  Let \(\mathcal R\) be a set of target labels
and suppose the only new nonnative pins are

\[
                 (I_\rho,\rho),\qquad \rho\in\mathcal R.            \tag{1.9}
\]

Then the maximal candidate reduces to

\[
 A_p=P_p\cap\bigcap_{\rho:\,p\in I_\rho}\rho,                    \tag{1.10}
\]

and, coordinatewise,

\[
 B_x=\bigcup_{\rho:\,x\notin\rho}I_\rho.                         \tag{1.11}
\]

Equations (1.6)--(1.7), applied to every old native pin and every new root
pin, remain necessary and sufficient.  In particular, overlapping shrink
intervals are not harmless automatically: one root pin may delete every
witness needed by another.  Equations (1.6)--(1.7) detect exactly that
failure.

## 2. Native bases with an exposed root set

Let \(X\) be a set of target labels and \(Y\) a set of distinct physical
cells.  Let \(\tau_P(c)\) denote the native trace of cell \(c\).  We call
\((X,Y)\) an **exposed-root native basis** with exposed set
\(R\subseteq X\) if

\[
              \tau_P:Y\longrightarrow X\setminus R               \tag{2.1}
\]

is a bijection.  Thus

\[
                  |X|-|Y|=|R|.                                    \tag{2.2}
\]

The terminology does not assert that a member of \(R\) equals
\(\bigcap_{x\in X}x\).  For a multi-root component the Boolean intersection
may not even belong to \(X\).

### Theorem 2.1 (exposed-root completion)

Assume \((X,Y)\) is an exposed-root native basis.  For every
\(\rho\in R_0\subseteq R\), choose an additional physical cell \(I_\rho\),
with all chosen cells distinct and disjoint from \(Y\).  Retain the native
pins on \(Y\), and repin \(I_\rho\) to \(\rho\).  If the system satisfies
(1.6)--(1.7), then one literal word realizes

\[
                  (X\setminus R)\sqcup R_0                         \tag{2.3}
\]

on distinct cells.  It therefore supplies exactly \(|R_0|\) new local
matching units.  If \(R_0=R\), it saturates all of \(X\).

The intervals of the additional cells may overlap one another and the
retained cells.  Their physical cell identities, however, must be distinct.

#### Proof

The retained cells in \(Y\) serve the pairwise distinct targets
\(X\setminus R\).  Theorem 1.1 makes each additional cell serve its distinct
label in \(R_0\) under the same word.  These two target sets and the two cell
sets are disjoint.  Hence they form the claimed literal matching.  \(\square\)

A duplicate-child realization is the special case in which
\(\tau_P(I_\rho)=s\in X\setminus R\) and the original cell serving \(s\) is
retained.  Across several components, Theorem 2.1 adds the exposed units only
when all added cells are globally distinct and the single simultaneous
system (1.6)--(1.7) passes.  A global Hall rank statement additionally needs
a disjoint retained or rerouted exterior matching.

## 3. The frozen Hall-20 to Hall-19 route

The three carriers are

```text
scratch/k15_segment_braid_hall20_zero6.json
scratch/k15_h20_h19_root8216_chain/router/candidate_0000.json
scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json
```

with SHA-256 values

```text
9dd192d50e2e94dccb109fdc649fa5e13d2e4f17bac687d30547bd1bb6ddfcf1
eabc8c63d5c8ae1b63e95118be620cb2e94507dafb1d11a1b10a46de41dc2e51
86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b
```

The stored transformations materialize exactly as

\[
 H20\xrightarrow{\operatorname{RF}(180,2764,4210)}H20^{(8216)}
    \xrightarrow{\operatorname{FR}(123,722,4710)}H19.             \tag{3.1}
\]

Every carrier is a deck-exact 6,435-vertex Johnson path, is depth-three
resident, has lower-hole vector

\[
                         (4,18,11,1,0,0,0),                       \tag{3.2}
\]

and has no upper support hole at any depth \(1\le q\le7\).  The same six
zero-candidate targets persist.  Exact matching ranks, Hall deficiencies,
and canonical DM shores are

\[
\begin{array}{c|c|c|c}
 &\nu&h&|L_{DM}|/|R_{DM}|\\ \hline
H20&16363&20&677/657\\
H20^{(8216)}&16363&20&677/657\\
H19&16364&19&516/497.
\end{array}                                                       \tag{3.3}
\]

Thus the first braid is neutral and the second gains exactly one graph rank.

## 4. The exact \(321/319\) two-root component

Before the neutral braid, the relevant components are

\[
                  161/160\text{ rooted at }8217,
          \qquad 160/159\text{ rooted at }8218.                   \tag{4.1}
\]

Their target sets are disjoint.  The neutral braid merges their union into
one connected \(321/319\) component \((X,Y)\).  Direct reconstruction gives

\[
                  \boxed{\{\tau_P(c):c\in Y\}
                         =X\setminus\{8217,8218\},}                \tag{4.2}
\]

with all 319 traces distinct.  Moreover,

\[
                         \bigcap_{x\in X}x=8216,
                 \qquad 8216\notin X.                             \tag{4.3}
\]

The improving braid leaves this component and its trace identity unchanged,
so it persists in final H19.

### Consequence

The object is not a single-rooted native basis: neither missing target can be
replaced by the intersection core.  It is exactly an exposed-root native
basis with

\[
                             R=\{8217,8218\}.                      \tag{4.4}
\]

Theorem 2.1 is therefore the correct completion theorem.  It would require
two distinct additional cells and a simultaneous overlap-safe check to fill
both roots.  No such two-cell completion is claimed here.  The neutral braid
has reorganized the deficit but has not reduced it.

The complete final H19 component census is

\[
\begin{array}{c|c|l}
|X|/|Y|&\#&\text{exposed targets}\\ \hline
321/319&1&8217,8218\\
161/160&1&960\\
5/4&2&4213,7504\\
3/2&2&1103,18970\\
2/1&6&2420,2575,2676,9524,17683,19568\\
1/0&6&5801,13616,13620,17738,21641,29776.
\end{array}                                                       \tag{4.5}
\]

Every component satisfies the exposed-root trace identity (2.1).  Hence the
497 final right cells give 497 simultaneous native pins, and the 19 exposed
targets in (4.5) are exactly the final DM gap.

## 5. Remote discharge of the root-`24610` component

In the neutral carrier, let \(X_{24610}\) be the old \(161/160\) component
rooted at `24610`.  The improving braid removes all 161 of its targets from
the final DM shore.  Restricted to those targets, its final physical
neighborhood has 162 cells.  Their native traces contain every one of the
160 nonroot targets.  Exactly two traces are duplicated:

\[
\begin{array}{c|c|c|c|l}
\tau_P&\text{cells}&\text{depth/start}&\text{controller letters}
 &\text{restricted shore}\\ \hline
25634&1212&0/1212&(25634)&\{24610,25634\}\\
25634&4713&0/4713&(25634)&\{24610,25634\}\\
26146&11150&1/4712&(26144,25634)&\{26146\}\\
26146&11671&1/5233&(9762,17954)&
 \{24610,25122,25634,26146\}.
\end{array}                                                       \tag{5.1}
\]

Every other nonroot trace occurs exactly once, and no trace lies outside
\(X_{24610}\).  The final neighborhood is disjoint from the 497-cell final DM
native basis.

Choose either depth-zero `25634` cell and repin it to `24610`.  Since

\[
                         25634\setminus24610=1024,                \tag{5.2}
\]

the maximal common-`Q` word is simply

\[
 A_p=\begin{cases}
       24610,&p=1212,\text{ respectively }p=4713,\\
       P_p,&\text{otherwise}.
     \end{cases}                                                  \tag{5.3}
\]

Keep the other depth-zero cell on `25634`, choose cell `11150` for `26146`,
and choose the unique native cell for every other nonroot.  Cell `11671`
remains unused.

### Theorem 5.1 (the H20-to-H19 former-shore pin unit is literal common-Q)

For either choice in (5.3), one word realizes simultaneously:

1. all 6,435 central middle windows;
2. all 497 native pins of the final H19 DM shore;
3. one native pin for each of the 160 nonroot targets in
   \(X_{24610}\); and
4. the exceptional root pin to `24610`.

All 658 targets and all 658 cells are pairwise distinct.  Every one of the
6,438 physical letters is nonempty.  On the former 677-target H20 critical
shore, the uncovered set is exactly

\[
\begin{split}
\{&960,1103,2420,2575,2676,4213,5801,7504,8217,8218,9524,\\
  &13616,13620,17683,17738,18970,19568,21641,29776\},             \tag{5.4}
\end{split}
\]

so the literal gap is exactly 19.

The word SHA-256 digests, using the comma-separated integer word, are

```text
cell 1212: 96d50becdfd5f9aede1fac5059b7cca295df6b37dcacbd70a8c91d88f9d63855
cell 4713: ec74223c038d38784059aae7ac801a2bce7297b90fa4503b34b3a252f343107a
```

#### Proof

All 657 retained nonexceptional pins are native under the final maximal
erosion controller \(P\), so they impose no new negative deletion.  The sole
deletion is mask 1024 at one position.  The verifier checks condition
(1.6) for all 3,573 positive obligations for the deleted coordinate among
the 6,435 central and 657 retained-native windows.  Exactly 6 of those
intervals meet changed position 1212, and exactly 7 meet changed position
4713; the remaining checks are automatic nonintersection witnesses.  It
checks (1.7) at all 6,438 positions and then independently recomputes every
central union and every one of the 658 selected pin unions under (5.3); all
are exact.

The final DM cells and the 162-cell \(X_{24610}\) neighborhood are disjoint.
The trace census in (5.1) supplies one distinct cell for every nonroot and a
second `25634` cell for the root shrink.  Hence target and cell injectivity
hold.  Equation (5.4) follows by exact set subtraction from the frozen
677-target shore.  Thus the one-unit increase in the former-shore
simultaneous pin count, from 657 to 658, is literal.  Independently, (3.3)
records the global incidence-rank change \(16363\to16364\); no exterior
common-word lift is inferred.  \(\square\)

## 6. Exact proved boundary

The following statements are proved:

* arbitrary overlapping exact shrink pins are governed exactly by
  (1.3)--(1.7);
* a native basis may have an exposed target set of any size; its local
  completion gains one literal unit per simultaneously feasible extra cell;
* final H19 contains the \(321/319\) native basis missing exactly
  `8217,8218`, not a fictitious root `8216`;
* the remote `24610` discharge has two independently valid literal sockets;
* either socket gives 658 simultaneous pins on the former 677-target shore,
  with exact literal gap 19.

The following statements are not proved:

* a two-cell completion of the exposed pair `8217,8218`;
* a single word realizing the exterior portion of a full 16,364-edge global
  matching;
* a universal router/splitter theorem or the asymptotic coefficient-one
  theorem.

In particular, a two-target restricted cell shore such as
\(\{24610,25634\}\) is not by itself a common-Q certificate.  The literal
claim comes from the separate blocker test and direct word reconstruction in
Theorem 5.1.

## 7. Permanent verifier and certificate

Run the lightweight deterministic audit with

```text
python3 scratch/audit_k15_h20_h19_exposed_roots_common_q.py
```

It reconstructs the three frozen graphs, recomputes three deterministic
bipartite maximum matchings and their DM components, and checks native traces
and interval unions.  It performs no carrier enumeration, SAT call, or search
for a solution.

```text
4d7e3d33621da4c202c68e9379da05338ba2890922dce63ecfe4be0857c8fd50
  scratch/audit_k15_h20_h19_exposed_roots_common_q.py

e691eb1760ddebbd7a82225f347c43ddc6cae32135c6db279797f18469e8b9b0
  scratch/k15_h20_h19_exposed_roots_common_q_certificate.json
```
