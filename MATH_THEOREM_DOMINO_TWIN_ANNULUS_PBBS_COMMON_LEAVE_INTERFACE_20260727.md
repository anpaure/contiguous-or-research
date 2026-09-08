# Domino-twin annulus to PBBS: the exact common-leave interface and the first-shadow obstruction

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Put

\[
 n=2m,\qquad W=\binom{2m}{m},\qquad
 q_0=a\sqrt m+O(1),\qquad H=b\sqrt m+O(1),
 \qquad 0<a<b,
\]

and let

\[
 r=m-q_0,\qquad D=H-q_0,\qquad
 V_d=\binom{[n]}{r-d},\qquad N_d=|V_d|.
\]

This note gives the deterministic annulus-to-compiler interface. Its
conclusions are as follows.

1. If one entrance matching of ordinary cyclic packets has constant mass
   \(G=N_0-L\) at every annular depth, then its lower hole count satisfies

   \[
   \boxed{
   \sum_{d=0}^{D}H_d
   =\underbrace{\sum_{d=0}^{D}(N_d-G)_+}_{B(L)}
    +\underbrace{\sum_{d=0}^{D}
       \left(\min\{G,N_d\}-|S_d|\right)}_{\mathfrak C}.}
   \tag{0.1}
   \]

   Here \(S_d\) is the support at depth \(d\). The upper annulus is its
   complement image, so the two-sided hole count is exactly
   \(2B(L)+2\mathfrak C\).

2. The weakest missing correlated-leave assertion is precisely

   \[
      \boxed{\mathfrak C=o(W).}
   \tag{0.2}
   \]

   It is neither a separate near-factor assertion at every rank nor a
   bound obtained by summing independent leaves. It is the floor-correct
   loss of distinct support of one common family of whole histories.

3. The scalar term is not automatically small from \(L=o(W)\). Uniformly
   in the Gaussian annulus,

   \[
   B(L)=O_a\left(L+\frac{L^2\sqrt m}{N_0}\right).
   \tag{0.3}
   \]

   Thus \(L=O(N_0/\sqrt m)\) is sufficient. More generally, for
   \(L/N_0=\delta\to0\) and \(\delta\sqrt m\to\infty\),

   \[
   B(L)=\left(\frac1{4a}+o(1)\right)
          N_0\delta^2\sqrt m.
   \tag{0.4}
   \]

   Hence the scalar threshold is \(\delta=o(m^{-1/4})\), not merely
   \(\delta=o(1)\).

4. An all-depth quarantine is automatically harmless if it contains
   \(o(W)\) **target-incidence edits after expansion through all depths**.
   Changing \(Q\) such incidences changes the aggregate hole count by at
   most \(Q\). This is the weakest uniform conclusion based only on the
   number of edits; a larger quarantine can of course be harmless when
   its edits are support-redundant. An \(o(W)\) set of entrance roots is
   not enough: its expanded annular shadow can contain order \(W\) or
   more incidences.

5. If the selected histories form \(p=O(W/m)\) legal rotor paths, the
   common-arrival compiler pays at most \(2Hp=o(W)\) in resets. Appending
   every remaining hole literally then proves the constant-one conclusion
   whenever (0.2), (0.3), and the expanded quarantine bound hold. No
   factor \(H\) multiplies the entrance leave.

6. The literal domino-twin realization does **not** satisfy (0.2). If a
   domino-twin matching covers \(N_0-L\) entrance targets and every
   selected superpacket is split into its two component cyclic packets,
   then, on the parity for which \(r\) is odd,

   \[
   \boxed{
   \mathfrak C\ge \widetilde E_1
      \ge \frac{N_0-L}{4}-O_a(W/\sqrt m).}
   \tag{0.5}
   \]

   Therefore a near-factor with \(L=o(W)\) has \(\Omega(W)\) holes already
   at the first deeper lower rank, and the same number on the upper shore.
   An \(o(W)\) incidence quarantine or an \(o(W)\)-length PBBS appendage
   cannot repair it.

The only surviving use of the domino-twin entrance factor is therefore a
global **re-bundling theorem**: repartition almost all of its covered
entrance roots into new, non-twin ordinary packet histories satisfying
(0.2). Choosing a different internal orientation of each selected domino
necklace is not such a re-bundling and does not remove (0.5).

## 1. One common packet family and its traces

For a directed cyclic order

\[
 \pi=(z_i)_{i\in\mathbb Z_n},
\]

write

\[
 I_\pi(i,k)=\{z_i,z_{i+1},\ldots,z_{i+k-1}\}.
\]

