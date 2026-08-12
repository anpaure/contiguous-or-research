# PBBS centered projection: exact depth-two chronology, bounded loads, and the first return obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or web
input is used.

## Dependency scope

The only shadow theorem imported at the start is the independently
rechecked centered \(q=1\) statement: the centered edges form an exact
Johnson \(2\)-factor, their rank-\((m+1)\) union colors occur once, and
their rank-\((m-1)\) intersection colors have loads in \(\{1,2,3\}\)
with no holes. The PBBS successor/inverse parenthesis rules and the orbit
divisibility \(L\in n\mathbb Z\) are part of the definition/structural
input, not higher-shadow assumptions.

Sections 3--7 derive the \(q=2\) chronology, loads, and literal compiler
from those inputs. Section 8 records separately rechecked fixed-depth-three
facts to locate the first obstruction; none of them is used to prove the
\(q=2\) theorem.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\frac Wn=\operatorname {Cat}_m .                 \tag{0.1}
\]

Orient the canonical PBBS factor of \(KG(n,m)\). On one odd-graph
component write its states as \(A_t\), and let \(\lambda_t\) be the
unique coordinate outside \(A_t\cup A_{t+1}\). Its centered Johnson
projection consists of the step-two rows

\[
                         B_j=A_{\epsilon+2j}.         \tag{0.2}
\]

The audit gives the following exact conclusions.

1. Every centered row is cyclically depth-two geodesic. In particular,

   \[
   |B_j\cap B_{j+1}\cap B_{j+2}|=m-2,
   \qquad
   |B_j\cup B_{j+1}\cup B_{j+2}|=m+2.               \tag{0.3}
   \]

   The decisive fact is the independently checked PBBS no-gap-three
   theorem \(\lambda_t\ne\lambda_{t+3}\).

2. The lower depth-two loads obey the uniform theorem

   \[
   \boxed{1\le \mu_2^-(S)\le10
          \quad\left(S\in\binom{[n]}{m-2}\right).}   \tag{0.4}
   \]

   The upper depth-two loads are precisely opposite-parity PBBS
   first-shadow loads, so

   \[
   \boxed{1\le \mu_2^+(U)\le3
          \quad\left(U\in\binom{[n]}{m+2}\right).}   \tag{0.5}
   \]

   Thus there are no depth-two target holes at either sign.

3. If an original PBBS component has length \(\ell n\), its centered
   projection has exactly \(\gcd(2,\ell)\) components, each of length

   \[
                       \frac{\ell n}{\gcd(2,\ell)}.  \tag{0.6}
   \]

   Consequently the total number \(K\) of centered components satisfies

   \[
                              K\le B,                \tag{0.7}
   \]

   and every component has length at least \(n\).

4. There is an important compiler distinction. The rank-\(m\) rows
   \(B_j\) need not satisfy positive delay \(P_2\): a gap-five return
   creates a positive coordinate run of exactly two \(B\)-states.
   However the complementary rank-\((m+1)\) rows

   \[
                              X_j=[n]\setminus B_j   \tag{0.8}
   \]

   satisfy the full \(G_2+P_2\) interface. They therefore compile
   literally with four collar letters per component. The exact finite
   consequence is a word of length at most

   \[
                              W+4B                  \tag{0.9}
   \]

   covering every set in the five ranks

   \[
                              m-1,m,m+1,m+2,m+3.     \tag{0.10}
   \]

5. No orientation or cyclic rephasing makes these rows \(G_3\), hence
   none makes them \(H\)-safe for any \(H\ge3\). PBBS has exactly

   \[
                              n(m-1)                 \tag{0.11}
   \]

   physical consecutive gap-five starts. Each creates one three-transition
   repeated-coordinate segment. For \(m\ge3\), each also creates one unit
   of depth-three rank excess.
   Reversal and rephasing preserve the cyclic coordinate-run lengths;
   complement merely exchanges the lower and upper defect.

6. The obstruction (0.11) is polynomial and is negligible compared with
   \(W\). It is not a constant-one no-go. The genuine growing-window gate
   is the packing/transversal number of consecutive omitted-label returns
   of gaps at most \(2H-1\). Ordinary orientation and phase choices cannot
   change that invariant. A constant-one PBBS proof still needs a
   Catalan-scale bound for those returns and a growing-depth correct-support
   theorem. The PBBS dominance-staircase construction already supplies the
   required linear-cost crossing seam.

Thus the centered PBBS factor passes depth two completely and with bounded
loads. The first pointwise chronological failure is exactly depth three,
not depth two. The finite-depth-three failure is harmless; its
Gaussian-window descendants are the unresolved issue.

## 1. Centered projection and its exact component chronology

Let \(F\) be an oriented cycle factor of \(KG(n,m)\), not yet necessarily
PBBS. If \(A_t\) is a component of length \(L\), then the centered edge at
\(A_t\) joins its two factor neighbours:

