# PBBS towers to ordinary annular packets: the exact stopped-profile coupling and FIFO bundling gate

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Work first on the native PBBS ground set of size

\[
 K=2m+1,
 \qquad
 W^+=\binom{2m+1}{m}.
\]

Put

\[
 q_0=a\sqrt m+O(1),\qquad H=b\sqrt m+O(1),
 \qquad 0<a<b,
\]

\[
 J=H-q_0,qquad R=m-q_0,qquad
 V_d=\binom{[K]}{R-d},\qquad N_d=|V_d|.
\]

The ordinary stopped-profile identity is purely set-theoretic and holds
unchanged for odd \(K\). Since

\[
 W^+=\frac{2m+1}{m+1}\binom{2m}{m},
\]

the two central normalizations have the same little-oh scale.

The conclusions are as follows.

1. The complete canonical PBBS occurrence tower is genuinely
   all-depth: at every depth its correct occurrences cover every target
   and have zero floor-correct excess. But its correct mass is
   depth-dependent. If \(b_d\) starts have died by depth \(q_0+d\), the
   live mass is \(M-b_d\). An ordinary cyclic packet family has one
   constant mass \(M\) at every depth. Therefore the full PBBS tower is
   not itself one ordinary correlated leave.

2. Let \(P_d\) be the support of the live depth-\(d\) PBBS occurrences
   of a selected entrance section of size \(M\), and let \(O_d\) be the
   support after extracting ordinary cyclic histories on the same
   entrance mass. Then the exact coupling identity is

   \[
   \boxed{
   \mathfrak C^{\rm ord}
   =\mathfrak C^{\rm PBBS}_{\rm live}
    +\mathfrak R_{\rm mort}
    +\mathfrak B_{\rm ext},}
   \tag{0.1}
   \]

   where

   \[
   \mathfrak C^{\rm PBBS}_{\rm live}
   =\sum_d\bigl(\min\{M-b_d,N_d\}-|P_d|\bigr),
   \tag{0.2}
   \]

   \[
   \mathfrak R_{\rm mort}
   =\sum_d
     \bigl(\min\{M,N_d\}-\min\{M-b_d,N_d\}\bigr),
   \tag{0.3}
   \]

   and

   \[
   \mathfrak B_{\rm ext}
   =\sum_d(|P_d|-|O_d|).
   \tag{0.4}
   \]

   The last term is signed: new seam-crossing ordinary targets may
   compensate for PBBS targets lost in extraction.

3. If the extracted ordinary packets are ordered and
   \(\Delta_j^{\rm ord}\) is their realized stopped-profile increment,
   then

   \[
   \boxed{
   \sum_j\Delta_j^{\rm ord}
   =\mathfrak C^{\rm PBBS}_{\rm live}
    +\mathfrak R_{\rm mort}
    +\mathfrak B_{\rm ext}.}
   \tag{0.5}
   \]

   For a random extraction law, if
   \(\mathscr P_j^{\rm ord}
   =\mathbb E[\Delta_j^{\rm ord}\mid\mathcal F_j]\), then the
   corresponding equality holds after taking expectations.

   Thus (0.1) is the exact PBBS-to-stopped-profile interface, not an
   additional sufficient surrogate.

4. A clean positive route would select

   \[
   \mathcal X\subseteq\Omega_H,
   \qquad
   M=N_0-O(N_0/\sqrt m),
   \]

   with entrance targets injective and
   \(\mathfrak C^{\rm PBBS}=o(W^+)\), and then extract ordinary cycles
   with \(\mathfrak B_{\rm ext}=o(W^+)\). The complete PBBS support
   theorem does not provide such a section. It proves only full support
   before thinning. The full coordinate-conjugate fan library does admit
   an exact zero-excess safe section, but its conjugate depends on the
   root and hence supplies no common successor factor to bundle.

5. Cyclic bundling has an exact pointwise obstruction. A rank-\(R\)
   Johnson cycle

   \[
   A_{i+1}=A_i-\{u_i\}+\{v_i\},\qquad i\in\mathbb Z_K,
   \]

   is the deck of one ordinary cyclic coordinate order if and only if

   \[
   \boxed{
   (u_i)_{i\in\mathbb Z_K}\text{ is a permutation of }[K],
   \qquad v_i=u_{i+R}.}
   \tag{0.6}
   \]

   PBBS local fan correctness and geodesicity imply neither part of
   (0.6).

