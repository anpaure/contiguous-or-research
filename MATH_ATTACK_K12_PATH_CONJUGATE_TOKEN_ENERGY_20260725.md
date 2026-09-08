# Lane K12: path-conjugate token blocks, exact floor descent, and the collision-span ceiling

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
SAT, or solver is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 T=\binom{n}{m-1}=\frac{m}{m+2}W,
\]

and partition \(2m\) coordinates into ordered pairs

\[
 P_i=\{a_i,b_i\}\quad(1\le i\le m),
\]

leaving one coordinate unpaired. Let

\[
 R_m=\frac1{2m-1}\binom{2m-1}{m-1}
     =\operatorname{Cat}_{m-1}.
\]

For every adjacent pair of pair-nodes define

\[
 \vartheta_i=(a_i\ a_{i+1})(b_i\ b_{i+1}).
\tag{0.1}
\]

Choose one exact local factor \(F_1\) on \([n]\setminus P_1\), and
recursively choose

\[
 F_{i+1}=\vartheta_iF_i.
\tag{0.2}
\]

The report proves the following package.

1. For the adjacent-priority swap \(P_iP_{i+1}\leftrightarrow
   P_{i+1}P_i\), every changed lower target is a private exchange cell:
   either a two-edge open path with distinct middle owners or a labelled
   parallel two-cycle with the same middle owner. Arbitrary tokenwise
   choices are therefore centrally legal. The genuine distinct-owner
   paths number at most \(2R_m=O(W/m)\); the positive-density reservoir is
   mostly a parallel-token, not a central-owner, reservoir.

2. In every physical row the changed starts form at most \(2i\) circular
   intervals. One bit per paired interval costs at most two new selected
   runs. At \(i=1\), the changed domain has
   \((1/16+O(1/m))W\) tokens and average paired interval length at least
   \(m/4\). If
   \[
   \ell=\lceil H\omega_m\rceil,\qquad
   \omega_m\to\infty,\qquad H\omega_m=o(m),
   \]
   and \(H\log ^2m=o(m)\), splitting into length-\(\ell\) chunks produces
   a persistent laminar clean-cover atlas with total new run charge
   \(o(W/H)\).

3. Every lower flag is fixed. An upper flag has the exact innovation

   \[
   \mathbf e_{\vartheta_iU}-\mathbf e_U.
   \]

   Within one adjacent chart all cross Grams are nonnegative, and physical
   interval packetization loses no curvature. If
   \(\nu_{i,q}(U)\) is the number of changed old occurrences of a moved
   upper target \(U\), the autonomous token-core floor energy has the exact
   fair-bit descent

   \[
   \boxed{
   \mathbb E\mathcal Q(M_\varepsilon)
   =\mathcal Q(M^-)
    -\sum_{q\le H}w_q^+
      \sum_U\binom{\nu_{i,q}(U)}2.}
   \tag{0.3}
   \]

   Thus every captured unordered duplicate pays exactly its weight, while
   every interval bit costs at most two runs. This is an exact
   floor-corrected contraction, not a generic seam count. Coherent global
   endpoints are energy-flat; mixed interval corners are not globally
   conjugate, so (0.3) is compatible with that flatness.

4. The recursion (0.2) supports one simultaneous product cube over all
   adjacent charts. Every corner is a lower-saturating, middle-injective
   token matching, although a general corner is not a first-avoided
   matching for a priority permutation. Its total fixed interface is

   \[
   O(W\log ^2m/m)=o(W/H)
   \tag{0.4}
   \]

   whenever \(H\log ^2m=o(m)\). Either parity layer of disjoint adjacent
   charts has an additive version of (0.3). Across the full path only
   neighbouring charts interact, and those interactions have the opposite
   sign. An explicit opposite-sign closure gives a legal dependent
   macroblock selection, but it may collapse to one block and therefore
   gives no quantitative contraction by itself.

5. The exact ceiling is a collision-capture ceiling. In one local row,
   at depth \(q\), at most \(2(q+1)\) starts move. No lower flag moves, and
   the first-upper edit capacity of one adjacent chart is only
   \(4R_m=O(W/m)\). At first upper depth a collision is captured exactly
   when its two two-coordinate contexts share the designated partner
   coordinate whose mate lies outside the common upper target. Disjoint
   contexts are invisible. Hence neither positive owner density nor clean
   cover implies that (0.3) is a fixed fraction of the total energy.