\[
                              A_{t-1}A_{t+1}.         \tag{1.1}
\]

Both are \(m\)-sets contained in the \((m+1)\)-set \(A_t^c\), so they
are adjacent in \(J(n,m)\). Every vertex \(A_t\) is incident with the
centered edges at \(A_{t-1}\) and \(A_{t+1}\), and a Johnson edge has a
unique disjoint middle center. Hence the centered edges form a simple
spanning Johnson \(2\)-factor.

On indices modulo \(L\), this factor is the step-two graph

\[
                              t\longleftrightarrow t+2.       \tag{1.2}
\]

It has \(\gcd(2,L)\) components, each of length
\(L/\gcd(2,L)\).

For PBBS, every factor component has length

\[
                              L=\ell n,\qquad \ell\ge1,       \tag{1.3}
\]

and the sum of the levels \(\ell\) over all PBBS components is

\[
                              \sum_C\ell_C=\frac Wn=B.        \tag{1.4}
\]

Since \(n\) is odd,

\[
 \gcd(2,L)=\gcd(2,\ell).
\]

This proves (0.6). Moreover

\[
 K=\sum_C\gcd(2,\ell_C)
   \le\sum_C\ell_C=B,                               \tag{1.5}
\]

and \(\ell n/\gcd(2,\ell)\ge n\). Notice that the cruder bound
\(K\le2B\) is valid but loses an unnecessary factor two.

Rotating the starting index on one component only rephases (1.2), and
reversing the component replaces step \(+2\) by step \(-2\). Neither
operation changes any cyclic window multiset, coordinate-run length, or
component length.

## 2. Omitted-label recurrence and the exact local return invariant

The omitted-label recurrence on every oriented odd-graph row is

\[
 A_{t+2}=A_t-\{\lambda_{t+1}\}+\{\lambda_t\}.       \tag{2.1}
\]

For the centered parity row (0.2), put

\[
 a_j=\lambda_{\epsilon+2j},\qquad
 d_j=\lambda_{\epsilon+2j+1}.                       \tag{2.2}
\]

Then

\[
                         B_{j+1}=B_j-\{d_j\}+\{a_j\}.        \tag{2.3}
\]

Consecutive occurrences of a fixed PBBS omitted label have odd gap. Indeed,
after an edge labelled \(x\), the coordinate \(x\) is absent from the two
incident odd-graph states. At every subsequent edge not labelled \(x\),
the complement rule flips the membership of \(x\). It can therefore be
absent at both endpoints of the next \(x\)-edge only after an odd number of
odd-graph edges. Gap one would traverse the same simple factor edge
backwards and repeat a state, so it is excluded.

A
gap

\[
                              g=2s+1                 \tag{2.4}
\]

produces, on one parity row, an insertion followed by deletion of the same
coordinate in a segment of exactly \(s+1\) Johnson transitions. On the
opposite parity row the same two occurrences bound the reverse-sign segment
of \(s+2\) transitions. Since every projected component has length at least
\(2m+1\), the two appearances generated by one and the same omitted edge
require a block of at least \(m+1\) transitions. Therefore, for
\(1\le H\le m\),

\[
 \boxed{
 \text{every row of the centered factor is }G_H
 \Longleftrightarrow
 \text{the PBBS gap word has no consecutive gap }g\le2H-1.}
                                                               \tag{2.5}
\]

Here the equivalence is for the full collection of step-two rows (one row
when the PBBS component length is odd, two when it is even). Indeed, every Johnson
transition toggles the two labels displayed in (2.3). A repeated physical
coordinate among a block of transitions is exactly a second omitted-label
occurrence in the corresponding odd interval; conversely such a recurrence
toggles one coordinate twice and makes the segment nongeodesic.

The right side of (2.5) is invariant under rephasing. Reversal preserves
the state-row distance and therefore geodesicity directly, even though it
may represent the same short run by the complementary directed gap.
Complementation also preserves Johnson distance. Hence no combination of
these three operations can remove a violation of \(G_H\).

## 3. Independent check of the no-gap-three theorem

We give a direct two-sided parenthesis proof, avoiding any assumption about
the quotient return distribution. Use \(1\) for an up-step and \(0\) for a
down-step. Normalize a middle state \(A\) at its unique forward-unmatched
zero \(r\), so its rooted cyclic word is

\[
                              0_rD,                 \tag{3.1}
\]

where \(D\) is a Dyck word of semilength \(m\). Factor \(D\) into
primitive Dyck factors. Let

* \(p_+(D)\) be the first up-step which reaches the global height of \(D\);
* \(p_-(D)\) be the initial up-step of the last primitive factor having
  that global height;
* \(v(D)\) be the down-step immediately following the rightmost occurrence
  of the global height.

