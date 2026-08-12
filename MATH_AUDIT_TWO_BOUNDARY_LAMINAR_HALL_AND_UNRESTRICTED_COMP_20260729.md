# Audit: two-boundary capacity, laminar Hall, and unrestricted COMP

Date: 2026-07-29

Status: proof-quality adversarial audit; no computation.

## 1. Verdict

The inequalities

\[
 \sum_{s=1}^q|\mathcal U_s|\le 2q\qquad(1\le q\le d)    \tag{1.1}
\]

do not, even with laminar PBBS flag labels or laminar candidate intervals,
imply feasibility of unrestricted \(\operatorname{COMP}_d(T)\).

The distinction by depth is sharp.

* The \(q=1\) capacity two is intrinsic even for unrestricted antecedents.
* For \(q\ge2\), capacity \(2q\) is a literal one-core phenomenon. An
  unrestricted witness can be a long interior interval.
* In one-core form, (1.1) is only the chain shadow of Hall. It is sufficient
  only under complete bank access, or after all node cuts of the actual
  laminar target-to-slot neighbourhood family have been checked.
* Matching still does not enforce chronology. One must first fix a safe
  core, or in unrestricted form check the coordinatewise no-cover
  conditions of Theorem 5.1 below.

## 2. The sharp q1/deeper separation

Let \(A=(A_0,\ldots,A_{W+d-1})\) satisfy \(D^dA=T\), where consecutive
terms of \(T\) are distinct adjacent rank-\(r\) Johnson vertices.

### Theorem 2.1 (unrestricted q1 has exactly two channels)

If a rank-\((r-1)\) target \(S\) is not equal to any internal colour
\(T_i\cap T_{i+1}\), then every interval of \(A\) with union \(S\) touches
source position \(0\) or \(W+d-1\). At most one distinct such target can
use each end.

#### Proof

A lower target has a witness interval of at most \(d\) letters, since any
longer interval contains a full middle window of rank \(r\). For a witness
\(I=[a,b]\), the middle windows containing it have starts

\[
 C(I)=[\max(0,b-d),\min(a,W-1)]\cap\mathbb Z.           \tag{2.1}
\]

For every \(i\in C(I)\), \(S\subseteq T_i\). If \(C(I)\) contains two
indices, it contains consecutive \(i,i+1\), and equal ranks force
\(S=T_i\cap T_{i+1}\). Thus a noninternal \(S\) has \(|C(I)|=1\).
Because \(|I|\le d\), (2.1) has one element only when \(a=0\) or
\(b=W+d-1\).

Prefix unions are nested, and two distinct sets of the same rank cannot be
nested. Hence at most one rank-\((r-1)\) target uses the left end. The
suffix proof is identical. QED.

Thus \(|H_1|\le2\) is universally necessary. It is not sufficient for
endpoint assignment. In the one-core extreme-letter architecture, the
sharp two-slot Hall conditions are

\[
 \#\{S:N(S)\subseteq\{L\}\}\le1,\quad
 \#\{S:N(S)\subseteq\{R\}\}\le1,\quad
 |H_1|\le2.                                             \tag{2.2}
\]

Two holes legal only at \(L\) pass the scalar bound and fail Hall.

### Proposition 2.2 (deeper targets can escape to the interior)

Assume the local intersection grading supplied by \(d\)-residence. An
interior source interval of length \(\ell\) is contained in

\[
                         t=d-\ell+2                     \tag{2.3}
\]

consecutive middle windows, whose intersection has rank \(r-(t-1)\). If a
rank-\((r-q)\) target on that interval is not a fixed depth-\(q\)
intersection colour, then

\[
                         \ell\ge d-q+2.                 \tag{2.4}
\]

Indeed, \(t>q+1\) makes the containing intersection too small, while
\(t=q+1\) forces equality with the fixed depth-\(q\) colour. Hence \(t\le q\),
which is (2.4).

For \(q=1\), (2.4) requires \(\ell\ge d+1\), impossible for a lower target.
For every \(q\ge2\), it permits \(\ell\le d\). A rank-\((r-2)\) hole, for
example, may occupy an interior interval of length \(d\). Therefore the
nested banks