6. Forests of conjugacy relations are consistent; cycles impose an exact
   holonomy invariance. For the natural pair exchanges, a triangle is
   impossible for every \(m\ge4\). Thus arbitrary fresh re-pairing cannot
   be installed in one fixed local-factor system without a new symmetry
   theorem.

Consequently the requested long-block energy mechanism exists and is
literal, integral, multidepth, and persistent. What remains unproved is a
hereditary collision-dispersion inequality showing that the captured
quantity in (0.3), after the necessary dependent closures and prior
history, dominates a fixed fraction of the unresolved energy. No
constant-one conclusion is claimed.

## 1. Adjacent-priority support

Use predecessor-owner tokens. In a row

\[
 \pi=(x_0,\ldots,x_{2m-2})
\]

of \(F_P\), with cyclic indices, put

\[
 S_t=I_\pi(t,m-1),\qquad
 Y_t=I_\pi(t-1,m),
\tag{1.1}
\]

and, for \(1\le q\le H\le m-2\),

\[
 L_q(t)=I_\pi(t+q-1,m-q),\qquad
 U_q(t)=I_\pi(t-1,m+q).
\tag{1.2}
\]

The first-avoided matching assigns a lower target \(S\) to the first pair
it avoids. Compare the priority orders which differ only by interchanging

\[
 A=P_i,\qquad B=P_{i+1}.
\]

### Lemma 1.1 (exact changed set)

The changed lower targets are exactly

\[
 \mathcal D_i=\left\{S\in\binom{[n]}{m-1}:
 S\cap P_h\ne\varnothing\ (h<i),\quad
 S\cap A=S\cap B=\varnothing\right\}.
\tag{1.3}
\]

Moreover

\[
 |\mathcal D_i|
 =\sum_{t=0}^{i-1}(-1)^t\binom{i-1}{t}
   \binom{2m-3-2t}{m-1}.
\tag{1.4}
\]

In particular

\[
 |\mathcal D_1|=\binom{2m-3}{m-1}
 =\frac{m(m+1)}{4(2m-1)(2m+1)}W
 =\left(\frac1{16}+O(m^{-1})\right)W,
\tag{1.5}
\]

and

\[
 \frac{|\mathcal D_1|}{R_m}=\frac m2.
\tag{1.6}
\]

#### Proof

A set missing an earlier pair is decided before \(A,B\) in both orders. A
set missing exactly one of \(A,B\) is assigned to that same pair in both
orders. A set meeting every earlier pair and missing both is assigned to
the one placed first. This proves (1.3). Inclusion-exclusion over the
\(i-1\) earlier pairs gives (1.4), and direct factorial cancellation gives
(1.5)--(1.6). \(\square\)

The sets \(\mathcal D_i\) are pairwise disjoint. Indeed, if \(i<k\), a
member of \(\mathcal D_i\) avoids \(P_i\), while a member of
\(\mathcal D_k\) meets \(P_i\).

The usual conditioned Bernoulli estimate gives an absolute constant \(C\)
such that

\[
 |\mathcal D_i|
 \le C\sqrt m\binom{2m-1}{m-1}(3/4)^{i-1}.
\tag{1.7}
\]

There is a minor constant trap in (1.7). First sample each coordinate of
the \((2m-3)\)-point complement of \(A\cup B\) independently with
probability \(p=(m-1)/(2m-3)\), and then condition on total size \(m-1\).
Before conditioning, the earlier disjoint-pair events are independent and
their common pair-meeting probability is

\[
 1-\left(\frac{m-2}{2m-3}\right)^2
 =\frac34+O(m^{-1})>\frac34.
\]

Its ratio to \(3/4\), raised to at most \(m\), is bounded by an absolute
constant. The probability of the conditioning event is
\(\Omega(m^{-1/2})\), so dropping the intersection with that event and
dividing by its probability costs \(O(\sqrt m)\). Thus (1.7) is correct
after changing \(C\), but a termwise "at most \(3/4\)" proof is not.

## 2. Exact component sizes under conjugate factors

Fix one adjacent chart and write

\[
 \vartheta=(a_i\ a_{i+1})(b_i\ b_{i+1}),\qquad
 F_B=\vartheta F_A.
\]