### Lemma 3.1 (two-sided distinguished deletions)

For the canonical PBBS map \(f\),

\[
 f^2(A)=(A\cup\{r\})\setminus\{p_+(D)\},          \tag{3.2}
\]

\[
 f^{-2}(A)=(A\cup\{v(D)\})\setminus\{p_-(D)\}.   \tag{3.3}
\]

Moreover, if \(m\ge2\), then

\[
                              p_+(D)\ne p_-(D).     \tag{3.4}
\]

#### Proof

Write \(D=P1_{p_+}Q\). After one PBBS step, root at \(p_+\). The
rooted word is

\[
                         0_{p_+}\,\overline Q\,0_r\,\overline P.
\]

The suffix is Dyck: \(\overline Q\) rises from zero to the old maximum,
the displayed \(0_r\) lowers once, and \(\overline P\) stays nonnegative
and ends at zero. Hence \(p_+\) is the next unmatched root. Since
\(f(A)=A^c\setminus\{r\}\), applying \(f\) once more gives (3.2).

For the backward formula write \(D=P0_vQ\). Reverse matching makes
\(v\) the reverse-unmatched root, and

\[
                         f^{-1}(A)=A^c\setminus\{v\}
\]

has, when rooted at \(v\), Dyck suffix

\[
                         \overline Q\,1_r\,\overline P.       \tag{3.5}
\]

Let \(C_*\) be the last primitive factor of \(D\) having maximum height,
and write \(P=LR\), where \(L\) is the concatenation of the primitive
factors preceding \(C_*\) and \(R\) is the nonempty prefix of \(C_*\)
ending immediately before \(v\). In (3.5), \(\overline Q\) never reaches
the old global height. The step \(1_r\) reaches it, and during
\(\overline P\) the current height is the old maximum minus the height
of the corresponding prefix of \(P\). It returns to the maximum exactly
when that prefix of \(P\) ends at height zero. The last such prefix is
\(L\); the next symbol is the complement of the initial up-step of
\(C_*\), hence a down-step. Thus the next reverse-unmatched root is that
initial up-step \(p_-(D)\), proving (3.3).

If the first and last maximum-height primitive factors differ, then
\(p_+\) and \(p_-\) lie in different factors. If they agree and the
height is at least two, \(p_-\) reaches height one while \(p_+\) reaches
the global height. If the height is one, every primitive factor is \(10\);
for \(m\ge2\) there are at least two of them, so the first and last such
factors differ. This proves (3.4). \(\square\)

It follows immediately that

\[
 f^{-2}(A)\cap A\cap f^2(A)
   =A\setminus\{p_-(D),p_+(D)\}                    \tag{3.6}
\]

has rank \(m-2\). Apply this with \(A=A_{t+2}\). From the recurrence
(2.1), a putative equality \(\lambda_t=\lambda_{t+3}\) would cause the
second centered transition to delete the coordinate inserted by the first,
so \(A_t\cap A_{t+2}\cap A_{t+4}\) would have rank \(m-1\), contrary to
(3.6). Therefore, for every \(m\ge2\),

\[
                              \boxed{\lambda_t\ne\lambda_{t+3}.} \tag{3.7}
\]

This also isolates the exceptional case: for \(m=1\), \(D=10\) and the
two distinguished up-steps coincide.

## 4. Pointwise depth-two geodesicity

Fix \(j\), suppress \(\epsilon\), and write

\[
 B_0=A_t,\quad B_1=A_{t+2},\quad B_2=A_{t+4}.       \tag{4.1}
\]

By (2.3), the only way that the second deletion can delete the first newly
inserted coordinate is

\[
 d_1=a_0
 \Longleftrightarrow
 \lambda_{t+3}=\lambda_t.                           \tag{4.2}
\]

This is excluded by (3.7). The two deletion labels are distinct, since
equal occurrences two positions apart would contradict the odd-gap rule.
Therefore

\[
 B_0\cap B_1\cap B_2
   =B_0\setminus\{d_0,d_1\},
 \qquad
 |B_0\cap B_1\cap B_2|=m-2.                        \tag{4.3}
\]

For the union, the second inserted coordinate \(a_1\) is outside \(B_1\).
If it belonged to \(B_0\), it would have to equal the first deleted
coordinate \(d_0\), but these are consecutive omitted labels and are
distinct. Also \(a_1\ne a_0\) by the odd-gap rule. Hence

\[
 B_0\cup B_1\cup B_2
   =B_0\cup\{a_0,a_1\},
 \qquad
 |B_0\cup B_1\cup B_2|=m+2.                        \tag{4.4}
\]

Equations (4.3)--(4.4) prove \(G_2\) pointwise on every centered
component. They also show exactly why first-shadow balance alone would not
have sufficed: the absent input was the return exclusion (3.7).