6. If a rebundling changes \(t\) successor seams, then at depth \(d\)
   at most \(dt\) retained PBBS window occurrences cross deleted seams.
   Consequently

   \[
   \boxed{
   \sum_{d=1}^{J}
   |P_d\setminus O_d|
   \le \frac{J(J+1)}2,t.}
   \tag{0.7}
   \]

   New seam targets can reduce the actual signed loss, but (0.7) is the
   best automatic inheritance bound. Since
   \(J^2=\Theta(m)\), Catalan-scale sewing
   \(t=\Theta(W^+/K)=\Theta(W^+/m)\) has a possible
   \(\Theta(W^+)\) all-depth footprint. Hence an \(o(W^+)\) edge edit
   theorem is not enough; one needs a signed seam-target theorem.

7. The upper tower is not independent:

   \[
   U_q(X)=[K]\setminus L_{q-1}(fX).
   \tag{0.8}
   \]

   An arbitrary good lower PBBS section need not respect this shifted
   phase pairing. An ordinary cyclic packet automatically does. Thus
   upper complement coherence is part of the FIFO bundling gate, not a
   separate rankwise choice.

Therefore the PBBS all-depth tower does not currently yield
\(\mathfrak C=o(W)\) after cyclic packet extraction. There is also no
proved positive-density no-go against every extraction. The exact
remaining theorem is a common-section plus FIFO sewing theorem whose
signed extraction functional in (0.4), rather than its number of seams,
is \(o(W)\).

## 1. The ordinary stopped profile on the PBBS ground set

For a cyclic order \(\pi=(z_i)_{i\in\mathbb Z_K}\), write

\[
 I_\pi(i,k)=\{z_i,z_{i+1},\ldots,z_{i+k-1}\}.
\]

Its depth-\(d\) ordinary deck is

\[
 E_d(\pi)=\{I_\pi(i,R-d):i\in\mathbb Z_K\}.
\tag{1.1}
\]

Let \(\Pi\) be an entrance matching of \(s\) such packets. Put

\[
 G=Ks,
 \qquad
 O_d=\bigcup_{\pi\in\Pi}E_d(\pi).
\tag{1.2}
\]

Every packet contributes exactly \(K\) occurrences at every depth.
Hence its floor-correct support loss is

\[
 \widetilde E_d^{\rm ord}
 =\min\{G,N_d\}-|O_d|,
\tag{1.3}
\]

and

\[
 \mathfrak C^{\rm ord}
 =\sum_{d=0}^{J}\widetilde E_d^{\rm ord}.
\tag{1.4}
\]

Order the packets as \(\pi_1,\ldots,\pi_s\). After \(j\) packets let
\(G_j=Kj\), let \(O_{d,j}\) be the current support, and define

\[
 c_{d,j}
 =\min\{G_j+K,N_d\}-\min\{G_j,N_d\},
\tag{1.5}
\]

\[
 Z_{d,j}
 =|E_d(\pi_{j+1})\setminus O_{d,j}|.
\tag{1.6}
\]

Then

\[
 \boxed{
 \Delta_j^{\rm ord}:=\sum_{d=0}^{J}(c_{d,j}-Z_{d,j}),
 \qquad
 \mathfrak C^{\rm ord}=\sum_{j=0}^{s-1}\Delta_j^{\rm ord}.}
\tag{1.7}
\]

Indeed, adding one packet raises scalar support capacity by \(c_{d,j}\)
and actual support by \(Z_{d,j}\). Equation (1.7) is the deterministic
ordinary stopped-profile identity.

## 2. What the complete PBBS tower actually supplies

Let \(f\) be the canonical cyclic parenthesis map on the middle layer
\(\binom{[K]}m\), and let

\[
 g=f^2.
\]

For a PBBS start \(X\), put

\[
 L_q(X)=\bigcap_{h=0}^{q}g^hX,
\tag{2.1}
\]

and define its rank excess by

\[
 \eta_q(X)=|L_q(X)|-(m-q)\ge0.
\tag{2.2}
\]

The exact departure formula shows

\[
 \eta_{q+1}(X)-\eta_q(X)\in\{0,1\}.
\tag{2.3}
\]

Thus correctness is absorbing backwards: if a start is correct at depth
\(q+1\), it is correct at depth \(q\), while a start which has failed can
never become correct again. Put

