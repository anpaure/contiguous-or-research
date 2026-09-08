# Growing `D_s`-port seeds: sparse-edit component rounding survives

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Verdict

The bounded-seed and component-local-minimum obstructions do not close every
exact-factor heat argument.  One genuinely different lane survives when the
two endpoints are themselves growing, anchored `D_s`-port factors and are
not required to be coordinate relabelings of one another.

Let

\[
        n=2s+1,\qquad B=\operatorname {Cat}_s,\qquad W=nB,
        \qquad H<s.
\]

For two anchored exact `D_s`-port factors \(F^0,F^1\), let \({\cal K}\)
be the components of their **full** state-and-colour ownership overlay.
The port state pairs the row rooted at \(P\) on the two shores, so each
component has one common root block \(R_K\subseteq D_s\).  Put

\[
 b_K=|R_K|,
 \qquad d(P)=d_\infty(\omega_0(P),\omega_1(P)),
 \qquad D_K=\sum_{P\in R_K}d(P),                       \tag{0.1}
\]

where \(d_\infty\) is rooted cyclic adjacent-transposition distance, with
the distinguished coordinate \(\infty\) fixed, and \(\omega_e(P)\) is the
rooted coordinate order of the row of \(F^e\) at \(P\).  The exact
size-weighted edit moment is

\[
 \boxed{\displaystyle
       \Xi(F^0,F^1)=\frac1B\sum_{K\in{\cal K}}b_KD_K.} \tag{0.2}
\]

If \(V_H\) is the complete component variance over the lower depths
\(1\le q\le H\), with the usual weights \(1/c_q\), then

\[
 \boxed{\displaystyle
 V_H(F^0,F^1)
 \le 4B\,\Xi(F^0,F^1)
             \sum_{q=1}^H\frac1{c_q}.}                \tag{0.3}
\]

For a direct root-scale factor this counts every cyclic start, including
the starts meeting the anchor.  It remains true after start-dependent
carrier/collar maps provided (i) the physical map at a given root and start
is the same on the two shores and (ii) the resulting proper ambient cyclic
intervals are distinct within each row.  Condition (ii) is automatic for
literal cyclic intervals in one ambient coordinate order.  More generally,
if one target can occur at most \(\rho\) times in one pushed-forward row,
the right side of (0.3) is multiplied by \(\rho\).  Thus no literal
crossing-collar term has been omitted.

For a lift to a strictly larger ambient row, the distance in the theorem
must be measured on the resulting full ambient coordinate words, unless
the lift is proved to send each local adjacent edit to one ambient adjacent
edit.  No such preservation is asserted for a moving-slot operadic lift;
that is exactly where the existing common-port obstruction applies.

Since \(c_q\ge1\), at \(H=\lceil A\sqrt s\rceil\),

\[
 \frac{V_H}{W}
 \le \frac{4H\Xi}{2s+1}.
                                                               \tag{0.4}
\]

Consequently

\[
                         \Xi=o_A(\sqrt s)              \tag{0.5}
\]

is sufficient for an \(o(W)\) integral rounding loss.  A convenient but
strictly stronger condition is

\[
 L\bar d=o_A(\sqrt s),\qquad
 L=\max_Kb_K,\quad
 \bar d=B^{-1}\sum_{P\in D_s}d(P),                    \tag{0.6}
\]

because \(\Xi\le L\bar d\).

The variance theorem is not, by itself, a contraction theorem.  The exact
remaining input is a **state-adaptive growing counterseed**: its midpoint
with the current factor must contract the full floor-corrected load, while
its full ownership overlay satisfies (0.5).  The terminal and iterative
forms are proved in Section 5.

This cleanly separates what survives from what does not:

* the old common-port obstruction rules out obtaining the required pair by
  suspending a bounded seed on almost all Catalan roots;
* the old component-expansion obstruction rules out deducing descent from
  the linear term of each component separately;
* neither obstruction applies to the aggregate variance estimate (0.3)
  for two directly constructed growing factors;
* growing size alone supplies neither midpoint counterbias nor small
  \(\Xi\).  A connected full overlay, for example, has no new integral
  child at all.

No coefficient-one conclusion is claimed here.  The precise constructive
lemma which would give it through this lane is stated in Section 7.

## 1. Anchored rows and their full lower profiles

Let \(J\) be a set of \(2s\) coordinates and
\(\infty\notin J\).  Fix the inherited Dyck port family