## 5. Exact lower depth-two loads

For

\[
                          S\in\binom{[n]}{m-2},       \tag{5.1}
\]

let

\[
 \mu_2^-(S)
 =\#\{(\epsilon,j):
        B_j\cap B_{j+1}\cap B_{j+2}=S\}.            \tag{5.2}
\]

The binary word of \(S\) has five forward-unmatched zeros. In cyclic order
write its canonical decomposition as

\[
 0_{z_0}D_0\,0_{z_1}D_1\,0_{z_2}D_2\,
 0_{z_3}D_3\,0_{z_4}D_4,                           \tag{5.3}
\]

where every \(D_i\) is a possibly empty Dyck word. Suppose first that
\(m\ge3\). At least one \(D_i\) is nonempty. Choose \(i\) for which the
height \(H_i\) of \(D_i\) is maximal, let \(u\) be the down-step
immediately following the rightmost occurrence of that maximum, and write

\[
                         D_i=P0_uQ.                 \tag{5.4}
\]

Change \(0_u\) to \(1_u\), writing the resulting ballot word as
\(D_i^\uparrow=P1_uQ\), and put

\[
                         A=S\cup\{z_i,u\}.          \tag{5.5}
\]

Rooting \(A\) at \(z_{i+4}\), its suffix is

\[
\begin{aligned}
D_{i+4}\,1_{z_i}D_i^\uparrow\,
0_{z_{i+1}}D_{i+1}\,
0_{z_{i+2}}D_{i+2}\,
0_{z_{i+3}}D_{i+3}.                                \tag{5.6}
\end{aligned}
\]

This is Dyck. After \(D_{i+4}\) returns to zero, the successive displayed
baselines are \(1,3,2,1,0\). The factor beginning at \(1_{z_i}\) and
ending at \(0_{z_{i+3}}\) is primitive and has height \(H_i+2\).
Every factor outside it has height at most \(H_i\); within it, the step
\(u\) is the first step reaching height \(H_i+2\). Thus it is the unique
tallest primitive factor, its initial up-step is \(z_i\), and its first
global-maximum up-step is \(u\). Lemma 3.1 therefore gives

\[
 p_-(A)=z_i,\qquad p_+(A)=u,
\]

and hence

\[
                         f^{-2}(A)\cap A\cap f^2(A)=S.         \tag{5.7}
\]

This is a literal oriented centered window, proving
\(\mu_2^-(S)\ge1\). For \(m=2\), \(S=\varnothing\); the rooted word
\(0\,1100\) has two distinct distinguished up-steps, and (3.6) gives the
same conclusion.

For the cap, every correct two-edge path deletes two distinct initial
extras. Reverse parenthesis monotonicity (equivalently, the one-flip
reverse-unmatched-zero rule applied twice) places both extras in the five
reverse-unmatched zeros \(U_-(S)\) of the deficit-five word of \(S\).
To recall the local rule: after cutting a deficit word at its
reverse-unmatched zeros, every intervening block is reverse-Dyck; changing
a zero to a one removes that marked zero and the next marked zero in the
reverse order (or the next two marks if the changed zero was unmarked).
Thus unmatched-zero sets can only shrink through the old marked set as
the two extras are restored. Applied backwards to the two deletions in
the occurrence, this puts both deleted extras in \(U_-(S)\).
Their unordered pair determines the initial middle state \(S\cup E\), and
the deterministic map \(f^2\) then determines the oriented path. Therefore

\[
                              \mu_2^-(S)\le\binom52=10.       \tag{5.8}
\]

This proves (0.4). For \(m\ge8\), the balanced floor is one, since

\[
 \frac{W}{\binom{2m+1}{m-2}}
 =\frac{(m+2)(m+3)}{m(m-1)}<2.                     \tag{5.9}
\]

Complete support and total occurrence mass give the exact excess

\[
\begin{aligned}
 R_2
 &=W-\binom{2m+1}{m-2}\\
 &=\frac{6(m+1)}{(m+2)(m+3)}W
 <12B.                                               \tag{5.10}
\end{aligned}
\]

In particular,

\[
 \sum_S(\mu_2^-(S)-1)=R_2,                          \tag{5.11}
\]

the total overload above an optimally chosen \(\{1,2\}\) baseline is at
most \(R_2\), and

\[
 \sum_S\binom{\mu_2^-(S)-1}{2}
 \le4R_2<48B.                                       \tag{5.12}
\]

The numerical inequality (5.12) is valid for every \(m\ge2\); only its
interpretation as the floor-one corrected collision energy uses
\(m\ge8\). The load cap ten and the excess identity (5.11) are valid for
every \(m\ge2\). The much sharper Catalan estimate is the aggregate fact
relevant to a coefficient-one ledger.

## 6. Upper depth-two loads are first-shadow loads