\[
 \Omega_q=\{X:\eta_q(X)=0\}.
\tag{2.4}
\]

Then

\[
 \Omega_H\subseteq\cdots\subseteq\Omega_{q_0}.
\tag{2.5}
\]

On the complete canonical PBBS deck, the correct depth-\(q\) histogram
covers every target in \(\binom{[K]}{m-q}\). If

\[
 M_q=|\Omega_q|,
\]

then

\[
 M_q\ge\binom K{m-q},
 \qquad
 \widetilde E_q^{\rm full}=0.
\tag{2.6}
\]

These are simultaneous statements about the same canonical PBBS deck,
but they use the decreasing masses \(M_q\). By contrast, (1.3) uses one
constant mass \(G\). The difference is not cosmetic: the missing
occurrences at depth \(q\) are precisely starts which have died and no
longer supply a target of the required rank.

## 3. A selected PBBS section and its mortality ledger

Let \(\mathcal X\) be a selected set of \(M\) PBBS starts, all correct at
depth \(q_0\), and suppose their entrance targets

\[
 L_{q_0}(X),\qquad X\in\mathcal X,
\]

are distinct. Put

\[
 b_d=|\{X\in\mathcal X:\eta_{q_0+d}(X)>0\}|,
\tag{3.1}
\]

and let

\[
 P_d=
 \{L_{q_0+d}(X):X\in\mathcal X,
                    \ \eta_{q_0+d}(X)=0\}.
\tag{3.2}
\]

The live mass at depth \(d\) is

\[
 G_d=M-b_d.
\tag{3.3}
\]

The PBBS floor-correct support loss is therefore

\[
 \widetilde E_d^{\rm PBBS}
 =\min\{M-b_d,N_d\}-|P_d|.
\tag{3.4}
\]

The actual PBBS hole count is

\[
 H_d^{\rm PBBS}
 =(N_d-M+b_d)_++\widetilde E_d^{\rm PBBS}.
\tag{3.5}
\]

If \(M=N_0-L\), then

\[
 H_d^{\rm PBBS}
 =\bigl(b_d+L-(N_0-N_d)\bigr)_+
   +\widetilde E_d^{\rm PBBS}.
\tag{3.6}
\]

Consequently full PBBS support before thinning proves neither a small
mortality staircase nor a small correlated support loss for one selected
section.

There is a clean mortality-free specialization. If

\[
 \mathcal X\subseteq\Omega_H,
\tag{3.7}
\]

then \(b_d=0\) for every \(d\), all depths have the common mass \(M\),
and

\[
 \mathfrak C^{\rm PBBS}(\mathcal X)
 =\sum_{d=0}^{J}
  \bigl(\min\{M,N_d\}-|P_d|\bigr).
\tag{3.8}
\]

Thus a safe section satisfying

\[
 M=N_0-O(N_0/\sqrt m),
 \qquad
 \mathfrak C^{\rm PBBS}(\mathcal X)=o(W^+)
\tag{3.9}
\]

would already solve the incidence half of the ordinary annular problem.
The fixed canonical PBBS support theorem does not imply (3.9). It proves
only that every target has some corrected occurrence, not the group Hall
inequalities needed to choose distinct entrance roots and one common
safe occurrence per root.

If all coordinate conjugates are allowed, inclusion-preserving Hall
surjections between consecutive rank layers give one safe nested flag per
entrance root with full support at every depth. Every such flag is
realized by a suitable conjugate of a terminal PBBS fan. Hence the full
conjugate library has an integral section with

\[
 b_d=0,
 \qquad
 \widetilde E_d^{\rm PBBS}=0
 \quad(0\le d\le J).
\tag{3.10}
\]

The conjugating permutation depends on the entrance root. Therefore
(3.10) is not a section of one canonical successor permutation and gives
no cyclic adjacency between histories chosen for different roots.

## 4. Exact coupling to an extracted ordinary family

Let \(\Pi\) be any extracted ordinary cyclic packet family with the same
total entrance mass \(M\), where \(K\mid M\). Its entrance roots are
assumed distinct, but
they need not retain the PBBS future targets. Let

\[
 O_d=\bigcup_{\pi\in\Pi}E_d(\pi)
\tag{4.1}
\]

be its ordinary support. Define

\[
 \mathfrak C^{\rm PBBS}_{\rm live}
 =\sum_{d=0}^{J}
  \bigl(\min\{M-b_d,N_d\}-|P_d|\bigr),
\tag{4.2}
\]