Let \(\Pi\) be a family of \(s\) ordinary cyclic packets which is a
matching at entrance rank \(r\). Thus its \(ns\) entrance intervals are
distinct. Put

\[
 G=ns=N_0-L.
\tag{1.1}
\]

The occurrence with entrance phase \((\pi,i)\) has lower trace

\[
 \tau_d(\pi,i)=I_\pi(i+d,r-d),\qquad 0\le d\le D.
\tag{1.2}
\]

Equivalently,

\[
 \tau_d(\pi,i)=I_\pi(i,r)\cap I_\pi(i+d,r).
\tag{1.3}
\]

The same \(\Pi\), not a new matching at depth \(d\), is used in (1.2).
Define

\[
 \mu_d(T)=|\{(\pi,i):\tau_d(\pi,i)=T\}|,
 \qquad
 S_d=\{T:\mu_d(T)>0\}.
\tag{1.4}
\]

Every packet has exactly \(n\) distinct cyclic intervals of every
positive proper length. Hence

\[
 \sum_{T\in V_d}\mu_d(T)=G
\tag{1.5}
\]

at every depth.

The corresponding upper trace is the complement of the lower trace:

\[
 [n]\setminus I_\pi(i+d,r-d)
 =I_\pi(i+r,n-r+d).
\tag{1.6}
\]

As \(i\) runs around the packet, (1.6) is a bijection of occurrences.
Consequently the upper load vector is the complement-image of the lower
load vector. In particular the two shores have exactly the same support
size, hole count, raw repeat count, and floor-correct repeat count.

## 2. Exact common-leave accounting

Let

\[
 E_d=\sum_{T\in V_d}(\mu_d(T)-1)_+,
 \qquad H_d=N_d-|S_d|.
\tag{2.1}
\]

Since every positive load contributes one unit to the support, (1.5)
gives

\[
 E_d=G-|S_d|,
 \qquad H_d=N_d-|S_d|.
\tag{2.2}
\]

Subtract the unavoidable scalar repeat floor:

\[
 \widetilde E_d=E_d-(G-N_d)_+.
\tag{2.3}
\]

Then

\[
 \boxed{
 \widetilde E_d
   =\min\{G,N_d\}-|S_d|
   =\min\{E_d,H_d\},}
\tag{2.4}
\]

and therefore

\[
 \boxed{H_d=(N_d-G)_++\widetilde E_d.}
\tag{2.5}
\]

Summing proves (0.1), with

\[
 B(L)=\sum_{d=0}^{D}(N_d-N_0+L)_+,
 \qquad
 \mathfrak C(\Pi)=\sum_{d=0}^{D}\widetilde E_d.
\tag{2.6}
\]

There is only one freely chosen entrance leave,

\[
 \mathcal L=V_0\setminus S_0.
\]

For \(d>0\), the hole family

\[
 \mathcal H_d(\Pi)=V_d\setminus S_d(\Pi)
\tag{2.6a}
\]

is induced by the same packet histories. It is not a separately chosen
leave \(\mathcal L_d\). Nor is it, in general, a set-theoretic shadow of
\(\mathcal L\) alone: collisions among retained histories contribute the
term \(\widetilde E_d\). Thus “one common leave serves all depths” means
exactly that one \(\Pi\) induces every \(\mathcal H_d\), with its total
cost evaluated by (0.1).

At the entrance, \(|S_0|=G\), so \(\widetilde E_0=0\). At later ranks,
the decreasing layer size supplies the scalar term \(B(L)\), while every
additional hole is exactly a loss of distinct support in
\(\mathfrak C\).

There are several exactly equivalent forms of the correlated term:

\[
 \boxed{
 \begin{aligned}
 \mathfrak C
 &=\sum_{d=0}^{D}
    \left[\min\{G,N_d\}-|S_d|\right]\\
 &=\sum_{d=0}^{D}\min\{E_d,H_d\}\\
 &=\frac12\sum_{d=0}^{D}
    \left(\|\mu_d-\mathbf1\|_1-|G-N_d|\right).
 \end{aligned}}
\tag{2.7}
\]

Thus (0.2) is not a convenient strengthening of what is needed. Once
\(B(L)=o(W)\), it is necessary and sufficient for \(o(W)\) aggregate
lower holes. By (1.6), the corresponding two-sided assertion is also
necessary and sufficient.

This explains precisely why independent rank leaves are the wrong bill.
If one found, separately at each of \(\Theta(\sqrt m)\) ranks, a matching
with \(\Theta(N_d/\sqrt m)\) leave, their sum would be \(\Theta(W)\).
For one common history family, the same entrance shortage contributes
only through \(B(L)\), and the remaining bill is the genuinely correlated
quantity \(\mathfrak C\).