\[
                         D_s\subseteq\binom Js .        \tag{1.1}
\]

An anchored exact `D_s`-port factor is a partition of the middle-levels
inclusion graph into paths

\[
 P=X_0\subset Y_0\supset X_1\subset\cdots
   \subset Y_{s-1}\supset X_s=J\setminus P,
                    \qquad P\in D_s.                  \tag{1.2}
\]

Write its deletion and insertion orders as

\[
 (a_1(P),\ldots,a_s(P)),\qquad
 (b_1(P),\ldots,b_s(P)),                              \tag{1.3}
\]

so that

\[
 X_t=(P\setminus\{a_1,\ldots,a_t\})
              \cup\{b_1,\ldots,b_t\}.                \tag{1.4}
\]

The rooted cyclic coordinate word is

\[
 \omega_F(P)=
 (a_1(P),\ldots,a_s(P),b_1(P),\ldots,b_s(P),\infty).
                                                               \tag{1.5}
\]

The final occurrence of \(\infty\) is the fixed root anchor.  For
\(1\le r<n\), let

\[
 h_{F,P,r}=\sum_{i\in\mathbb Z/n\mathbb Z}
       e_{I_r(\omega_F(P),i)},                         \tag{1.6}
\]

where \(I_r(\omega,i)\) is the set of the \(r\) consecutive coordinates
starting at cyclic position \(i\).  Distinct starts give distinct proper
cyclic intervals: a nonempty proper directed arc is determined by its two
boundary edges and hence by its start.  Thus \(h_{F,P,r}\) is a zero-one
vector.

At lower depth \(q\), put \(r=s-q\) and

\[
 \mu_q^F=\sum_{P\in D_s}h_{F,P,s-q}.                  \tag{1.7}
\]

This is the complete lower cyclic-interval histogram: it contains all
\(n\) starts in every row, including the starts meeting the anchor.

For later collar use, one may replace each summand in (1.6) by

\[
 e_{\Gamma_{P,q,i}(I_r(\omega_F(P),i))},              \tag{1.8}
\]

where \(\Gamma_{P,q,i}\) is a deterministic map into a target universe
which is fixed between the two factors.  In particular,

\[
                  \Gamma(S)=C_{P,q,i}\mathbin{\dot\cup}\iota(S)       \tag{1.9}
\]

allows a start-dependent exterior collar.  The perturbation bound below
uses only that an unchanged local interval at a fixed start has an
unchanged image.  The component \(\ell^\infty\)-bound additionally uses
the physical fact that the resulting proper cyclic intervals within one
row are distinct.  If a more general push-forward merges at most \(\rho\)
starts of one row into one target, the final variance bound has the factor
\(\rho\).

This push-forward statement concerns the displayed \(n\) root-scale
occurrences.  An ambient lift which creates additional starts must first
identify them with a common side-independent occurrence map, or else apply
Theorem 4.1 directly to the two full ambient words.

## 2. Full ownership components retain common roots

Overlay two anchored exact factors \(F^0,F^1\).  Make one bipartite
vertex for each row on each shore.  Every middle state \(X\) and every
adjacent-union colour \(Y\) joins its unique owner on shore zero to its
unique owner on shore one.  Call this the full ownership overlay.

### Lemma 2.1 (common-root component law)

Every full ownership component \(K\) has the same root set \(R_K\) on
its two shores.  Choosing either complete shore independently in every
component produces another integral exact anchored `D_s`-port factor.

#### Proof

For every \(P\in D_s\), the port state \(X_0=P\) is owned by the row
rooted at \(P\) in both factors.  Its ownership edge therefore joins the
two vertices with the same root \(P\).  Hence a component contains the
shore-zero row at \(P\) if and only if it contains the shore-one row at
\(P\).  This proves the common-root assertion.

Every state or colour is an overlay edge lying wholly in one component.
After choosing one complete shore of that component, the chosen rows own
that token exactly once.  Doing this in every component therefore
partitions both the middle states and the adjacent-union colours.  The
chosen row at root \(P\) is a row rooted at \(P\) on either shore, so its
two ports remain \(P,J\setminus P\).  Thus the result is an integral
exact anchored factor.  Explicitly, the \(X\)-partition owns every
middle state once, while complementation of each selected \(Y\), followed
by adjoining \(\infty\), owns every remaining odd-graph vertex once.
Thus upper-side exactness is included, rather than inferred from the
middle ledger alone.  \(\square\)