\[
 \mathfrak R_{\rm mort}
 =\sum_{d=0}^{J}
  \left[
    \min\{M,N_d\}-\min\{M-b_d,N_d\}
  \right],
\tag{4.3}
\]

and

\[
 \mathfrak B_{\rm ext}
 =\sum_{d=0}^{J}(|P_d|-|O_d|).
\tag{4.4}
\]

### Theorem 4.1 (PBBS-to-ordinary support coupling)

The extracted ordinary correlated loss obeys the exact identity

\[
 \boxed{
 \mathfrak C^{\rm ord}
 =\mathfrak C^{\rm PBBS}_{\rm live}
  +\mathfrak R_{\rm mort}
  +\mathfrak B_{\rm ext}.}
\tag{4.5}
\]

If the ordinary packets are exposed by any stopped ordering, then

\[
 \boxed{
 \sum_j\Delta_j^{\rm ord}
 =\mathfrak C^{\rm PBBS}_{\rm live}
  +\mathfrak R_{\rm mort}
  +\mathfrak B_{\rm ext}.}
\tag{4.6}
\]

For a random extraction law, defining
\(\mathscr P_j^{\rm ord}
=\mathbb E[\Delta_j^{\rm ord}\mid\mathcal F_j]\) gives

\[
 \mathbb E\mathfrak C^{\rm ord}
 =\mathbb E\sum_j\mathscr P_j^{\rm ord}.
\tag{4.6a}
\]

#### Proof

At depth \(d\), add and subtract the live PBBS capacity and support:

\[
 \begin{aligned}
 \min\{M,N_d\}-|O_d|
 ={}&\bigl(\min\{M-b_d,N_d\}-|P_d|\bigr)\\
 &+\bigl(\min\{M,N_d\}-\min\{M-b_d,N_d\}\bigr)\\
 &+(|P_d|-|O_d|).
 \end{aligned}
\tag{4.7}
\]

Sum over \(d\) to obtain (4.5). The ordinary stopped-profile identity
(1.7) says its left side equals
\(\sum_j\Delta_j^{\rm ord}\), proving (4.6). Conditional expectation
and the tower property give (4.6a). \(\square\)

The extraction term is signed. Indeed,

\[
 |P_d|-|O_d|
 =|P_d\setminus O_d|-|O_d\setminus P_d|.
\tag{4.8}
\]

The first term counts lost PBBS targets and the second counts genuinely
new ordinary targets. Thus bounding only destroyed PBBS windows is a
sufficient but not necessary route. The weakest exact extraction theorem
is the signed assertion that the right side of (4.5) is \(o(W^+)\).

If extraction changes at most \(Q_d\) individual depth-\(d\) target
incidences, then support cardinality is one-Lipschitz under each edit, so

\[
 \bigl||P_d|-|O_d|\bigr|\le Q_d.
\tag{4.9}
\]

Consequently

\[
 \sum_dQ_d=o(W^+)
\tag{4.10}
\]

is a simple sufficient inheritance theorem. It is not supplied by an
\(o(W^+)\) count of changed entrance edges, because one edge change has
a growing all-depth shadow.

## 5. Exact cyclic packet closure

We next isolate which Johnson cycles are literal ordinary cyclic decks.

### Theorem 5.1 (FIFO closure law)

Let \((A_i)_{i\in\mathbb Z_K}\) be a directed cycle of distinct
rank-\(R\) sets with

\[
 A_{i+1}=A_i-\{u_i\}+\{v_i\}.
\tag{5.1}
\]

There is a cyclic coordinate order \((z_i)_{i\in\mathbb Z_K}\) such
that

\[
 A_i=\{z_i,z_{i+1},\ldots,z_{i+R-1}\}
\tag{5.2}
\]

for every \(i\) if and only if

\[
 \boxed{
 (u_i)_{i\in\mathbb Z_K}\text{ is a permutation of }[K],
 \qquad
 v_i=u_{i+R}.}
\tag{5.3}
\]

#### Proof

For a literal cyclic order, shifting the window removes \(z_i\) and
inserts \(z_{i+R}\). Thus \(u_i=z_i\), the departures form a
permutation, and \(v_i=u_{i+R}\).

