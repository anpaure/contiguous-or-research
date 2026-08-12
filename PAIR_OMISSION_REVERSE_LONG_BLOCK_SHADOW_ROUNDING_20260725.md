# Reverse-transport LONG-BLOCK shadow rounding: exact path cube, parity action, and the first-upper floor

Date: 2026-07-25

## 0. Outcome

This note audits the componentwise LONG-BLOCK interpolation suggested by
an adjacent swap of two first-avoided pair priorities.  It gives one
positive exact rounding theorem and one sharp obstruction.  All multidepth
statements assume \(1\le H\le m-2\), as in the intended Gaussian range.

Let the adjacent omitted pairs be \(A=P_j\) and \(B=P_{j+1}\), let
\(\tau\) exchange the two coordinates of \(A\) with the two coordinates
of \(B\), choose

\[
 F_B=\tau F_A,
\]

and traverse the transported rows in the opposite orientation.  Then:

1. every component of the central matching difference is exactly one
   physical interval of changed starts;
2. every legal component state is one threshold, namely an \(A\)-prefix
   followed by a \(B\)-suffix;
3. every choice of all component thresholds is an integral
   lower-saturating, middle-simple matching;
4. every such choice creates at most two new physical runs per component,
   so all corners retain predecessor probability \(1-o(1/H)\); and
5. the flag difference between two thresholds is supported only on the
   endpoint collars and has weighted squared norm at most
   \[
      8\sum_{q\le H}q w_q,
   \]
   independently of the length of the switched block.

For any two prescribed thresholds on every component, let \(z_I\) be the
resulting flag innovation, let \(B_w\) be the invariant coordinatewise
pair-sum floor, let \(O_w\) be the odd-pair-sum parity floor, and put

\[
 D_w=\min_{\varepsilon_I\in\{\pm1\}}
       \left\|\sum_I\varepsilon_Iz_I\right\|_w^2.
\]

Then one integral LONG-BLOCK corner has balanced flag excess at most

\[
 \boxed{\frac{B_w}{2}+\frac{D_w-O_w}{8}.}
\]

This is the sharp correlated shadow-twin theorem for the reverse path
cube.  It loses neither central integrality nor predecessor correlation.
Because every \(z_I\) is coordinatewise \(0,\pm1\), a concrete sufficient
condition is