\[
 B_q=\{0,\ldots,q-1\}\cup
     \{W+d-q,\ldots,W+d-1\},\qquad |B_q|=2q             \tag{2.5}
\]

are forced only after the one-core residuals have been made literal. They
are not unrestricted capacities.

## 3. Exact laminar b-matching

Let \(\mathcal D\) be unit demands, \(V\) slots with integral capacities
\(b(v)\), and \(N(u)\subseteq V\) the nonempty neighbourhood of demand
\(u\).

### Theorem 3.1 (laminar Hall reduction)

If the distinct sets in \(\mathcal L=\{N(u):u\in\mathcal D\}\) are
laminar, a capacitated matching saturating \(\mathcal D\) exists if and only
if, for every \(L\in\mathcal L\),

\[
 \boxed{
 |\{u:N(u)\subseteq L\}|\le\sum_{v\in L}b(v).}           \tag{3.1}
\]

#### Proof

Necessity is clear. Given \(X\subseteq\mathcal D\), its inclusion-maximal
neighbourhoods are pairwise disjoint by laminarity. Partition \(X\) among
those maximal neighbourhoods. Applying (3.1) to each part and summing gives
the capacitated Hall inequality for \(X\). Hall gives the matching. QED.

If every depth-\(s\) demand has exactly \(N(u)=B_s\), (3.1) reduces to
(1.1). This complete-bank hypothesis is the strongest setting in which the
scalar depth inequalities alone suffice. With proper subbanks, every node
cut is needed.

Laminarity of PBBS target labels is not laminarity of \(N(u)\). Nor is the
local laminarity of coordinate-position sets in a PBBS corridor the
target-to-slot incidence required here.

For the one-core compiler, Theorem 3.1 becomes sufficient only after a core
\(C\) satisfying

\[
 C_p\subseteq P_p,\qquad
 C_p\cup C_{p+1}=P_p\cup P_{p+1}                       \tag{3.2}
\]

has been fixed, and with the actual neighbourhoods

\[
 N_C(S)=\{p:C_p\subseteq S\subseteq P_p\}.              \tag{3.3}
\]

If \(\{N_C(S)\}\) is laminar, (3.1) is an exact compact form of Hall for
that fixed core.

## 4. Two exact chronology counterexamples

### Counterexample 4.1 (laminar matching, adjacent one-core loss)

Let \(P_0=U\), \(P_1=U\setminus\{a\}\), and choose \(b\in U\setminus\{a\}\).
Put

\[
 S=U\setminus\{b\},\qquad R=U\setminus\{a,b\}.          \tag{4.1}
\]

The labels are nested. Suppose the local containment neighbourhoods are

\[
 N(S)=\{0\},\qquad N(R)=\{0,1\}.                        \tag{4.2}
\]

They are laminar and satisfy Hall. The unique matching sends \(S\) to
\(0\) and \(R\) to \(1\), but

\[
 S\cup R=U\setminus\{b\}\neq U=P_0\cup P_1.             \tag{4.3}
\]

Both assigned letters omit \(b\), so adjacent chronology fails. The scalar
depth loads also pass: one q1 demand and one q2 demand give \(1\le2\) and
\(2\le4\). This is why a safe core must precede matching.

### Counterexample 4.2 (laminar pins erase an unrestricted middle window)

Let \(d\ge2\) and \(r\ge2d+1\). Choose an \(r\)-set \(U\), distinct
\(a_1,\ldots,a_d,b,c_1,\ldots,c_d\in U\), and distinct
\(\alpha_1,\ldots,\alpha_d\notin U\). Use the resident Johnson prefix

\[
 T_j=(U\setminus\{a_1,\ldots,a_j\})
        \cup\{\alpha_1,\ldots,\alpha_j\}\quad(0\le j\le d). \tag{4.4}
\]

Its left erosion cells are

\[
 P_p=U\setminus\{a_1,\ldots,a_p\}\quad(0\le p\le d).    \tag{4.5}
\]