Conversely, assume (5.3) and put \(z_i=u_i\). Coordinate \(u_j\) is
inserted at transition \(j-R\) and removed at transition \(j\). Hence it
belongs exactly to the \(R\) states

\[
 A_{j-R+1},A_{j-R+2},\ldots,A_j.
\]

Equivalently, \(A_i=\{u_i,ldots,u_{i+R-1}\}\), proving (5.2).
\(\square\)

Along one PBBS component, the sliding entrance traces

\[
 T_i=L_{q_0}(g^iX)
\tag{5.4}
\]

do form Johnson transitions whenever the relevant deeper window is
correct. A terminal global-maximum fan even gives a local geodesic trace.
These facts constrain a finite path only. They do not prove that a chosen
\(K\)-block closes, that its departures exhaust \([K]\), or that each
arrival is the departure delayed by exactly \(R\) positions. Thus local
PBBS fan correctness does not imply (5.3).

The full coordinate-conjugate zero-excess section in (3.10) is even
farther from (5.3): its successor conjugate can change from one entrance
root to the next, so there is no common Johnson adjacency to test.

## 6. The all-depth cost of sewing seams

Suppose a PBBS trace component is cut at some successor arcs and the
resulting segments are sewn into proposed ordinary cycles. Retain the
old trace sequence inside every segment. A depth-\(d\) PBBS descendant
of phase \(i\) is

\[
 L_{q_0+d}(X_i)
 =\bigcap_{h=0}^{d}L_{q_0}(X_{i+h}).
\tag{6.1}
\]

Thus it depends on \(d\) consecutive successor arcs of the entrance
trace sequence.

### Lemma 6.1 (seam-shadow bound)

If \(t\) old successor arcs are deleted, then at depth \(d\) at most
\(dt\) old PBBS occurrences have trace windows crossing a deleted arc.
Consequently, for the retained PBBS support \(P_d\) and extracted
ordinary support \(O_d\),

\[
 |P_d\setminus O_d|\le dt,
\tag{6.2}
\]

provided every old window avoiding all deleted arcs is retained
literally. Hence

\[
 \boxed{
 \sum_{d=1}^{J}|P_d\setminus O_d|
 \le\frac{J(J+1)}2,t.}
\tag{6.3}
\]

#### Proof

On a cyclic sequence, a fixed successor arc lies in exactly \(d\)
windows of \(d+1\) consecutive entrance traces. Take a union bound over
the \(t\) deleted arcs. Every old occurrence whose window crosses no
deleted arc remains an identical occurrence after sewing; hence every
lost old support target must have all its old occurrences among the
crossing windows. In particular the number of lost support targets is at
most the number of crossing occurrences, proving (6.2). Sum over
\(d\). \(\square\)

The new seams also generate at most \(dt\) new depth-\(d\) occurrences.
They may replace lost targets or hit targets outside \(P_d\). Equation
(4.8), rather than (6.3), records their exact value. Therefore (6.3) is
an automatic upper bound, not a lower-bound obstruction.

Since

\[
 J^2=\Theta(m),
\]

condition

\[
 t=o(W^+/m)
\tag{6.4}
\]

would make the crude inherited loss in (6.3) little-oh. A
Catalan-scale number

\[
 t=\Theta(W^+/K)=\Theta(W^+/m)
\tag{6.5}
\]

gives only an \(O(W^+)\) bound. This is the quantitative reason a
first-shadow statement stable under \(o(W^+)\) edge edits does not
automatically extend to the whole Gaussian annulus.

There is also a component-count lower bound on how many PBBS edges a
literal length-\(K\) cycle factor may need to change. Let
\(B=W^+/K\), and let \(b_1\) be the number of PBBS components already of
length \(K\).

### Lemma 6.2 (component sewing lower bound)

Every exact length-\(K\) cycle factor \(F\) differs from the PBBS
2-factor \(P\) in at least

\[
 \boxed{|E(P)\setminus E(F)|\ge B-b_1.}
\tag{6.6}
\]

#### Proof

Delete the \(t=|E(P)\setminus E(F)|\) old PBBS edges. Every untouched
PBBS component remains a component of \(F\), so only the \(b_1\)
already-short components can be untouched. Cutting the other PBBS cycles
at a total of \(t\) deleted edges produces at most \(t\) additional
retained paths. Adding the new factor edges cannot increase component
count. Since \(F\) has exactly \(B\) components,

\[
 B\le b_1+t.
\]