For three consecutive centered states with old PBBS indices restored,
adjacent odd-graph disjointness gives

\[
 \boxed{
 (A_t\cup A_{t+2}\cup A_{t+4})^c
   =A_{t+1}\cap A_{t+3}.}                           \tag{6.1}
\]

Indeed, the right side is contained in the left side. By (4.4), both have
size \(m-1\), so equality follows.

Consequently complementing an upper depth-two target identifies its load
with the PBBS first-shadow load on the opposite parity row. Under the
audited centered-projection hypothesis

\[
 1\le\mu_1(T)\le3
 \qquad\left(T\in\binom{[n]}{m-1}\right),           \tag{6.2}
\]

equation (6.1) proves (0.5). If \(a_i\) counts first-shadow targets of
load \(i\), then

\[
 a_2+2a_3
 =W-\binom{2m+1}{m-1}
 =\frac{2W}{m+2},                                   \tag{6.3}
\]

and hence

\[
                              a_3\le\frac{W}{m+2}.   \tag{6.4}
\]

Thus the upper depth-two bad-load mass is also \(O(B)\).

## 7. Positive delay and the exact choice of physical owners

Depth-two geodesicity \(G_2\) does not by itself give the \(P_2\) needed
by the literal atom compiler. This distinction is real here.

Suppose

\[
                              \lambda_t=\lambda_{t+5}=x       \tag{7.1}
\]

are consecutive occurrences. On the parity row containing \(A_t\), the
first occurrence inserts \(x\), while the second deletes it. Therefore
the cyclic indicator of \(x\) on that rank-\(m\) row contains a positive
run of exactly two states. Reversal preserves that run length, and
rephasing merely changes its starting index. Hence the centered rank-\(m\)
family generally fails \(P_2\).

Now pass to the complementary parity rows

\[
                              X_j=[n]\setminus B_j.   \tag{7.2}
\]

Their transition recurrence is

\[
 X_{j+1}=X_j-\{a_j\}+\{d_j\}.                       \tag{7.3}
\]

If consecutive occurrences of a coordinate have gap \(2s+1\), the first
occurrence which deletes it from the \(A\)-row inserts it into the
\(X\)-row, and the next occurrence removes it after exactly \(s+1\)
\(X\)-states. Thus its positive \(X\)-residence has \(s+1\) states. The no-gap-three theorem
gives \(s\ge2\), so every nonconstant positive run has at least three
states. Thus

\[
                              X\text{ satisfies }P_2.         \tag{7.4}
\]

Complement preserves \(G_2\), so the \(X\)-rows satisfy the full
\(G_2+P_2\) physical interface.

Put

\[
                              D_j=X_j\cap X_{j+1}\cap X_{j+2}. \tag{7.5}
\]

On a component of length \(L\), emit cyclically

\[
 D_0,D_1,\ldots,D_{L-1},D_0,D_1,D_2,D_3.            \tag{7.6}
\]

Positive delay gives the exact erosion/dilation identities

\[
\begin{aligned}
 D_i&=X_i\cap X_{i+1}\cap X_{i+2},\\
 D_i\cup D_{i+1}&=X_{i+1}\cap X_{i+2},\\
 D_i\cup D_{i+1}\cup D_{i+2}&=X_{i+2},\\
 D_i\cup\cdots\cup D_{i+3}&=X_{i+2}\cup X_{i+3},\\
 D_i\cup\cdots\cup D_{i+4}
   &=X_{i+2}\cup X_{i+3}\cup X_{i+4}.              \tag{7.7}
\end{aligned}
\]

Restoring the old PBBS indices, the five designated window families and
their loads are

\[
\begin{array}{c|c|c}
\text{atom window}&\text{PBBS identity}&\text{designated load}\\ \hline
D_i&
 (A_t\cup A_{t+2}\cup A_{t+4})^c
   =A_{t+1}\cap A_{t+3}&1\text{--}3\\
D_i\cup D_{i+1}&
 (A_{t+2}\cup A_{t+4})^c=A_{t+3}&1\\
D_i\cup D_{i+1}\cup D_{i+2}&A_{t+4}^c&1\\
D_i\cup\cdots\cup D_{i+3}&
 (A_{t+4}\cap A_{t+6})^c&1\text{--}3\\
D_i\cup\cdots\cup D_{i+4}&
 (A_{t+4}\cap A_{t+6}\cap A_{t+8})^c&1\text{--}10 .
\end{array}                                                    \tag{7.8}
\]

The ranks of these rows are \(m-1,m,m+1,m+2,m+3\), respectively.
Thus the five right sides range over all targets in (0.10), by (0.4),
(0.5), middle ownership, and complementation. The load statements in
(7.8) count the designated within-block witnesses; accidental
cross-component intervals can only add witnesses and are irrelevant.