## 3. The scalar common-leave bill

The exact layer ratio is

\[
 \frac{N_d}{N_0}
 =\prod_{j=0}^{d-1}
   \frac{r-j}{n-r+j+1}.
\tag{3.1}
\]

For \(d=O(\sqrt m)\), Taylor expansion of the logarithm gives, uniformly,

\[
 \frac{N_d}{N_0}
 =\exp\left(
   -\frac{2q_0d+d^2}{m}
   +O_a(m^{-1/2}+d/m)
   \right).
\tag{3.2}
\]

Put \(\delta=L/N_0\). A summand in \(B(L)\) is positive precisely when

\[
 1-\frac{N_d}{N_0}<\delta.
\tag{3.3}
\]

Because \(a>0\), (3.2) implies that (3.3) can hold for only

\[
 O_a(1+\delta\sqrt m)
\tag{3.4}
\]

values of \(d\). Every positive summand is at most \(L\). Therefore

\[
 B(L)=O_a\left(L+\frac{L^2\sqrt m}{N_0}\right),
\tag{3.5}
\]

which is (0.3).

For completeness, suppose \(\delta\to0\) and
\(\delta\sqrt m\to\infty\). The contributing depths then satisfy
\(d=o(\sqrt m)\), and (3.2) becomes

\[
 1-\frac{N_d}{N_0}
   =\frac{2ad}{\sqrt m}+o(\delta)
\tag{3.6}
\]

uniformly through the positive range. Thus that range ends at

\[
 d_*=(1+o(1))\frac{\delta\sqrt m}{2a},
\tag{3.7}
\]

and summing the arithmetic triangle gives

\[
 \begin{aligned}
 B(L)
 &=N_0\sum_{d\le d_*}
   \left(\delta-\frac{2ad}{\sqrt m}+o(\delta)\right)\\
 &=\left(\frac1{4a}+o(1)\right)
   N_0\delta^2\sqrt m.
 \end{aligned}
\tag{3.8}
\]

Since \(N_0=e^{-a^2+o(1)}W\), equations (3.5)--(3.8) prove all scalar
claims in Section 0. In particular, a stopped leave such as
\(L=\Theta(N_0/\log m)\) is \(o(W)\) but has

\[
 B(L)=\Theta_a\left(\frac{W\sqrt m}{\log^2m}\right),
\tag{3.9}
\]

so it does not cross the annular bridge even before trace collisions are
examined.

## 4. Quarantine is measured after all-depth expansion

The following elementary stability statement is the exact robust form
needed at the interface.

### Lemma 4.1 (incidence-edit Lipschitz bound)

Suppose two all-depth occurrence systems differ by \(Q\) insertions,
deletions, or replacements of individual target incidences, counted in
the disjoint union of all signed annular ranks. Then their aggregate hole
counts differ by at most \(Q\).

#### Proof

One incidence edit changes the support size at its rank by at most one,
and changes no other rank. The hole count is the layer size minus the
support size. Sum the one-edit bound along the edit sequence. \(\square\)

Accordingly, if \(\mathcal Q\) is a quarantine of target incidences and

\[
 |\mathcal Q|=o(W)
\tag{4.1}
\]

after both shores and all depths have been expanded, then

\[
 H_{\rm ann}^{\rm post}
 \le 2B(L)+2\mathfrak C+|\mathcal Q|.
\tag{4.2}
\]

The qualification “after expansion” is essential. If
\(\mathcal Q_0\) is instead a family of quarantined entrance occurrences,
let \(\operatorname{tr}_d(\mathcal Q_0)\) be its depth-\(d\) incidence
image along the selected histories. The safe quantity is

\[
 Q^\sharp=
 \sum_{\text{signs }\sigma}\sum_{d=0}^{D}
 |\operatorname{tr}^{\sigma}_d(\mathcal Q_0)|_{\rm inc},
\tag{4.3}
\]

not \(|\mathcal Q_0|\). Deterministically,

\[
 Q^\sharp\le2(D+1)|\mathcal Q_0|.
\tag{4.4}
\]

For example, \(|\mathcal Q_0|=\Theta(W/\sqrt m)=o(W)\) has
\(Q^\sharp=\Theta(W)\) when all its histories are discarded throughout
the Gaussian-width annulus. Thus the weakest uniform size hypothesis is
\(Q^\sharp=o(W)\), or any stronger statement implying it. A larger
expanded quarantine may still be harmless, but that requires an
additional support-cancellation statement.