This proves (6.6). \(\square\)

If \(b_1\) is not \(B-o(B)\), Lemma 6.2 forces Catalan-scale sewing.
No asymptotic bound on \(b_1\) is used here. Even when (6.6) is large, it
does not prove linear annular holes: the new seams may have favorable
signed support gain. It proves that sparse-edit inheritance cannot be the
general argument.

## 7. Two-sided phase coherence

The PBBS upper and lower towers satisfy the exact relation

\[
 U_q(X)=[K]\setminus L_{q-1}(fX).
\tag{7.1}
\]

Thus choosing a lower tower at phase \(X\) fixes the relevant upper tower
at the shifted phase \(fX\). A rootwise lower Hall section, including the
zero-excess conjugate section in (3.10), need not choose the matching
phase on the upper shore and need not use one common conjugate there.

For an ordinary cyclic coordinate order, complementation sends every
length-\((R-d)\) interval to a length-\((K-R+d)\) interval in the same
order. Hence a valid ordinary packet automatically has the required
two-sided coupling. This is another reason that lower support before
bundling cannot be promoted directly to the ordinary stopped profile.
The phase shift (7.1) and FIFO law (5.3) must be solved by the same
extracted cycles.

## 8. The exact sufficient PBBS-to-ordinary theorem

The preceding identities isolate a clean sufficient theorem.

> **PBBS--ordinary correlated bundling theorem.** Select a canonical
> PBBS entrance section \(\mathcal X\) of size
> \[
> M=N_0-O(N_0/\sqrt m)
> \]
> with distinct entrance targets. Extract from those roots a
> complement-coupled family of ordinary cyclic packets satisfying the
> FIFO law (5.3). Require
> \[
> \mathfrak C^{\rm PBBS}_{\rm live}
> +\mathfrak R_{\rm mort}
> +\mathfrak B_{\rm ext}=o(W^+).
> \tag{8.1}
> \]

By Theorem 4.1, (8.1) is exactly

\[
 \mathfrak C^{\rm ord}=o(W^+).
\tag{8.2}
\]

The common scalar entrance bill is

\[
 \sum_{d=0}^{J}(N_d-M)_+=o(W^+),
\tag{8.3}
\]

and cutting each extracted ordinary cycle once gives

\[
 p=O(W^+/K),
 \qquad
 2Hp=O(W^+/\sqrt m)=o(W^+).
\tag{8.4}
\]

Thus the ordinary annulus compiler closes deterministically.

There are two useful stronger versions of (8.1).

1. A mortality-free PBBS section with
   \(\mathfrak C^{\rm PBBS}=o(W^+)\), followed by an extraction with
   \(\mathfrak B_{\rm ext}=o(W^+)\).
2. An expanded incidence edit bound
   \(\sum_dQ_d=o(W^+)\), which implies the second condition by (4.9).

Neither is presently proved in one canonical PBBS factor. The complete
all-depth PBBS tower proves only the unthinned, variable-mass statement
(2.6). The conjugate library proves the incidence part but destroys the
common successor needed for FIFO bundling. The known component sewing
results work at Catalan edge scale, whose all-depth seam shadow is only
\(O(W^+)\), not \(o(W^+)\).

## 9. Exact remaining obstruction

After coupling to the ordinary stopped profile, the missing physical
statement can be written without reference to independent ranks:

> Find one canonical PBBS section and one collection of FIFO-valid
> length-\(K\) cycles for which the signed support balance
> \[
> \sum_{d=0}^{J}
> \left[
>   \min\{M,N_d\}-|O_d|
> \right]=o(W^+).
> \tag{9.1}
> \]
> Equivalently, prove (8.1), or prove that the ordinary stopped-profile
> drifts of the extracted packets sum to \(o(W^+)\).

This is the exact bundling obstruction. It has three inseparable parts:

1. one mortality-controlled common section inside a fixed PBBS factor;
2. FIFO and phase-shift closure into ordinary cycles;
3. signed compensation of the all-depth targets destroyed and created at
   the sewing seams.

PBBS's deterministic occurrence tower solves the local nested-history
problem and the uncut target histograms. It does not solve these three
global selection and bundling conditions. Conversely, the present
identities do not prove that every FIFO extraction has a linear defect;
such a no-go would require a positive lower bound on the signed term
\(\mathfrak B_{\rm ext}\), not merely on the number of seams.