\[
 B_w=o(W),\qquad
 \Gamma_w:=\sum_\alpha w_\alpha
       \binom{\#\{I:z_I(\alpha)\ne0\}}2=o(W).
\]

Indeed \(D_w-O_w\le2\Gamma_w\).  Thus the remaining positive input is a
paired-floor plus collar-overlap theorem, not a tokenwise rounding theorem.

There is, however, an immutable first-upper obstruction.  Across the
entire reverse path cube, at most

\[
 4R_m=O(W/m),\qquad
 R_m=\frac1{2m-1}\binom{2m-1}{m-1},
\]

rank-\((m+1)\) occurrences can differ from the original matching.  If
\(C_1=\sum_T(\mu_1^+(T)-1)_+\) is its first-upper raw duplicate excess,
then the pair-sum floor of **any two** reverse-path corners obeys

\[
 \boxed{B_1^+\ge C_1-4R_m=C_1-O(W/m).}
\]

Consequently reverse transport cannot repair a linear first-upper defect.
It is a genuine positive long-block interpolation only after the first
upper shadow has already been made \(o(W)\).  At deeper ranks its exact
remaining gate is \(B_w=o(W)\) and \(D_w-O_w=o(W)\); neither follows from
matching-polytope integrality or from the orbit convex decomposition.

## 1. The two adjacent-priority matchings

Put

\[
 n=2m+1,\qquad W=\binom nm,
 \qquad L=2m-1,
 \qquad R_m=\frac1L\binom{2m-1}{m-1}.
\]

Throughout, \(1\le H\le m-2\).  This is automatic in the intended
Gaussian/product-tail range.  The upper collar estimate is not asserted at
\(q=m-1\), where the local upper window becomes the full local universe.

Partition \(2m\) coordinates into ordered disjoint pairs
\(P_1,\ldots,P_m\).  Fix adjacent priorities

\[
 A=P_j,\qquad B=P_{j+1}.
\]

The lower targets whose assigned carrier changes when these priorities
are interchanged are exactly

\[
 \mathcal D_j=
 \left\{S\in\binom{[n]}{m-1}:
 S\cap P_h\ne\varnothing\ (h<j),\quad
 S\cap A=S\cap B=\varnothing\right\}.
\tag{1.1}
\]

Choose a bijection from the two coordinates of \(A\) to the two
coordinates of \(B\), and let \(\tau\) be the product of the two resulting
transpositions.  Thus \(\tau A=B\), \(\tau B=A\), and \(\tau\) fixes
\([n]\setminus(A\cup B)\) pointwise.  Choose one exact local factor
\(F_A\) on \(Q_A=[n]\setminus A\), set \(F_B=\tau F_A\), and reverse the
orientation of every transported row of \(F_B\).

For a row

\[
 \pi=(x_0,x_1,\ldots,x_{L-1})
\]

of \(F_A\), use cyclic indices and write

\[
 S_i=I_\pi(i,m-1),\qquad X_i=I_\pi(i,m).
\tag{1.2}
\]

Over a changed lower target \(S_i\), the old and reverse-transport tokens
are

\[
 e_A(i)=(S_i,X_{i-1}),
 \qquad
 e_B(i)=(S_i,\tau X_i).
\tag{1.3}
\]

All lower targets outside \(\mathcal D_j\) retain their original token.

### Lemma 1.1 (changed-start interval count)

The set of starts \(i\) for which \(S_i\in\mathcal D_j\) has at most
\(2j\) circular intervals in one row of \(F_A\).  Hence the total number
\(s_j\) of maximal changed intervals satisfies

\[
 \boxed{s_j\le2jR_m=O(jW/m).}
\tag{1.4}
\]

#### Proof

The row already avoids \(A\).  For one fixed earlier pair, the starts at
which a cyclic length-\((m-1)\) window avoids both of its coordinates form
the intersection of two circular arcs and have at most two components.
The same is true for the pair \(B\).  The complement of the union of the
\(j\) bad-start sets therefore has at most \(2j\) circular components.
There are \(R_m\) rows in \(F_A\). \(\square\)

## 2. Exact central path decomposition

### Theorem 2.1 (reverse components are physical interval paths)

Let

\[
 I=[a,b]=\{a,a+1,\ldots,b\}
\]

be a maximal changed interval in one row of \(F_A\).  In the symmetric
difference of the two central matchings, its edges form the alternating
path

\[
 X_{a-1}-S_a-X_a-S_{a+1}-\cdots-X_{b-1}-S_b-\tau X_b.
\tag{2.1}
\]

Different maximal intervals give different components.  In particular
there are no alternating cycles.  Every lower-saturating, middle-simple
selection supported on this path has a unique threshold \(r\in
\{a-1,a,\ldots,b\}\):

\[
 \boxed{
 \{e_A(i):a\le i\le r\}
 \cup
 \{e_B(i):r<i\le b\}.}
\tag{2.2}
\]

Conversely, independent threshold choices on all the paths, together with
the unchanged tokens, always form an integral lower-saturating,
middle-simple matching.

#### Proof

If both \(S_i\) and \(S_{i+1}\) lie in \(\mathcal D_j\), then \(S_i\)
and \(S_{i+1}\) avoid \(A\cup B\).  Since

\[
 X_i=S_i\cup\{x_{i+m-1}\}
     =S_{i+1}\cup\{x_i\},
\]

the entering and departing coordinates also lie outside \(A\cup B\).
Thus \(\tau X_i=X_i\), so \(e_B(i)\) and \(e_A(i+1)\) meet at \(X_i\).

Conversely, suppose a new changed edge and an old changed edge meet:

\[
 \tau X_i=X_{k-1}.
\]

The left side avoids \(B\), while the right side avoids \(A\).  Their
common value therefore avoids both pairs and is fixed by \(\tau\).  Hence
\(X_i=X_{k-1}\).  The length-\(m\) windows of an exact local factor occur
exactly once, so the two windows lie in the same row and \(k=i+1\).
This proves (2.1) and excludes links between different maximal intervals.

A middle vertex incident with an unchanged common token cannot be incident
with a changed token: either endpoint matching would then use that middle
vertex twice.  Hence the displayed path components are also disjoint from
all unchanged tokens.

A full cyclic changed interval is impossible because the row contains the
two coordinates of \(B\), whereas every changed lower window avoids them.
Thus every component is an open path.

On the path, write \(u_i=1\) when the old edge \(e_A(i)\) is chosen and
\(u_i=0\) when the new edge \(e_B(i)\) is chosen.  Exact lower saturation
forces one of the two at every \(S_i\).  Middle simplicity at \(X_i\)
forbids \((u_i,u_{i+1})=(0,1)\).  Therefore

\[
 u_a\ge u_{a+1}\ge\cdots\ge u_b,
\]

which is exactly (2.2).  Direct inspection proves the converse on one
path.  Distinct components are vertex-disjoint, so all thresholds may be
chosen independently. \(\square\)

This proves every integrality assertion directly; no total-unimodularity
claim is being used.

Every corner uses exactly \(|V_-|\) distinct middle owners, but the missed
middle set can depend on the thresholds.  Its size is always

\[
 W-|V_-|=\frac{2W}{m+2}=O(W/m).
\]

After the final corner is chosen, those missing middle targets may be
added as singleton owners at \(o(W)\) cost.  Thus the varying middle leave
does not enter the multidepth flag action below.  If one elects to include
the middle incidence in that action, changing a path threshold contributes
only the two path endpoints, adding at most \(2s_j=O(jW/m)\).

## 3. Run count and predecessor correlation

### Proposition 3.1 (uniform two-boundary toll)

Let \(M_A\) be the all-old first-avoided matching, and let \(M_{\mathbf r}\)
be any threshold corner from Theorem 2.1.  Then

\[
 \boxed{
 J(M_{\mathbf r})\le J(M_A)+2s_j.}
\tag{3.1}
\]

Consequently, if

\[
 J(M_A)=O(W\log^2m/m),
 \qquad H=o(m/\log^2m),
 \qquad jH=o(m),
\tag{3.2}
\]

then every threshold corner satisfies

\[
 J(M_{\mathbf r})=o(W/H).
\tag{3.3}
\]

#### Proof

On one path, changing the cut from the all-old endpoint removes one suffix
interval from the old physical row and inserts the corresponding suffix
interval in the oppositely oriented transported row.  Deleting one
interval can increase the number of selected runs by at most one, and
inserting one interval can increase it by at most one.  Summing over the
paths proves (3.1).  Equations (1.4) and (3.2) give (3.3). \(\square\)

For a deterministic matching \(M\), choose a uniformly random selected
token and ask whether its cyclic predecessor position in the same source
row is also selected.  Apart from the harmless convention for a fully
selected cyclic row, the number of failures is the number of cyclic run
starts and is at most \(J(M)\).  Since every corner has
\(|V_-|=\binom n{m-1}=\Theta(W)\) selected tokens, (3.3) gives

\[
 \boxed{
 \Pr(\operatorname{pred}(e)\in M\mid e\in M)
 \ge1-\frac{J(M)}{|V_-|}
 =1-o(1/H).}
\tag{3.4}
\]

This holds corner by corner, hence under every random law on the path cube.

## 4. Exact multidepth collar vectors

For \(1\le q\le H\), the old token over \(S_i\) carries

\[
 L^A_q(i)=I_\pi(i+q-1,m-q),
 \qquad
 U^A_q(i)=I_\pi(i-1,m+q).
\tag{4.1}
\]

Opposite orientation in the transported row gives

\[
 L^B_q(i)=I_\pi(i,m-q),
 \qquad
 U^B_q(i)=\tau I_\pi(i-q,m+q).
\tag{4.2}
\]

The missing \(\tau\) in the first formula is intentional:
\(I_\pi(i,m-q)\subseteq S_i\), and every changed \(S_i\) avoids
\(A\cup B\), so this lower flag is fixed by \(\tau\).

For a consecutive interval \(K\) inside one path, define

\[
 E_{r}(K)=\sum_{i\in K}{\bf1}_{I_\pi(i,r)}.
\tag{4.3}
\]

Switching precisely \(K\) from old to new tokens has flag innovation

\[
 \boxed{
 \begin{aligned}
 z^-_{K,q}&=E_{m-q}(K)-E_{m-q}(K+q-1),\\
 z^+_{K,q}&=\tau E_{m+q}(K-q)-E_{m+q}(K-1).
 \end{aligned}}
\tag{4.4}
\]

### Lemma 4.1 (length-independent collar action)

For every consecutive \(K\) and \(1\le q\le m-2\),

\[
 \boxed{
 \|z^-_{K,q}\|_2^2\le2(q-1),
 \qquad
 \|z^+_{K,q}\|_2^2\le6q+2.}
\tag{4.5}
\]

In particular, for nonnegative class weights \(w_q\),

\[
 \boxed{
 \|z_K\|_w^2
 :=\sum_{q\le H}w_q
   \bigl(\|z^-_{K,q}\|_2^2+\|z^+_{K,q}\|_2^2\bigr)
 \le8\sum_{q\le H}q w_q.}
\tag{4.6}
\]

Moreover every coordinate of \(z_K\) lies in \(\{-1,0,1\}\).

#### Proof

At every proper rank, distinct cyclic starts in one row give distinct
windows.  The two start intervals in the lower line of (4.4) are translates
by \(q-1\), so their symmetric difference has size at most \(2(q-1)\).

For the upper line, insert \(\tau E_{m+q}(K-1)\).  The translate part has
\(\ell_1\)-norm at most \(2(q-1)\).  For \(i\in K\), the old upper window

\[
 I_\pi(i-1,m+q)
\]

contains the changed lower window \(S_i\), which avoids \(A\cup B\), and
has only \(q+1\) additional collar coordinates.  Each of the two
coordinates of \(B\) can occur in this collar for at most \(q+1\) starts
in the whole cyclic row.  Thus at most \(2(q+1)\) relevant upper windows
are moved by \(\tau\), each contributing two points to the symmetric
difference.  The total \(\ell_1\)-norm is at most

\[
 2(q-1)+4(q+1)=6q+2.
\]

Within either state, the fixed-rank targets on one path are distinct.
After common targets are cancelled, every innovation coordinate is
therefore \(0,1\), or \(-1\).  Its squared \(\ell_2\)-norm equals its
support size and is at most the displayed \(\ell_1\) bounds.  Summing the
two signs gives (4.6). \(\square\)

If two thresholds \(r_I^0,r_I^1\) are prescribed on a path, their
difference is exactly one consecutive interval \(K_I\), so Lemma 4.1
applies to the corresponding two-state innovation \(z_I\).

## 5. Parity-sharp correlated rounding on the path cube

Let \(\alpha\) index all signed flag classes under consideration.  Write
\(\mathcal U_\alpha\) for the target set, \(N_\alpha=|\mathcal U_\alpha|\),
and let the fixed total class load be

\[
 T_\alpha=c_\alpha N_\alpha+\rho_\alpha,
 \qquad 0\le\rho_\alpha<N_\alpha.
\tag{5.1}
\]

For an integer \(x\ge0\), put

\[
 e_c(x)=\frac{(x-c)(x-c-1)}2,
\tag{5.2}
\]

and define the weighted balanced excess

\[
 \Delta_w(\mu)=
 \sum_\alpha w_\alpha
 \sum_{T\in\mathcal U_\alpha}e_{c_\alpha}(\mu_\alpha(T)).
\tag{5.3}
\]

Choose two legal thresholds on every reverse path.  Let
\(a_I^0,a_I^1\) be their flag incidence vectors, put

\[
 z_I=a_I^1-a_I^0,
\]

and let \(a_{\rm fr}\) contain all unchanged contributions.  For a sign
vector \(\varepsilon\in\{\pm1\}^{s_j}\), the corresponding integral
corner has load

\[
 \mu^\varepsilon
 =\frac12\left(t+\sum_I\varepsilon_Iz_I\right),
 \qquad
 t=2a_{\rm fr}+\sum_I(a_I^0+a_I^1).
\tag{5.4}
\]

Its complementary corner is \(\mu^{-\varepsilon}\), and their pair sum
\(t\) is independent of \(\varepsilon\).

For integers \(c,t\ge0\), define

\[
 b_c(t)=
 \min_{u+v=t}\{e_c(u)+e_c(v)\}
 =\left\lfloor\frac{(t-2c-1)^2}{4}\right\rfloor.
\tag{5.5}
\]

Put

\[
 B_w=\sum_{\alpha,T}w_\alpha
       b_{c_\alpha}(t_\alpha(T)),
 \qquad
 O_w=\sum_{\alpha,T}w_\alpha
       {\bf1}_{\{t_\alpha(T)\ \mathrm{odd}\}},
\tag{5.6}
\]

and

\[
 D_w=\min_{\varepsilon\in\{\pm1\}^{s_j}}
 \left\|\sum_I\varepsilon_Iz_I\right\|_w^2.
\tag{5.7}
\]

### Theorem 5.1 (exact LONG-BLOCK shadow-twin rounding)

Some integral reverse-path corner satisfies

\[
 \boxed{
 \Delta_w(\mu)
 \le\frac{B_w}{2}+\frac{D_w-O_w}{8}.}
\tag{5.8}
\]

Every corner in (5.8) is an exact lower-saturating, middle-simple matching,
obeys (3.1), and hence has predecessor probability (3.4).  Also

\[
 D_w\ge O_w
\tag{5.9}
\]

and

\[
 \boxed{
 D_w\le A_w:=\sum_I\|z_I\|_w^2
 \le8s_j\sum_{q\le H}q w_q.}
\tag{5.10}
\]

#### Proof

For integers \(d\equiv t\pmod2\), direct expansion gives

\[
 e_c\left(\frac{t+d}{2}\right)
 +e_c\left(\frac{t-d}{2}\right)
 =b_c(t)+\frac{d^2-{\bf1}_{\{t\ \mathrm{odd}\}}}{4}.
\tag{5.11}
\]

Apply (5.11) coordinatewise to the complementary corners in (5.4).  With
\(d^\varepsilon=\sum_I\varepsilon_Iz_I\),

\[
 \frac{\Delta_w(\mu^\varepsilon)
       +\Delta_w(\mu^{-\varepsilon})}{2}
 =\frac{B_w}{2}
  +\frac{\|d^\varepsilon\|_w^2-O_w}{8}.
\tag{5.12}
\]

Choose a minimizing sign vector in (5.7), then choose the better of its
two integral corners.  This proves (5.8).  Parity gives
\(|d^\varepsilon_\alpha(T)|\ge1\) whenever \(t_\alpha(T)\) is odd, proving
(5.9).  Finally, independent fair signs have

\[
 \mathbb E\left\|\sum_I\varepsilon_Iz_I\right\|_w^2
 =\sum_I\|z_I\|_w^2,
\]

so the minimum is at most this expectation.  Lemma 4.1 proves the final
bound.  Central integrality and the run statement were proved in Theorem
2.1 and Proposition 3.1 for every corner, not merely in expectation.
\(\square\)

The raw action in (5.10) is critical rather than small.  Unweighted,

\[
 A_w=O(jWH^2/m).
\tag{5.13}
\]

For \(H=\sqrt m\,\omega\), this is \(O(jW\omega^2)\), so discarding the
parity term cannot close the argument.

### Corollary 5.2 (collar-overlap sufficient condition)

For a target-depth coordinate \(\gamma=(\alpha,T)\), put

\[
 r_\gamma=\#\{I:z_I(\gamma)\ne0\},
 \qquad
 \Gamma_w=\sum_\gamma w_\gamma\binom{r_\gamma}{2}.
\tag{5.14}
\]

Then

\[
 \boxed{
 D_w-O_w\le A_w-O_w
 =\sum_\gamma w_\gamma
    \bigl(r_\gamma-(r_\gamma\bmod2)\bigr)
 \le2\Gamma_w.}
\tag{5.15}
\]

Consequently

\[
 \boxed{B_w=o(W),\quad \Gamma_w=o(W)}
\tag{5.16}
\]

imply an integral exact central corner with balanced flag excess \(o(W)\)
and predecessor probability \(1-o(1/H)\).

#### Proof

Lemma 4.1 gives \(z_I(\gamma)\in\{-1,0,1\}\), so the contribution of
\(\gamma\) to \(A_w\) is \(w_\gamma r_\gamma\).  Modulo two, signs do not
matter and

\[
 t(\gamma)\equiv\sum_Iz_I(\gamma)\equiv r_\gamma\pmod2.
\]

This proves the equality in (5.15).  For every integer \(r\ge0\),

\[
 r-(r\bmod2)=2\lfloor r/2\rfloor\le2\binom r2.
\]

Use \(D_w\le A_w\), sum, and apply Theorem 5.1. \(\square\)

Thus the relevant action is the parity-restitution defect
\(D_w-O_w\), not the raw collar mass \(A_w\).  The collar-overlap
functional in (5.14) is a concrete sufficient structural gate.

### Corollary 5.3 (exact contraction identity)

Let \(\mu^0,\mu^1\) be the two coherent global corners obtained by taking
state zero on every path and state one on every path.  Then

\[
 \frac{\Delta_w(\mu^0)+\Delta_w(\mu^1)}2
 =\frac{B_w}{2}
  +\frac{\|\sum_Iz_I\|_w^2-O_w}{8}.
\tag{5.17}
\]

The best antipodal hybrid pair improves their average by exactly

\[
 \boxed{
 \frac{\|\sum_Iz_I\|_w^2-D_w}{8}.}
\tag{5.18}
\]

In particular, reverse transport gives a strict energy contraction exactly
when its component vectors admit a signing with strictly smaller squared
norm than their coherent sum.  The collar theorem alone gives no sign for
this quantity.

## 6. The first-upper pair-floor obstruction

At the first upper flag, (4.1)--(4.2) reduce to

\[
 U^A_1(i)=I_\pi(i-1,m+1),
 \qquad
 U^B_1(i)=\tau I_\pi(i-1,m+1).
\tag{6.1}
\]

The changed lower window \(S_i=I_\pi(i,m-1)\) is contained in this upper
window and avoids \(A\cup B\).  The difference

\[
 I_\pi(i-1,m+1)\setminus S_i
 =\{x_{i-1},x_{i+m-1}\}
\tag{6.2}
\]

has only two collar positions.  For one fixed coordinate of \(B\), there
are at most two starts in a row for which it occupies one of these
positions.  Hence:

### Lemma 6.1 (only \(4R_m\) movable first-upper occurrences)

Across all rows and all reverse-path thresholds, the set of token
occurrences whose first-upper target can differ from its all-old target has
size at most

\[
 \boxed{E_1\le4R_m=O(W/m).}
\tag{6.3}
\]

In particular, the first-upper load vector of any reverse-path corner is
obtained from that of \(M_A\) by replacing at most \(E_1\) occurrences.
\(\square\)

The rank-\((m+1)\) target class has size \(W\), while every central
matching has

\[
 T=|V_-|=\binom n{m-1}=\frac{m}{m+2}W<W
\]

first-upper occurrences.  Its balanced floor is therefore \(c=0\), and
the pair-sum floor function is

\[
 \beta(t)=b_0(t)=\left\lfloor\frac{(t-1)^2}{4}\right\rfloor.
\tag{6.4}
\]

### Theorem 6.2 (first-upper floor survives every reverse hybrid pair)

Let \(\mu\) be the first-upper load vector of \(M_A\), and put

\[
 C_1(M_A)=\sum_T(\mu(T)-1)_+.
\tag{6.5}
\]

For any two integral corners \(M^0,M^1\) of the full reverse path cube,
let

\[
 B_1^+(M^0,M^1)
 =\sum_T\beta\bigl(\mu^0(T)+\mu^1(T)\bigr).
\tag{6.6}
\]

Then

\[
 \boxed{
 B_1^+(M^0,M^1)
 \ge C_1(M_A)-E_1
 \ge C_1(M_A)-4R_m.}
\tag{6.7}
\]

#### Proof

For \(h=0,1\), let \(d_h(T)\) count the all-old occurrences at \(T\)
which are removed when forming \(M^h\).  Additions can only increase the
resulting coordinate load, so

\[
 \mu^0(T)+\mu^1(T)
 \ge2\mu(T)-d_0(T)-d_1(T).
\tag{6.8}
\]

Lemma 6.1 gives

\[
 \sum_Td_h(T)\le E_1.
\tag{6.9}
\]

The function \(\beta\) is nondecreasing on the nonnegative integers and
obeys

\[
 \beta(u)\ge\frac u2-1\qquad(u\ge0).
\tag{6.10}
\]

For a coordinate with \(\mu(T)\ge1\), (6.8)--(6.10) give

\[
 \beta(\mu^0(T)+\mu^1(T))
 \ge \mu(T)-1-\frac{d_0(T)+d_1(T)}2.
\]

For \(\mu(T)=0\), the desired lower bound is zero.  Sum over \(T\) and
use (6.9). \(\square\)

### Corollary 6.3 (necessary prepared-first-shadow condition)

If

\[
 C_1(M_A)=\Omega(W),
\]

then every two-state correlated rounding inside the reverse path cube has

\[
 B_1^+=\Omega(W).
\]

Thus the sufficient condition \(B_w=o(W)\) in Theorem 5.1 is impossible.
In particular, reverse transport cannot repair the linear first-upper
collision of an unprepared first-avoided carrier.  A genuinely useful
application must begin with

\[
 \boxed{C_1(M_A)=o(W).}
\tag{6.11}
\]

This is stronger than saying that orbit averaging makes the mean uniform:
the orbit can average the load vector without changing any member's
duplicate energy, while (6.7) is an integral two-cover obstruction.

## 7. Exact conditional gate

For the reverse-transport adjacent-priority class, the remaining theorem
needed for a positive constant-one application is now precise.

> **Reverse-path pair-floor/discrepancy gate.**  First construct a
> first-avoided matching with \(C_1=o(W)\).  Then choose adjacent priorities,
> the reverse transport, and two thresholds per physical exchange path so
> that
> \[
> B_w=o(W),\qquad D_w-O_w=o(W).
> \tag{7.1}
> \]
> Equivalently, the stronger explicit conditions
> \[
> B_w=o(W),\qquad\Gamma_w=o(W)
> \tag{7.2}
> \]
> suffice.

Under (7.1), Theorem 5.1 gives an integral exact central matching with
\(o(W)\) balanced multidepth flag excess.  Proposition 3.1 gives
\(J=o(W/H)\) in the product-tail range, and hence predecessor conditional
probability \(1-o(1/H)\).  Every flag remains attached to its literal
physical token; no vertex-independent residual is introduced.

What is proved here is the entire component, integrality, run, parity, and
collar-action theorem.  What is not proved is (7.1).  The balanced
fractional point and its convex decomposition into integral low-run
matchings do not imply it: they control means, whereas \(B_w\) is an
invariant integer pair floor and \(D_w-O_w\) is a common-sign multidepth
discrepancy.  The first-upper lower bound (6.7) shows that at least one part
of this gap is genuinely necessary.