For \(S\in\mathcal D_i\), the set \(S\) is fixed pointwise by
\(\vartheta\). Hence its two labelled token alternatives satisfy

\[
 e_B(S)=\vartheta e_A(S),\qquad
 Y_B(S)=\vartheta Y_A(S).
\tag{2.1}
\]

### Theorem 2.1 (private-cell theorem)

The affected two-coloured overlay has exactly one lower target in every
connected component. If \(Y_A(S)\ne Y_B(S)\), the component is the
two-edge open path

\[
 Y_A(S)-S-Y_B(S).
\]

If \(Y_A(S)=Y_B(S)\), it is a labelled parallel two-cycle. In particular,
arbitrary choices of one alternative for every \(S\in\mathcal D_i\) form
a lower-saturating, middle-injective matching together with the unchanged
background.

#### Proof

Suppose an old owner and a new owner coincide:

\[
 Y_A(S)=Y_B(T)=\vartheta Y_A(T).
\]

The old owner avoids \(A\), while the new owner avoids \(B\); their common
value therefore avoids \(A\cup B\) and is fixed by \(\vartheta\). Hence

\[
 Y_A(S)=Y_A(T).
\]

The owner map inside the exact factor \(F_A\) is injective, so \(S=T\).
Same-side owners are already distinct. Every old alternative is
compatible with the common background in the old coherent endpoint, and
every new alternative is compatible with that same background in the new
coherent endpoint. Thus no mixed-background collision occurs. The two
component types follow. \(\square\)

The parallel case must not be deleted as a common edge: the two labelled
tokens can have the same central incidence and different upper-context
flags.

There are few genuine distinct-owner paths. Write

\[
 Y_A(S)=S\cup\{x(S)\}.
\]

Since \(S\) avoids \(A\cup B\), the owners differ exactly when
\(x(S)\in B\). In one cyclic row, each of the two coordinates of \(B\)
is the predecessor of exactly one start. Therefore