The use of the **full** overlay is essential.  Components of an
\(X\)-state suboverlay may be merged by colour-owner edges and cannot be
substituted for the components in Lemma 2.1.

## 3. One rooted adjacent swap changes only two starts

Let \(d_\infty(\omega,\omega')\) be the least number of adjacent
transpositions of the first \(2s\) positions which transform one word
of the form (1.5) into the other; the anchor \(\infty\) remains in the
last position throughout.  The intermediate words are only a metric
device and are not asserted to be rows of exact factors.

### Lemma 3.1 (two-start perturbation)

For every \(1\le r<n\),

\[
 \boxed{\displaystyle
 \|h_{\omega,r}-h_{\omega',r}\|_1
       \le4d_\infty(\omega,\omega').}                 \tag{3.1}
\]

The same \(\ell^1\)-bound holds for the start-resolved push-forward (1.8).

#### Proof

It is enough to consider one adjacent transposition, exchanging the
coordinates \(x,y\) in consecutive cyclic positions.  An \(r\)-interval
which contains both exchanged positions, or neither, has the same set
before and after the exchange.  Exactly one cyclic \(r\)-interval ends at
the first position and contains \(x\) but not \(y\), and exactly one
starts at the second position and contains \(y\) but not \(x\).  These
are the only two starts whose interval sets can change.

Each changed start removes one basis vector and inserts one basis vector.
The \(\ell^1\)-change is therefore at most four.  If the start is passed
through (1.8), the same two starts are the only possible changes; merging
two images can only lower the \(\ell^1\)-distance.  A shortest sequence
of adjacent transpositions and the triangle inequality prove (3.1).
\(\square\)

This is uniform in \(r\).  In particular one pays four, not \(O(n)\),
at each protected depth for one rooted adjacent edit.

## 4. The new component-variance theorem

For \(K\in{\cal K}\), let

\[
 \delta_{K,q}
 =\sum_{P\in R_K}
     \bigl(h_{F^1,P,s-q}-h_{F^0,P,s-q}\bigr).          \tag{4.1}
\]

This is the exact depth-\(q\) load change when component \(K\) is
switched from shore zero to shore one.  Define

\[
 V_H(F^0,F^1)
 =\sum_{K\in{\cal K}}\sum_{q=1}^H
       \frac{\|\delta_{K,q}\|_2^2}{c_q}.              \tag{4.2}
\]

Here

\[
 N_q=\binom n{s-q},\quad
 \lambda_q=\frac W{N_q},\quad
 c_q=\lfloor\lambda_q\rfloor.                         \tag{4.3}
\]

Since \(N_q<W\) for \(q\ge1\), one has \(c_q\ge1\).

### Theorem 4.1 (size-weighted sparse-edit variance)

For arbitrary anchored exact factors \(F^0,F^1\), with no relabeling
relation assumed,

\[
 \boxed{\displaystyle
 \sum_{K\in{\cal K}}\|\delta_{K,q}\|_2^2
       \le4\sum_{K\in{\cal K}}b_KD_K
       =4B\Xi(F^0,F^1)}                                \tag{4.4}
\]

at every depth.  Consequently (0.3) holds.  Both assertions remain true
for the full literal collar profiles (1.8), whose proper ambient cyclic
intervals are distinct within each row.  If the chosen push-forward has
row multiplicity at most \(\rho\), then instead

\[
 \sum_K\|\delta_{K,q}\|_2^2\le4\rho B\Xi,
 \qquad
 V_H\le4\rho B\Xi\sum_{q\le H}c_q^{-1}.              \tag{4.5}
\]

#### Proof

Fix a component \(K\).  A single row histogram in (1.6) is zero-one.
On either shore, the multiplicity of one target among the \(b_K\) rows
therefore lies in \([0,b_K]\).  Hence

\[
                         \|\delta_{K,q}\|_\infty\le b_K.              \tag{4.6}
\]

Lemma 3.1 and the triangle inequality give

\[
 \|\delta_{K,q}\|_1
 \le\sum_{P\in R_K}
       \|h_{F^1,P,s-q}-h_{F^0,P,s-q}\|_1
 \le4D_K.                                             \tag{4.7}
\]

Therefore

\[
 \|\delta_{K,q}\|_2^2
 \le\|\delta_{K,q}\|_\infty
        \|\delta_{K,q}\|_1
 \le4b_KD_K.                                          \tag{4.8}
\]

Sum over components to obtain (4.4), and then over depths with weights
\(1/c_q\) to obtain (0.3).  The proof of Lemma 3.1 already includes the
push-forward (1.8).  For literal ambient cyclic intervals, distinct starts
give distinct proper intervals, so (4.6) remains valid and the collar
statement follows.  Under a general multiplicity-\(\rho\) push-forward,
the corresponding bound is \(\|\delta_{K,q}\|_\infty\le\rho b_K\), which
proves (4.5).
\(\square\)

If \(L=\max_Kb_K\), then

\[
 \Xi=\frac1B\sum_Kb_KD_K
 \le\frac LB\sum_KD_K=L\bar d,                        \tag{4.9}
\]

which proves the advertised cruder criterion (0.6).

There is also an exact converse warning.  If the two rows at a root
\(P\) are identical, their state and colour tokens give only parallel
edges between the same two overlay vertices, so that root is an isolated
common-row component.  After deleting these inert components, every
remaining root has \(d(P)\ge1\).  Hence \(D_K\ge b_K\) on every nontrivial
component and

\[
 \boxed{\displaystyle
       \Xi\ge\frac1B\sum_{K\text{ nontrivial}}b_K^2.}  \tag{4.10}
\]

Indeed, rooted coordinate word equality determines all states (1.4) and
all adjacent unions, so \(d(P)=0\) is exactly row equality.  If a positive
fraction \(\alpha B\) of the changed roots lies in components of size at
least \(\gamma s\), then

\[
 \Xi\ge\frac1B(\gamma s)(\alpha B)
             =\alpha\gamma s.                         \tag{4.11}
\]

Thus any component-expansion theorem putting positive changed-root mass in
\(\Theta(s)\)-sized full components forces \(\Xi=\Omega(s)\), far above
the required \(o(\sqrt s)\).  This rules out certification by the
sparse-edit moment (and item 2 of `GPC_A`); it is not a lower bound on the
actual variance, because signed row effects inside a large component could
cancel.  Any use of that possibility needs a separate cancellation theorem.
Conversely, bounded full components pass
the variance gate when the average edit distance is bounded, but they
still need the independent midpoint/visibility condition of Section 5.

## 5. Exact floor accounting and contraction

Put

\[
 \theta_q=\lambda_q-c_q,qquad
 \mathsf B_H=\sum_{q=1}^H\frac{N_q\theta_q(1-\theta_q)}{c_q},         \tag{5.1}
\]

and, for an exact factor \(F\),

\[
 f_q^F=\mu_q^F-\lambda_q\mathbf1,qquad
 \mathcal E_H(F)=\sum_{q=1}^H\frac{\|f_q^F\|_2^2}{c_q},qquad
 \mathcal Q_H(F)=\mathcal E_H(F)-\mathsf B_H.         \tag{5.2}
\]

The integer floor gives \(\mathcal Q_H(F)\ge0\).
Let

\[
 \bar f=\frac12(f^{F^0}+f^{F^1}),qquad
 \mathsf S_H=\sum_{q=1}^H\frac1{c_q}.                 \tag{5.3}
\]

We now invoke the already audited two-seed component identity: independent
fair choices of the shores in Lemma 2.1 have

\[
 \mathbb E\mathcal E_H(F^\varepsilon)
     =\|\bar f\|_H^2+\frac14V_H(F^0,F^1).             \tag{5.4}
\]

The new input is Theorem 4.1, not a rederivation of (5.4).

### Corollary 5.1 (terminal growing-pair theorem)

Some integral exact anchored factor selected from the overlay cube obeys

\[
 \boxed{\displaystyle
 \mathcal Q_H(F^\varepsilon)
 \le \|\bar f\|_H^2-\mathsf B_H
          +B\Xi(F^0,F^1)\mathsf S_H.}                 \tag{5.5}
\]

In particular, if

\[
 \|\bar f\|_H^2-\mathsf B_H=o(W),qquad
 \Xi\mathsf S_H=o(n),                                \tag{5.6}
\]

then \(\mathcal Q_H(F^\varepsilon)=o(W)\).

#### Proof

Subtract \(\mathsf B_H\) from (5.4), apply (0.3), and choose an outcome no
larger than the expectation.  Conditions (5.6) make the two terms on the
right of (5.5) \(o(W)\), because \(W=nB\).  \(\square\)

At \(H=\lceil A\sqrt s\rceil\), one has

\[
 \mathsf S_H\le H,qquad
 \frac{B\Xi\mathsf S_H}{W}
       \le\frac{(A\sqrt s+1)\Xi}{2s+1}.               \tag{5.7}
\]

Thus \(\Xi=o_A(\sqrt s)\) gives the claimed \(o(W)\) loss with the exact
factor \(1/(2s+1)\) accounted for.

### Corollary 5.2 (one-step midpoint contraction)

Fix \(\eta>0\) and \(\varepsilon_s\ge0\).  Suppose that, for a current
factor \(F^0\), an anchored factor \(F^1\) satisfies

\[
 \|\bar f\|_H^2-\mathsf B_H
 \le(1-\eta)\mathcal Q_H(F^0)+\varepsilon_sW,          \tag{5.8}
\]

and

\[
                    \Xi(F^0,F^1)\mathsf S_H
                         \le\varepsilon_sn.            \tag{5.9}
\]

Then one legal component signing gives

\[
 \boxed{\displaystyle
 \mathcal Q_H(F^\varepsilon)
 \le(1-\eta)\mathcal Q_H(F^0)+2\varepsilon_sW.}       \tag{5.10}
\]

If (5.8)--(5.9) hold for every member of a finite anchored factor fibre,
with fixed \(\eta>0\) and \(\varepsilon_s=o(1)\), that fibre contains a
factor \(F_*\) with

\[
                 \mathcal Q_H(F_*)\le
                     \frac{2\varepsilon_s}{\eta}W=o(W).              \tag{5.11}
\]

#### Proof

Combine (5.5), (5.8), and (5.9) to get (5.10).  For (5.11), choose a
minimizer \(F_*\) of \(\mathcal Q_H\) in the finite fibre.  The child in
(5.10) remains in that fibre by Lemma 2.1, so minimality gives

\[
 \mathcal Q_H(F_*)
 \le(1-\eta)\mathcal Q_H(F_*)+2\varepsilon_sW.
\]

Rearrange.  \(\square\)

This is a genuine non-relabeling contraction theorem: \(F^1\) may be any
second exact anchored factor.  No equality of endpoint energies and no
coordinate group action is used.

## 6. Exact surviving obstructions

The theorem identifies three conditions which growing size alone does not
provide.

### 6.1 A connected full overlay has no rounding freedom

If the full ownership overlay is connected, Lemma 2.1 offers only the two
endpoint factors.  Equivalently, \({\cal K}\) has one component with
\(b_K=B\), and component signing creates no third exact factor.  Thus no
claim of the form

\[
 \text{``two growing exact factors automatically yield heat descent''}
                                                               \tag{6.1}
\]

can be true.  Fragmentation must be proved for the full state-and-colour
overlay, not inferred from a root graph or an \(X\)-only overlay.

### 6.2 Small variance does not create midpoint counterbias

Taking \(F^1=F^0\) gives \(\Xi=0\) and \(V_H=0\), while preserving the
entire pre-existing floor excess.  More generally, suppose two factors
coincide outside \(M\) root rows.  At any fixed target \(T\), every row
contributes either zero or one occurrence, and hence

\[
 \left|\frac{\mu_q^{F^0}(T)+\mu_q^{F^1}(T)}2
               -\mu_q^{F^0}(T)\right|\le\frac M2.     \tag{6.2}
\]

If \(\mu_q^{F^0}(T)-\lambda_q=\rho>M/2\), then

\[
 \boxed{\displaystyle
 \|\bar f_q\|_2^2\ge(\rho-M/2)^2.}                   \tag{6.3}
\]

Thus changing only \(o(B)\) rows cannot counterbalance a target plateau
whose excess is \(\Theta(B)\); its midpoint still has
\(\Theta(B^2)\) energy.  This is the exact point at which the bounded-seed
coverage obstruction meets the heat argument.  Known bounded-seed
suspensions fail before (5.8), not inside the variance proof (4.4).

### 6.3 Port-blind windows remain null directions

If a carrier window contains both complementary fixed ports, its local
intersection is empty and its target is identical on both shores.  Its
row difference and every \(\delta_{K,q}\) are zero.  No component signing
can change load concentrated in that carrier coordinate.

The sparse-edit theorem does not conceal this null space: such a start
simply contributes zero in Lemma 3.1.  Condition (5.8) is deliberately on
the **full** midpoint profile and therefore requires a fresh ancestor or a
different growing factor to repair every blind carrier.  When the seed is
root-scale and \(H=o(s)\), the theorem does not obtain shallow control by
swallowing or propagating through the whole seed; it controls each actual
cyclic start directly.

### 6.4 Individual component curvature need not be negative

The exact floor expansion for a single switch contains a nonnegative
integer curvature.  Theorem 4.1 neither bounds that curvature component by
component nor claims that every switch descends.  It bounds the aggregate
second moment of a fair full-component signing.  Corollary 5.2 then
extracts one global signing after the unrelated endpoint has supplied the
midpoint term (5.8).  Hence the earlier all-local-minimum obstruction and
the present theorem have disjoint quantifiers.

## 7. The exact constructive lemma now required

The following is sufficient and is not supplied by any current theorem.

> **Growing port counterseed lemma \(\mathrm{GPC}_A\).**  For every fixed
> \(A>0\), put \(H=\lceil A\sqrt s\rceil\).  There exist
> \(\eta_A>0\) and \(\varepsilon_s=o_A(1)\) such that every anchored exact
> `D_s`-port factor \(F\) admits another anchored exact `D_s`-port factor
> \(G=G(F)\) for which:
>
> 1. the complete, all-start midpoint satisfies
>    \[
>      \left\|\frac{f^F+f^G}{2}\right\|_H^2-\mathsf B_H
>      \le(1-\eta_A)\mathcal Q_H(F)+\varepsilon_sW;
>    \]
> 2. in the full state-and-colour ownership overlay, with rooted edit
>    distances and \(\Xi\) defined by (0.1)--(0.2),
>    \[
>                       \Xi(F,G)\mathsf S_H
>                             \le\varepsilon_s(2s+1);
>    \]
> 3. the physical carrier map at every root and cyclic start is common to
>    the two shores (as it is for a direct anchored replacement), so the
>    start-resolved estimate of Theorem 4.1 applies.

### Theorem 7.1 (consequence of `GPC_A`)

If \(\mathrm{GPC}_A\) holds, then the anchored factor fibre contains
\(F_*\) with

\[
                       \mathcal Q_H(F_*)=o_A(W).       \tag{7.1}
\]

Define the depth-\(q\) excess above the upper integer floor by

\[
                O_q(F)=\sum_T(\mu_q^F(T)-c_q-1)_+.
\]

Consequently the weighted total lower overload satisfies

\[
          2\sum_{q=1}^H\frac{O_q(F_*)}{c_q}
             \le\mathcal Q_H(F_*)=o_A(W).             \tag{7.2}
\]

#### Proof

The hypotheses of `GPC_A` are exactly (5.8)--(5.9).  Apply Corollary 5.2
to a minimizer in the finite anchored fibre to get (7.1).  The standard
integer-floor inequality gives (7.2).  \(\square\)

The quantitative combinatorial target in item 2 can be read without
Hilbert-space notation.  At \(H=A\sqrt s\), it is enough to construct the
counterseed so that

\[
                         \Xi(F,G)=o_A(\sqrt s).         \tag{7.3}
\]

For example, average rooted edit distance \(O_A(1)\) and maximum full
component size \(o_A(\sqrt s)\) suffice.  Large components are still
allowed when their rows have proportionally smaller total edit distance;
that flexibility is exactly why \(\Xi\), rather than \(\max b_K\), is the
correct parameter.

## 8. Precise boundary

What is proved:

1. direct overlays of arbitrary growing anchored `D_s`-port factors are
   integral and port-valid component by component;
2. rooted adjacent edit distance controls the complete, collar-resolved
   component variance by (0.3), with no missing factor of \(n\);
3. \(\Xi=o(\sqrt s)\) gives \(o(W)\) rounding loss on every fixed Gaussian
   window;
4. the midpoint conditions (5.6) or (5.8) then give, respectively, a
   terminal theorem or an iterative contraction theorem.

What is not proved:

1. existence of a growing counterseed satisfying the full midpoint
   inequality;
2. fragmentation of its **full** ownership overlay at the required
   size-weighted edit scale;
3. a construction of that counterseed from bounded `D_4` or other finite
   operadic packets.

Thus the exact-factor switch/heat lane is not dead, but its surviving form
is a root-scale two-seed theorem.  The next construction must jointly
engineer midpoint counterbias and the moment \(\Xi=o(\sqrt s)\); neither
bounded-seed coverage nor component abundance in an `X`-only graph is an
adequate substitute.