The base portions of (7.6) total \(W\), while the four-letter collars
total at most \(4K\le4B\). This proves (0.9).

The collar constant four is exact for the support-blind cyclic atom chart:
the top depth-two witness in (7.7) uses five consecutive atoms, so a
window starting at the last base atom requires four copied prefix atoms.
There is no intercomponent seam charge because every certified interval is
kept inside its displayed component word.

## 8. The exact depth-three obstruction

This section uses two separately and independently rechecked PBBS
fixed-depth lemmas: the complete gap-five classification, and the
deficit-seven correct-support corridor. They are recorded here to identify
the next gate, but they are not dependencies of Sections 3--7.
Their full proofs are in PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md,
Sections 18--20, and PBBS_Q3_DEFICIT7_COMPLETE_SUPPORT_20260725.md,
respectively.

PBBS has gap-five returns for every \(m\ge2\). Their complete quotient
classification is

\[
 D=(10)^a1(10)^b0,
 \qquad a\ge0,\quad b\ge1,\quad a+b=m-1.            \tag{8.1}
\]

There are \(m-1\) quotient roots and \(n\) spatial phases, hence exactly
\(n(m-1)\) physical starts.

At such a start choose the parity on which the first occurrence of
\(x\) is an insertion. Over the three centered transitions the coordinate
history is

\[
                         0\longrightarrow1\longrightarrow1
                          \longrightarrow0.          \tag{8.2}
\]

Thus one coordinate is toggled twice, and the segment is not geodesic.
For \(m\ge3\), more explicitly, the other two deleted coordinates are
distinct and

\[
 \left|B_j\cap B_{j+1}\cap B_{j+2}\cap B_{j+3}\right|
 =m-2                                                     \tag{8.3}
\]

instead of the depth-three value \(m-3\). For \(m\ge3\), summing over all windows, every
gap-five start contributes exactly one unit, giving the exact rank-excess
identity

\[
                              E_3=n(m-1).             \tag{8.4}
\]

On the complementary row, (8.2) becomes
\(1,0,0,1\). The defect is then an upper-union defect instead of a lower-
intersection defect. Hence complement cannot restore \(G_3\). Reversal
and rephasing preserve the state pattern up to reversal/rotation. This
proves the claimed orientation-independent obstruction.

The normalized size is tiny:

\[
                              \frac{n(m-1)}W\longrightarrow0. \tag{8.5}
\]

One may cut or repair every depth-three bad window at polynomial total
cost. Thus (8.4) forbids a pointwise \(H\)-safe claim but does not threaten
constant one by itself.

There is also a stronger positive statement at the same depth. If only
rank-correct four-state windows are counted, then, for \(m\ge3\), the audited seven-mark
corridor gives

\[
 \boxed{
 1\le \mu_{3}^{-,\mathrm{corr}}(S)\le35
 \quad\left(S\in\binom{[n]}{m-3}\right).}           \tag{8.6}
\]

The cap is \(\binom73\): the three distinct initial extras later deleted
belong to the seven reverse-unmatched zeros of \(S\), and their three-set
determines the deterministic PBBS path. Thus depth three has complete
correct support even though it is not pointwise geodesic. Since a
three-transition block contains only six consecutive omitted-label
positions, no-gap-three and the odd-gap rule allow at most the single
gap-five repetition joining its two endpoints. Hence every bad window has
excess exactly one, and the number of bad windows is also \(n(m-1)\).
Consequently

\[
 \sum_S\bigl(\mu_{3}^{-,\mathrm{corr}}(S)-1\bigr)
 =W-n(m-1)-\binom{2m+1}{m-3},                       \tag{8.7}
\]

which is nonnegative and is less than

\[
 W-\binom{2m+1}{m-3}
 =\frac{12(m^2+2m+2)}{(m+2)(m+3)(m+4)}W
 <24B.                                               \tag{8.8}
\]

Thus the exact next obstruction is chronological return control, not a
new fixed-depth target Hall deficit.

For \(m\ge3\), the same ledger gives a completely literal fixed-depth repair. Four-fold
erosion on the complementary rows uses six copied prefix atoms per
component. A positive run of length three can spoil at most

\[
                              1+2+3+4+5+6=21          \tag{8.9}
\]

of the intended dilation windows, and such runs are precisely the
gap-five returns. Appending each spoiled intended target literally gives
the finite bound

\[
 \boxed{
 W+6B+21n(m-1)}                                     \tag{8.10}
\]

for a word covering all seven ranks

\[
                              m-2,m-1,m,m+1,m+2,m+3,m+4.      \tag{8.11}
\]

Both error terms in (8.10) are \(o(W)\). This is a genuine bounded-depth
positive theorem, but seven ranks are still far too narrow for the
Gaussian-above tail interface.

## 9. General \(H\): the exact surviving return-packing gate