## 5. Deterministic PBBS/compiler implication

We record the chronology statement in a form independent of how the
legal paths were found.

### Lemma 5.1 (hard-started common-arrival paths)

Suppose \(T\) selected radius-\(H\) states are partitioned into \(p\)
directed legal rotor paths. Let \(h_j\) be the number of missing masks at
signed depth \(-H\le j\le H\), and let

\[
 c_0=T-(W-h_0).
\]

Then there is a literal band word of length

\[
 \boxed{
 W+c_0+\sum_{j\ne0}h_j+2Hp.}
\tag{5.1}
\]

#### Proof

Write a state as

\[
 \omega=(A;z_1,\ldots,z_{2H};B),\qquad |A|=m-H,
\]

with displayed flags

\[
 C_{-H+t}(\omega)=A\cup\{z_1,\ldots,z_t\},
 \qquad 0\le t\le2H.
\]

Hard-start the first state of a path by the \(2H+1\) letters

\[
 \{z_{2H}\},\ldots,\{z_1\},A.
\]

Its suffix unions display all \(2H+1\) flags. Under a legal
common-arrival transition

\[
 C'_{-H}=C_{-H}-x+y,
 \qquad C'_j=C_{j-1}+y\quad(-H<j\le H),
\]

append the one letter \(C'_{-H}\). The suffix ending at that letter now
displays every \(C'_j\). Hence a path of \(u\) states costs exactly
\(u+2H\) letters, and all paths cost \(T+2Hp\).

Append every still-missing band mask as one literal letter. Since
\(T+h_0=W+c_0\), this gives (5.1). Windows crossing concatenation seams
can create additional witnesses but cannot destroy any displayed one.
\(\square\)

### Theorem 5.2 (weakest correlated-leave compiler theorem)

Assume the PBBS/inner compiler and the annular construction use one
common physical state family and satisfy all of the following:

1. the \(T\) successor letters of the common path family are the core
   body already charged in the baseline word; the annular masks are
   suffix flags of those same letters, rather than a second body to be
   concatenated;
2. the annular entrance shortage obeys \(B(L)=o(W)\);
3. the same whole annular histories obey \(\mathfrak C=o(W)\);
4. all discarded or altered all-depth target incidences have expanded
   count \(Q^\sharp=o(W)\);
5. the resulting states have a legal path cover with
   \(Hp=o(W)\).

Then the same core body can be compiled to cover all lower and upper
annular targets at total additional defect/reset cost \(o(W)\). In
particular, if the common PBBS/core body has baseline length \(W+o(W)\),
the combined controlled-band word also has length \(W+o(W)\).

#### Proof

Equations (0.1), (1.6), and Lemma 4.1 give

\[
 \sum_{\text{annular signed ranks}}h_j
 \le 2B(L)+2\mathfrak C+Q^\sharp=o(W).
\tag{5.2}
\]

Lemma 5.1 reuses the common successor letters and adds only reset toll
\(2Hp=o(W)\). Every remaining annular hole is then appended literally
once. No second copy of the \(T\)-letter core body, no independent rank
matching, and no sum of rankwise entrance leaves occurs. \(\square\)

For full cyclic packets one may cut each packet once, so
\(p\le s=G/n=O(W/m)\). Since \(H=O(\sqrt m)\),

\[
 2Hp=O(W/\sqrt m)=o(W).
\tag{5.3}
\]

Thus the only nonautomatic annular incidence input, after a critical
entrance leave has been obtained, is (0.2). This is the promised weakest
correlated-leave theorem.

## 6. The literal domino-twin split fails the interface

Assume now that \(r\) is odd. A simple domino-twin superpacket is an
unoriented cyclic necklace of \(m\) unordered dominoes. Choose any
orientation of each domino to obtain a cyclic order \(P\), and let
\(P^\tau\) be obtained by reversing the two entries in every domino.
For a cyclic order \(Q\), write

\[
 \mathcal I_k(Q)=\{I_Q(i,k):i\in\mathbb Z_n\}.
\tag{6.0}
\]

At the odd entrance length \(r\), the two cyclic decks are disjoint.

Let \(\mathcal M\) be a matching of \(T\) such superpackets and split
each selected superpacket into \(P,P^\tau\). Then

\[
 G=2nT=N_0-L.
\tag{6.1}
\]

At the first deeper rank the interval length is \(r-1\), which is even.
Exactly the \(m=n/2\) intervals whose endpoints lie on domino boundaries
are unions of whole consecutive dominoes. They occur in both \(P\) and
\(P^\tau\). No other interval is common: an interval beginning inside a
domino has one split choice at each boundary, and \(\tau\) changes those
choices. Hence

\[
 |\mathcal I_{r-1}(P)\cap\mathcal I_{r-1}(P^\tau)|=m.
\tag{6.2}
\]

For a target \(X\), let \(k_X\) be the number of selected twins whose
two component packets both contain \(X\). Its load satisfies
\(\mu_1(X)\ge2k_X\), and therefore

\[
 (\mu_1(X)-1)_+\ge k_X.
\]

Summing first over targets and then over selected twins gives

\[
 E_1\ge\sum_Xk_X=mT=\frac G4.
\tag{6.3}
\]

The scalar floor is at most

\[
 (G-N_1)_+
 \le N_0-N_1
 =N_0\frac{2q_0+1}{m+q_0+1}
 =O_a(W/\sqrt m).
\tag{6.4}
\]

Subtracting (6.4) from (6.3) proves

\[
 \widetilde E_1
 \ge\frac{N_0-L}{4}-O_a(W/\sqrt m),
\tag{6.5}
\]

which is (0.5). If \(L=o(W)\), then

\[
 H_1\ge\widetilde E_1=(1/4-o(1))N_0=\Omega_a(W).
\tag{6.6}
\]

Complementation gives the same upper-rank bound.

Lemma 4.1 shows that \(o(W)\) all-depth incidence edits leave
\(\Omega(W)\) holes. There is also a direct chronology lower bound. Fix
one target rank. For a fixed right endpoint, the unions of intervals
ending there are nested as the left endpoint moves left, so at most one
distinct union can have the prescribed cardinality. An appendage of
\(\ell\) new letters has only \(\ell\) new right endpoints and hence
creates at most \(\ell\) new targets at that rank. Therefore the holes in
(6.6) require \(\Omega(W)\) additional length. PBBS chronology cannot
turn (6.6) into an \(o(W)\) repair.

This obstruction is unaffected by choosing another internal orientation
of a selected domino necklace: every complementary decomposition obeys
(6.2). To destroy the obstruction while retaining component packets, one
must break all but \(o(W/n)\) intact twin pairs. Breaking one pair by
discarding a component loses \(n\) entrance incidences, so this costs
\(\Omega(W)\) entrance incidences. Equivalently, resolving the \(m\)
common first-shadow occurrences of each of \(\Theta(W/n)\) twins requires
\(\Omega(W)\) all-depth incidence edits.

## 7. Exact surviving re-bundling gate

Let

\[
 \mathcal A=V_0\setminus\mathcal L
\]

be the entrance family covered by the stopped domino-twin matching. The
following is the weakest physical escape which actually uses that output.

> **Correlated entrance re-bundling theorem.** After changing
> \(o(W)\) entrance incidences, partition the retained members of
> \(\mathcal A\) into ordinary cyclic packet decks \(\Pi'\), with one
> complement-coupled realization on the upper shore, such that
> \[
> p(\Pi')=O(W/m),\qquad
> \sum_{d=0}^{D}
> \left[\min\{G',N_d\}-|S_d(\Pi')|\right]=o(W),
> \tag{7.1}
> \]
> and the expanded incidence cost of all discarded or changed histories
> is \(o(W)\).

Subject also to the scalar condition \(B(N_0-G')=o(W)\), Theorem 5.2
then gives the annulus-to-PBBS/compiler bridge deterministically.

The stopped domino-twin near-factor supplies the large entrance set
\(\mathcal A\). It does not supply the partition \(\Pi'\), the support
inequality (7.1), or the common PBBS chronology. Conversely, no stronger
rankwise theorem is needed: (7.1) is exactly the floor-correct aggregate
defect which appears in the final length bill.

## 8. Final separation of proved and unproved statements

The following implications are now exact and unconditional.

1. One common family obeys the support ledger (0.1).
2. Complementation doubles, rather than changes, that ledger.
3. A critical scalar entrance leave costs only \(o(W)\) across the whole
   annulus.
4. An expanded \(o(W)\) incidence quarantine perturbs the total hole bill
   by only \(o(W)\).
5. A path cover of size \(O(W/m)\) has \(o(W)\) Gaussian-width reset toll.
6. Under (0.2), literal hole appending closes the deterministic compiler
   interface at coefficient one.
7. The intact domino-twin split violates (0.2) by a linear amount at
   depth one, even for a hypothetical critical entrance leave.

What remains open is not “use one leave at every rank”; that accounting is
already (0.1). The remaining positive theorem is the global non-twin
re-bundling assertion (7.1), or another construction which directly
produces one ordinary packet history family with the same correlated
support property.