\[
 \boxed{
 \#\{S\in\mathcal D_i:Y_A(S)\ne Y_B(S)\}\le2R_m=O(W/m).}
\tag{2.2}
\]

Thus the \(1/16\)-density first chart is a large labelled-context cube but
has only boundary-scale nontrivial central-owner motion.

## 3. Row intervals and persistent laminar clean cover

In an \(F_i\)-row the affected-start predicate is

\[
 [S_t\cap P_{i+1}=\varnothing]
 \ \wedge\
 \bigwedge_{h<i}[S_t\cap P_h\ne\varnothing].
\tag{3.1}
\]

For one coordinate pair, the starts at which a length-\((m-1)\) window
avoids that pair form at most two circular intervals. The boundary of
(3.1) is contained in the union of the boundaries of its \(i\) pair
predicates. Hence one row contains at most \(2i\) affected circular
intervals.

Let \(r_i\) be the number of maximal affected intervals in \(F_i\). Their
conjugate intervals in \(F_{i+1}\) are paired one-for-one. Then

\[
 \boxed{r_i\le\min\{2iR_m,|\mathcal D_i|\}.}
\tag{3.2}
\]

Toggling one paired interval deletes a selected interval in one row and
inserts its mate in another. Each operation raises the run count by at
most one, so

\[
 \boxed{J(M_\varepsilon)\le J(M_0)+2r_i.}
\tag{3.3}
\]

For all charts at once, (1.7) and a split at
\(t=\lceil20\log m\rceil\) give

\[
 \begin{aligned}
 \sum_i r_i
 &\le \sum_{i\le t}2iR_m+\sum_{i>t}|\mathcal D_i|\\
 &=O(W\log ^2m/m).
 \end{aligned}
\tag{3.4}
\]

The first-avoided endpoint already has

\[
 J(M_0)=O(W\log ^2m/m).
\tag{3.5}
\]

Hence every maximal-interval corner in the path atlas obeys

\[
 J=O(W\log ^2m/m)=o(W/H)
\tag{3.6}
\]

provided \(H\log ^2m=o(m)\).

For finer energy control, split every paired interval into consecutive
blocks of target length \(\ell\), leaving at most one shorter remainder.
Let \(b_i\) be the number of paired block bits. Then

\[
 b_i\le\frac{|\mathcal D_i|}{\ell}+r_i,
\qquad
 \sum_i b_i\le\frac{T}{\ell}+O(W\log ^2m/m),
\tag{3.7}
\]

because the \(\mathcal D_i\) are disjoint. Every block bit costs at most
two new runs. If

\[
 \ell=\lceil H\omega_m\rceil,\qquad \omega_m\to\infty,
 \qquad H\omega_m=o(m),\qquad H\log ^2m=o(m),
\tag{3.8}
\]

then

\[
 2\sum_i b_i=o(W/H).
\tag{3.9}
\]

At \(i=1\), (1.6) and \(r_1\le2R_m\) imply average paired interval length
at least \(m/4\). Intervals shorter than \(\ell\) contain at most
\(2R_m\ell\) tokens, so their fraction of \(\mathcal D_1\) is at most

\[
 \frac{2R_m\ell}{|\mathcal D_1|}=\frac{4\ell}{m}.
\tag{3.10}
\]

Thus \(H\ll\ell\ll m\) gives a positive-density reservoir of genuine long
row blocks.

Place the blocks of each paired interval as the leaves of a binary interval
tree. The trees are disjoint across physical intervals, so their node
sets form a laminar family. Toggling an internal node means toggling all
of its descendant leaves. Theorem 2.1 makes every such history centrally
legal. The final row mask can change only at the fixed leaf cuts, so
repeated node toggles do not accumulate new seams: the uniform final bound
is still (3.9). This is the promised persistent laminar clean-cover atlas.

The exact affine energy identities below apply to the selected token core.
The standard \(H\)-contexts used to literalize the fixed leaf boundaries
are charged separately by \(O(HJ)=o(W)\); their flags are not silently
inserted into the affine identity.

## 4. Multidepth action and exact floor descent

For a changed token \(S\in\mathcal D_i\), (1.2) and pointwise fixation of
\(S\) give

\[
 L_q^B(S)=L_q^A(S),
\qquad
 d_{i,S,q}^+=\mathbf e_{\vartheta_iU_q(S)}-\mathbf e_{U_q(S)}.
\tag{4.1}
\]

Thus every lower-depth action is zero.

If \(U,V\subseteq[n]\setminus P_i\), then

\[
 \left\langle
 \mathbf e_{\vartheta_iU}-\mathbf e_U,
 \mathbf e_{\vartheta_iV}-\mathbf e_V
 \right\rangle
 =2\mathbf1_{\{U=V,\ U\cap P_{i+1}\ne\varnothing\}}.
\tag{4.2}
\]

Indeed, a cross equality \(U=\vartheta_iV\) would make the common set avoid
both \(P_i,P_{i+1}\), hence fixed by \(\vartheta_i\), and gives the
cancelling zero case. Therefore all same-chart Grams are nonnegative.
Distinct proper cyclic windows of one row are distinct for \(q\le m-2\),
so innovations inside one physical block are orthogonal.

Give every signed depth an arbitrary finite nonnegative weight
\(w_q^\pm\). For an upper target \(U\), let

\[
 \nu_{i,q}(U)
 =|\{S\in\mathcal D_i:U_q(S)=U,\ U\cap P_{i+1}\ne\varnothing\}|.
\tag{4.3}
\]

If \(z_C\) is the action of a paired physical block, put

\[
 D_i=\sum_Cz_C,\qquad
 A_i=\|D_i\|_w^2,\qquad
 V_i=\sum_C\|z_C\|_w^2.
\]

Then packetization is lossless and

\[
 \boxed{
 A_i-V_i
 =4\sum_{q\le H}w_q^+
   \sum_U\binom{\nu_{i,q}(U)}2.}
\tag{4.4}
\]

The factor \(4\) is essential: one shared nonfixed old target gives inner
product \(2w_q^+\), and the norm expansion counts each unordered block
pair twice.

We now include the integer floors exactly. At a signed target rank
\(\alpha=(q,\pm)\), let \(K_\alpha\) be the number of target sets. Every
token corner has mass \(T\), so write

\[
 T=c_\alpha K_\alpha+\delta_\alpha,
 \qquad0\le\delta_\alpha<K_\alpha,
 \qquad\lambda_\alpha=T/K_\alpha.
\tag{4.5}
\]

For an integral load vector \(x\), use the unhalved autonomous token-core
floor excess

\[
 Q_\alpha(x)=
 \sum_Z(x_Z-c_\alpha)(x_Z-c_\alpha-1)
 =\|x-\lambda_\alpha\mathbf1\|_2^2-B_\alpha,
\tag{4.6}
\]

where \(B_\alpha=\delta_\alpha(K_\alpha-\delta_\alpha)/K_\alpha\).
Let

\[
 \mathcal Q=\sum_\alpha w_\alpha Q_\alpha.
\]

At the first upper rank, \(K=W\) and \(T<W\), so \(c_{1,+}=0\) and

\[
 Q_{1,+}=\sum_U\mu(U)(\mu(U)-1)
        =2\sum_U\binom{\mu(U)}2.
\tag{4.7}
\]

No singular \(1/c_{1,+}\) weight is used for this autonomous core. This
must be distinguished from a completed \(W\)-mass word. For the latter
write

\[
 \bar c_\alpha=\left\lfloor\frac{W}{K_\alpha}\right\rfloor,\qquad
 \bar Q_\alpha(x)=
 \sum_Z(x_Z-\bar c_\alpha)(x_Z-\bar c_\alpha-1).
\tag{4.7a}
\]

Put \(\bar{\mathcal Q}=\sum_\alpha w_\alpha\bar Q_\alpha\).

In particular \(\bar c_{1,+}=1\). The \(c_{1,+}=0\) normalization in
(4.7) is only the autonomous \(T\)-token-core floor.

Let \(M_i^-,M_i^+\) be the two coherent priority endpoints of chart \(i\).
Their lower loads agree. At every upper depth, target coordinates split
by their first avoided pair. On the union of the \(P_i,P_{i+1}\) strata,
\(\vartheta_i\) carries the complete endpoint load vector of \(M_i^-\) to
that of \(M_i^+\); all other strata agree. Hence

\[
 \mathcal Q(M_i^-)=\mathcal Q(M_i^+)
\tag{4.8}
\]

rank by rank. This is coherent global-bit flatness.

Choose every physical block bit independently and fairly. The
mean-plus-variance identity, (4.4), and (4.8) give

\[
 \boxed{
 \mathbb E\mathcal Q(M_\varepsilon)
 =\mathcal Q(M_i^-)
  -\mathcal C_i,\qquad
 \mathcal C_i:=
 \sum_{q\le H}w_q^+\sum_U
 \binom{\nu_{i,q}(U)}2.}
\tag{4.9}
\]

Some deterministic integral corner attains the same upper bound and obeys
the deterministic boundary estimate. If the halved factorial energy is
used, the guaranteed descent is \(\mathcal C_i/2\).

Equation (4.9) is the exact requested energy contraction per \(O(1)\) new
boundaries. The whole adjacent stratum as one bit has variance \(A_i\)
and zero Haar gap. Refining it into physical blocks has variance \(V_i\);
the removed cross terms are \(A_i-V_i=4\mathcal C_i\). Thus coherent
endpoint flatness and mixed-corner descent (strict when
\(\mathcal C_i>0\)) are compatible.

A completion chosen separately for each corner is outside the affine
identity. Suppose instead that one centrally compatible common completion
\(r=(r_\alpha)\), of the missing \(W-T\) flags per rank, is held fixed
across the cube. It need not be \(\vartheta_i\)-symmetric. With the
full-word floor (4.7a), the coherent endpoint drift is

\[
 g_i:=\bar{\mathcal Q}(M_i^++r)
      -\bar{\mathcal Q}(M_i^-+r)
 =2\sum_{q,U}w_q^+\nu_{i,q}(U)
   \bigl(r_q(\vartheta_iU)-r_q(U)\bigr),
\tag{4.9a}
\]

with the old/new sign convention of (4.1). Fair interval bits therefore
have expectation

\[
 \bar{\mathcal Q}(M_i^-+r)+\frac{g_i}{2}-\mathcal C_i.
\tag{4.9b}
\]

Thus descent below the completed current endpoint additionally requires
the exact background-drift inequality

\[
 \mathcal C_i\ge
 \frac{\bar{\mathcal Q}(M_i^++r)
       -\bar{\mathcal Q}(M_i^-+r)}2
 +\rho\,\bar{\mathcal Q}(M_i^-+r)
\tag{4.10}
\]

for a desired \(\rho\)-contraction. The standard literal contexts are
instead charged as the separate \(o(W)\) term noted after (3.10).

## 5. Simultaneous path-conjugate cube

The recursion (0.2) imposes every adjacent conjugacy relation on one fixed
factor family. The individual changed domains are disjoint, but adjacent
charts share a local factor. The following legality assertion is therefore
not automatic from disjoint parity layers.

### Theorem 5.1 (all-chart product legality)

Keep the common tokens of the original first-avoided matching. For every
\(i\) and every \(S\in\mathcal D_i\), choose independently either its
\(F_i\)-token or its \(F_{i+1}\)-token. Every resulting set of tokens is a
lower-saturating, middle-injective matching.

#### Proof

The \(\mathcal D_i\) are disjoint, so lower saturation is immediate. A
chosen owner from chart \(i\) has original first-avoided category \(i\) or
\(i+1\). Hence nonadjacent charts cannot collide.

Consider charts \(i\) and \(i+1\). The only unresolved case has the chart
\(i\) token on its \(F_{i+1}\)-side. If the chart \(i+1\) token is also on
its \(F_{i+1}\)-side, equality of owners contradicts injectivity inside
\(F_{i+1}\). If the latter is on its \(F_{i+2}\)-side and the owners are
equal, the common owner avoids both \(P_{i+1},P_{i+2}\), so it is fixed by
\(\vartheta_{i+1}\). Transporting it back gives equality of two
\(F_{i+1}\)-owners, again forcing equality of the lower targets. But
\(\mathcal D_i\cap\mathcal D_{i+1}=\varnothing\).

Every alternative is compatible with the unchanged background because it
occurs with that background in its corresponding one-chart coherent
endpoint. Thus no owner collision occurs. \(\square\)

A general corner of Theorem 5.1 is a path-conjugate hybrid token matching,
not a first-avoided matching for simultaneous overlapping priority swaps.

For either parity class \(E\subseteq\{1,\ldots,m-1\}\), the adjacent
blocks are disjoint. Their upper target strata are disjoint, so their
innovations are orthogonal and their coherent simultaneous endpoints are
rankwise energy-equal. Therefore fair independent physical block bits
give the additive autonomous-core descent

\[
 \boxed{
 \mathbb E\mathcal Q(M_{E,\varepsilon})
 =\mathcal Q(M_0)-\sum_{i\in E}\mathcal C_i.}
\tag{5.1}
\]

Every corner has the common persistent boundary bound (3.9).
If the same common full-word completion \(r\) is held fixed, then instead

\[
 \mathbb E\bar{\mathcal Q}(M_{E,\varepsilon}+r)
 =\bar{\mathcal Q}(M_0+r)
  +\frac12\sum_{i\in E}g_i-\sum_{i\in E}\mathcal C_i.
\tag{5.1a}
\]

Across the full path, a nonzero depth-\(q\) innovation from chart \(i\)
has its negative target in first-avoided category \(i\) and its positive
target in category \(i+1\). Therefore charts at distance at least two are
orthogonal. Neighbouring charts can meet only as positive head versus
negative tail, and hence

\[
 \langle d_i,d_{i+1}\rangle_w\le0.
\tag{5.2}
\]

This gives the exact multidepth span picture: at each upper rank the raw
innovations are oriented incidence vectors on a category-monotone path
graph. Their span lies in that graph's incidence image; its annihilator
contains potentials constant on every activated transport component and
all isolated targets. Every lower coordinate is in the annihilator. The
same physical bits couple these incidence images across all depths, so
rankwise dimensions cannot be added independently.

There is an exact dependent selection which removes the negative
cross-block interactions. Start from the physical leaf blocks and join
two blocks whenever, at some signed rank and target, one block has a
positive coefficient and the other a negative coefficient. Take
transitive closure and call the resulting unions macroblocks. Distinct
macroblocks now have coordinatewise same-sign overlap, hence nonnegative
Gram. Indeed, if two distinct aggregate blocks had opposite nonzero signs
at one coordinate, they would contain constituent leaf blocks with
opposite signs there, and those leaves would have been joined.

If \(z_Q\) is the action of macroblock \(Q\), put

\[
 \Gamma=\left\|\sum_Qz_Q\right\|_w^2-
         \sum_Q\|z_Q\|_w^2\ge0.
\tag{5.3}
\]

Independent fair macroblock bits remain centrally legal by Theorem 5.1,
and the fixed leaf-grid boundary bound is unchanged. For the two all-side
endpoints \(M^0,M^1\),

\[
 \boxed{
 \mathbb E\mathcal Q(M_Q)
 =\frac{\mathcal Q(M^0)+\mathcal Q(M^1)}2-\frac\Gamma4.}
\tag{5.4}
\]

Thus a \(\rho\)-contraction from \(M^0\) follows from the exact condition

\[
 \boxed{
 \Gamma\ge
 2\bigl(\mathcal Q(M^1)-\mathcal Q(M^0)\bigr)
 +4\rho\,\mathcal Q(M^0).}
\tag{5.5}
\]

This is a genuine bounded-interface dependent-selection theorem. It is
not yet quantitative: opposite-sign closure may create one giant
macroblock, in which case \(\Gamma=0\). Nor does the original laminar TU
property imply a variance deficit after arbitrary block identifications.

## 6. Collar capacity and the exact visibility obstruction

Fix one chart \(i\). Since \(S\cap P_{i+1}=\varnothing\) and

\[
 U_q(S)\setminus S
\]

has \(q+1\) row positions, a fixed coordinate of \(P_{i+1}\) can make an
upper innovation nonzero at at most \(q+1\) starts in one row. Hence

\[
 E_{i,q}:=
 |\{S\in\mathcal D_i:U_q(S)\cap P_{i+1}\ne\varnothing\}|
 \le2(q+1)R_m.
\tag{6.1}
\]

Consequently

\[
 \sum_S\|d_{i,S,q}\|_2^2\le4(q+1)R_m,
 \qquad
 \|D_{i,q}\|_1\le4(q+1)R_m
 =O(qW/m).
\tag{6.2}
\]

At \(q=1\), one adjacent chart edits at most \(4R_m=O(W/m)\) upper
occurrences. No lower occurrence moves at any depth. Thus a diffuse
linear defect outside the pair collar cannot be repaired by one chart.

There is an exact first-upper collision test. Suppose two changed tokens
have the same old upper target \(Z\), and write

\[
 C=Z\setminus S,\qquad C'=Z\setminus S',
 \qquad |C|=|C'|=2.
\tag{6.3}
\]

Under the standing hypothesis that both occurrences lie in the same
changed domain \(\mathcal D_i\), they are activated by partner pair
\(B=P_{i+1}\) if and only if

\[
 \boxed{
 \varnothing\ne B\cap Z\subseteq C\cap C'.}
\tag{6.4}
\]

For distinct occurrences, \(C\ne C'\), so (6.4) says that the two
contexts share one coordinate \(b\), and the designated mate of \(b\) in
\(B\) lies outside \(Z\). If \(C\cap C'=\varnothing\), the collision is
invisible to every common-partner adjacent chart which fixes both lower
endpoints. More generally, under the analogous changed-domain hypothesis
at depth \(q\), activation is equivalent to the exact condition

\[
 \varnothing\ne B\cap U
 \subseteq (U\setminus S)\cap(U\setminus S').
\tag{6.5}
\]

At the first upper rank, (4.7) says the total autonomous energy is twice
the number of all unordered collision pairs, whereas \(\mathcal C_i\)
counts only those pairs passing (6.4) for the designated chart. Therefore
positive switched-token density, long blocks, and nonnegative Grams do not
imply

\[
 \mathcal C_i\ge\eta\mathcal Q
\]

for any fixed \(\eta>0\). This is the exact innovation-dispersion gate.

## 7. Forest consistency and cyclic holonomy

The path recursion (0.2) is a special case of a general forest theorem.
Let \(G\) be a graph whose vertices are omitted coordinate pairs and whose
oriented edge \(uv\) carries a coordinate exchange \(\vartheta_{uv}\)
mapping
\([n]\setminus P_u\) to \([n]\setminus P_v\). On a forest, choose a root
factor in every component and transport it uniquely along the tree. All
edge conjugacies are then simultaneous; the reverse orientation carries
\(\vartheta_{vu}=\vartheta_{uv}^{-1}\).

For a graph with cycles, choose a spanning forest and transports \(g_v\)
from each root. A non-tree edge \(uv\) is compatible exactly when the
cycle holonomy

\[
 h_{uv}=g_v^{-1}\vartheta_{uv}g_u
\tag{7.1}
\]

stabilizes the root factor. Thus all cycle holonomies must lie in the
setwise automorphism group of that exact factor; this condition is also
sufficient.

For the consistently labelled pair exchanges used here, triangle-wide
conjugacy is impossible when \(m\ge4\). Indeed, pairwise prescriptions on
three pair-nodes force the root factor to be invariant under the holonomy
which exchanges the other two pair blocks, a product of two coordinate
transpositions on its \(2m-1\)-point local universe. This holonomy fixes
an \((m-1)\)-target chosen from the remaining \(2m-5\) fixed coordinates.
Exactness gives a unique cyclic row owning that target; invariance of the
factor forces that row to be holonomy-fixed.

But the stabilizer of an unoriented cyclic order on \(2m-1\) distinct
points is dihedral. A nontrivial involutive reflection on an odd cycle has
exactly \(m-1\) transpositions, not two, for \(m\ge4\). Hence no row is
fixed, a contradiction. (For oriented rows, the cyclic stabilizer is
smaller.)

Thus a forest, including the full path (0.2), is unconditional, while a
cyclic menu of fresh pair partners requires genuinely new factor symmetry.
The coordinate graph consisting of the two rails

\[
 a_i a_{i+1},\qquad b_i b_{i+1},
\]

and the rungs \(a_ib_i\) is connected of maximum degree three after
attaching the unpaired coordinate at an endpoint. This is a degree-three
coordinate scaffold for the path conjugacies; the rungs do not supply
additional factor-conjugacy relations or renewal, and connectivity alone
does not imply the collision-capture inequality of Section 6.

## 8. Precise proved and conditional boundary

The following statements are proved.

* A same-orientation adjacent conjugate chart has private one-lower
  components, exact tokenwise integrality, \(O(1)\) new boundaries per
  paired physical block, and the exact autonomous token-core floor descent
  (4.9).
* The first chart contains a \((1/16+o(1))W\) switched-token reservoir, and
  all but \(O(\ell/m)\) of that reservoir lies in physical intervals of
  length at least \(\ell\).
* A recursively conjugate path of fixed local factors supports a
  simultaneous all-chart token cube. Its maximal-interval or fine
  laminar-clean-cover boundary is \(o(W/H)\), uniformly over every history.
* Either parity layer has additive autonomous token-core
  captured-collision descent (5.1), with the completed correction (5.1a).
* Opposite-sign closure gives the exact dependent macroblock identity
  (5.4)--(5.5) without sacrificing integrality or the boundary ledger.
* Every lower flag is invariant; the upper action is confined to the
  pair collar and the incidence-image span described in Sections 5--6.
* Forest conjugacy is consistent, while triangle renewal is obstructed by
  holonomy.

The following statement is still unproved and is exactly what a
constant-factor iteration would need.

> **Hereditary collision-capture and drift lemma.** At every unresolved
> low-run token state of energy \(\mathcal Q=\Omega(W)\), some available
> parity chart or opposite-sign macroblock quotient has captured curvature
> and endpoint drift satisfying (4.10) or (5.5) with a fixed
> \(\rho>0\), after conditioning on all previous laminar choices; the same
> fixed leaf grid remains available until the energy is \(o(W)\).

Neither the \(1/16\) owner density, the clean-cover property, nor the
degree-three coordinate menu proves this lemma. Disjoint first-upper
contexts give a rigorous zero-curvature sector, and cyclic re-pairing is
not freely renewable. Accordingly, the present report proves the exact
long-block energy switch and sharpens the remaining gate, but does not
claim MWB, labelled synchronization, or

\[
 \nu(k)\le(1+o(1))W(k).
\]

## 9. Relation to the concurrent adjacent-swap audits

The coherent-bit flatness theorem in
PAIR_PRIORITY_SWAP_EXACT_FLOOR_ENERGY_AUDIT_20260725.md and the refined
interval descent in
MATH_AUDIT_PAIR_OMISSION_INTERVAL_CORNERS_AND_FLOOR_DESCENT_20260725.md
are compatible: the first forces all physical interval bits to agree, and
the second releases them. The single-chart identities here agree with
those audits, including the factor \(4\) in (4.4), the autonomous
first-upper floor \(c_{1,+}=0\), and the separate literal-context charge.

The new contributions of this report are the simultaneous path-conjugate
product legality theorem, the persistent path-wide laminar clean cover,
the additive parity-layer descent, the opposite-sign dependent closure,
the exact multidepth incidence-span description, and the forest/triangle
holonomy boundary.