Fix \(1\le H\le m-1\). This conservative finite range makes every
protected window shorter than every projected component and is the range
used by the central-band compiler.

There are two local conditions in the literal compiler, so the cut object
must record both; \(G_H\) alone is not enough. On a complementary centered
component \(C=(X_j)\), define \(\mathcal I_H(C)\) to contain the following
circular intervals of transition edges.

1. For each coordinate, include the minimal interval containing two
   consecutive toggles when that interval has at most \(H\) transitions.
   These are exactly the minimal \(G_H\)-violations.
2. For each nonconstant positive coordinate run having \(r\le H\) owner
   states, include the interval from its insertion boundary through its
   deletion boundary. It has \(r+1\) transitions. These are exactly the
   minimal \(P_H\)-violations.

For a consecutive omitted-label gap

\[
                              g=2s+1,                \tag{9.1}
\]

one step-two phase contains the two toggles in a block of \(s+1\)
transitions, while the other contains a positive complementary run of
\(s+1\) owner states, bounded by \(s+2\) transitions. Hence the gap
contributes to \(\mathcal I_H\) precisely when \(g\le2H-1\), through the
two associated bad arcs in the full step-two row collection. Conversely
every interval in \(\mathcal I_H\) arises from such a consecutive gap. This is the exact
off-by-one form of the return dictionary.

Let \(\nu_H(C)\) be the maximum number of pairwise edge-disjoint intervals
in \(\mathcal I_H(C)\), and let \(\tau_H(C)\) be its minimum edge
transversal. Then

\[
                       \nu_H(C)\le\tau_H(C)\le\nu_H(C)+1.    \tag{9.2}
\]

For completeness, choose any transition edge \(e\). The intervals
containing \(e\) are stabbed by \(e\); after deleting them and cutting the
circle at \(e\), the remaining family is an interval family on a line, for
which the greedy right-endpoint algorithm gives equality of packing and
transversal numbers. Its packing number is at most \(\nu_H(C)\), proving
the upper bound in (9.2); the lower bound is immediate.

Cutting a transversal makes every remaining open path internally
\(G_H+P_H\): any surviving violation would contain one of the minimal
intervals just defined. Conversely, every decomposition into internally
\(G_H+P_H\) paths must cut every member of \(\mathcal I_H(C)\).
Therefore the exact chronological cut parameter is

\[
                              J_H:=\sum_C\tau_H(C),   \tag{9.3}
\]

equivalently up to the at most \(K\) additive term in (9.2), the aggregate
packing \(\sum_C\nu_H(C)\).

This two-family parameter is equivalent up to an absolute factor to the
older one-sided PBBS positive-residence parameter. Let
\(\mathcal R_H\) retain only the positive-run arcs in item 2, and write
\(\tau_H^P,\nu_H^P\) for its aggregate transversal and packing numbers.
For a short gap, call its \(s+1\)-edge negative/G arc \(N_i\) and its
\(s+2\)-edge positive/P arc \(R_i\). If a cut set \(T\) meets every
\(R_i\), then \(T\) together with the two adjacent index shifts
\(T-1,T+1\), taken in the original PBBS index and hence allowed to pass
between the two step-two phases, meets every \(N_i\) as well. Hence

\[
             \tau_H^P\le J_H\le3\tau_H^P.           \tag{9.3a}
\]

On each active circular component, (9.2) applied to the \(R_i\)'s gives
\(\tau_H^P\le\nu_H^P+K_P\), where \(K_P\) is the number of active
positive-residence components. Since every such component contains a
packable arc, \(K_P\le\nu_H^P\). Therefore

\[
                         J_H\le6\nu_H^P.             \tag{9.3b}
\]

Thus adding the missing \(G_H\) shore strengthens the old residence gate
by only an absolute factor; it does not create a new asymptotic scale.

Let \(K_{\rm act}\) be the number of components with
\(\mathcal I_H(C)\ne\varnothing\). An inactive component remains cyclic
and costs \(2H\) collar letters; an active component cut
\(\tau_H(C)\) times becomes that many open paths and costs
\(H\tau_H(C)\). Thus the sharp collar after this cut scheme is

\[
                 2H(K-K_{\rm act})+HJ_H.             \tag{9.4}
\]

In particular it is at most

\[
                              2HK+HJ_H.              \tag{9.5}
\]

Here

\[
                              2HK\le2HB
                              =\frac{2H}{n}W=o(W)
\]

whenever \(H=o(m)\). Thus the additional cut requirement is
\(HJ_H=o(W)\).

There is a separate support charge. A bare cut loses exactly \(q\)
cyclic lower starts and \(q\) cyclic upper starts at depth \(q\).
Consequently support-blind restoration through depth \(H\) costs at most

\[
                   2\sum_{q=1}^{H}q
                     =H(H+1)                       \tag{9.6}
\]