This prefix is compatible with strong \(d\)-residence: continue for \(d\)
steps by deleting \(c_1,\ldots,c_d\) and inserting fresh coordinates, so
every newly inserted \(\alpha_j\) survives for at least \(d+1\) states.
The runs deleted in the displayed prefix meet the global left endpoint.

Take the two pins

\[
 (\{0\},S),\qquad([1,d],R),                             \tag{4.6}
\]

with

\[
 S=U\setminus\{b\},\qquad R=U\setminus\{a_1,b\}.        \tag{4.7}
\]

Their labels are nested and their intervals are disjoint, hence laminar.
Both fit the erosion envelope, and their q1/q2 scalar loads pass. Yet both
labels omit \(b\), so the negative intervals cover the entire first middle
window \([0,d]\). Since \(b\in T_0\), no word realizing both pins can have
\(D^dA=T\). This is an unrestricted chronology conflict, not merely a
failure of \(DA=DP\).

## 5. Correct fixed-atlas criterion for unrestricted COMP

Fix one desired witness pin \((I_\alpha,S_\alpha)\), \(|I_\alpha|\le d\),
for every lower target. Define

\[
 E_x=\{p:x\in P_p\},\qquad
 Q_x=E_x\setminus
       \bigcup_{\alpha:x\notin S_\alpha}I_\alpha.       \tag{5.1}
\]

### Theorem 5.1 (fixed-atlas no-cover criterion)

There is a nonzero \(A\subseteq P\) with \(D^dA=T\) and
\(\bigcup_{p\in I_\alpha}A_p=S_\alpha\) for every \(\alpha\) if and only if

\[
 Q_x\cap[i,i+d]\neq\varnothing
 \quad(i=0,\ldots,W-1,\ x\in T_i),                     \tag{5.2}
\]

\[
 Q_x\cap I_\alpha\neq\varnothing
 \quad(\alpha,\ x\in S_\alpha),                        \tag{5.3}
\]

and

\[
                         \bigcup_xQ_x=[0,W+d-1].        \tag{5.4}
\]

When they hold, the maximal allowed word \(A_p=\{x:p\in Q_x\}\) works.

#### Proof

Each negative pin forbids \(x\) throughout its interval, so every realizing
support lies in \(Q_x\). Middle positives, pin positives, and nonzero source
letters give (5.2), (5.3), and (5.4). Conversely, the maximal allowed word
contains no forbidden coordinate; (5.2) realizes every middle equality,
(5.3) every extra pin equality, and (5.4) makes all letters nonempty. QED.

The central-hit condition (5.2) is indispensable. Extra negative pins can
erase all hits which the unmodified maximal erosion supplied. Counterexample
4.2 does exactly this.

Thus, after one interval per target has been fixed, no rounding or Hall
argument remains: the test is coordinatewise. If intervals still must be
selected from PBBS candidate flags, that selection problem is coupled and
is not solved by scalar or laminar capacity counts.

## 6. Exactly what PBBS supplies and what remains

The audited PBBS machinery supplies cyclic targetwise flags, concrete local
corridor witnesses, local prefix/suffix laminar coordinate supports, and a
literal chronology on which cut losses can be evaluated. In the special
complement-projected/fixed-matching factor used at \(k=15\), it also supplies
an exact q1 rainbow deck; that is not a property of the raw PBBS
\(m\)-set factor.

It does not presently supply uniformly:

1. one surviving final interval for every lower target, selected
   simultaneously;
2. the central no-cover checks (5.2) for that selection;
3. a safe one-core \(C\);
4. laminarity of the global target-to-slot sets \(N_C(S)\); or
5. every laminar-node load (3.1), rather than only the scalar bank shadows.

A sound sufficient theorem can therefore use either of two interfaces:

* an unrestricted PBBS-supported atlas satisfying (5.2)--(5.4); or
* a safe one-core \(C\) whose actual \(N_C(S)\) are laminar and satisfy
  every node inequality (3.1).

In the second interface, q1 is the sharp two-endpoint Hall problem (2.2).
For deeper levels, \(2q\) is only the capacity of the root bank \(B_q\);
all branch cuts are still required. Neither interface is currently proved
uniformly from PBBS flags.