literal singleton repairs per cut. Blind repair therefore requires
\(H^2J_H=o(W)\). If instead the actual aggregate post-cut target holes
are proved to be \(o(W)\), or a crossing chart repairs them for
\(O(H)\) letters per cut, the weaker and sharp collar condition
\(HJ_H=o(W)\) suffices.

For PBBS the linear crossing alternative is not merely hypothetical. The
independently audited dominance-staircase seam, valid when
\(2H\le m+1\), uses \(4H-1\) letters per active cut and restores every
floor-correct lower crossing occurrence and every upper crossing
occurrence. Together with the \(H\)-letter open-path collar, its exact
central charge is

\[
                  W+2H(K-K_{\rm act})+(5H-1)J_H.    \tag{9.6a}
\]

Thus, conditional on pre-cut correct target support, \(HJ_H=o(W)\)
really is sufficient. The seam theorem is proved and audited in
MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md and
PBBS_DOMINANCE_STAIRCASE_INDEPENDENT_AUDIT_20260725.md.

There are two implication scopes. The generic factor-blind
rank-correct compiler requires the full \(G_H+P_H\) parameter \(J_H\).
The PBBS-specific endpoint-capped erosion/seam construction can tolerate
extra wrong-rank windows and uses only the one-sided positive-residence
transversal \(\tau_H^P\), provided an independent theorem supplies all
designated correct targets. Equations (9.3a)--(9.3b) show that these two
chronology gates differ by only an absolute factor, but the target-support
hypothesis cannot be dropped in either formulation.

If one additionally imports the separately audited global-maximum
all-depth PBBS correct-support corridor, then that hypothesis is discharged:
the dominance seam preserves the selected correct occurrences across the
cuts. Under that larger theorem package, the sole remaining
PBBS-specific quantitative chronology gate is the Catalan estimate

\[
                  \nu_H^P=O_A(B),
                  \qquad H=\lceil A\sqrt m\rceil,    \tag{9.6b}
\]

for every fixed \(A\). This report does not use or reprove the all-depth
corridor, in accordance with its stated \(q=1\)-only starting scope.

For fixed \(A\), a Catalan-scale theorem

\[
             J_{\lceil A\sqrt m\rceil}=O_A(B)        \tag{9.7}
\]

would make the linear collar/seam cost

\[
 O_A(HB)=O_A\!\left(\frac{W}{\sqrt m}\right)=o_A(W). \tag{9.8}
\]

Within the present \(q=1\)-only input scope, it would not by itself prove
constant one: one must also prove that the
literal-valid lower and upper targets remaining through every
\(q\le H\) have aggregate hole count \(o_A(W)\). The depth-two bounded
loads prove that statement only for \(q=2\). At growing \(q\), safety
controls rank but not collisions or target support.

After the standard diagonal choice of \(A\), (9.7), the audited linear
crossing repair (or direct post-cut hole control), and an independent growing-depth
support theorem would compose into the constant-one endgame. No
orientation, rephase, or complement can establish these new estimates:
those operations preserve the cyclic toggle/run interval system and the
target-window multisets. A new aggregate PBBS return theorem or a
chronology-changing refactorization is required.

## 10. Precise proved boundary

The following statements are proved in this audit.

* The centered projection is an exact Johnson factor, with component
  chronology (0.6)--(0.7).
* Every centered PBBS row is \(G_2\).
* Every lower depth-two target occurs between one and ten times.
* Every upper depth-two target occurs between one and three times.
* The complementary physical rows satisfy \(G_2+P_2\) and give the exact
  five-rank word bound \(W+4B\).
* General \(G_H+P_H\) chronology is exactly the two-family short-return
  transversal problem of Section 9.

The following separately audited fixed-depth inputs are used only in
Section 8.

* The exact gap-five classification gives \(n(m-1)\) starts; the local
  calculation here then proves their orientation-, phase-, and
  complement-invariant \(G_3\) obstruction and exact aggregate excess.
* The deficit-seven corridor gives correct depth-three load \(1\)--\(35\)
  and aggregate excess below \(24B\).
* Its erosion repair gives (8.10), hence \(W+o(W)\) for the seven fixed
  ranks when \(m\ge3\).
* The dominance-staircase seam gives the linear cut charge (9.6a) under
  \(2H\le m+1\), conditional on pre-cut correct support.

The following are not proved here.

* No growing-window Catalan bound such as (9.7) is proved.
* Orientation, rephasing, and complementation cannot improve the value of
  that parameter; they leave the interval system unchanged.
* The depth-two bounded-load theorem alone does not imply constant one,
  because a product-SCD tail is negligible only after the protected radius
  grows faster than \(\sqrt m\).
* A chronology-changing splice or a new PBBS return-packing theorem could
  still close the route. The depth-three witness is not a no-go against
  either possibility.
