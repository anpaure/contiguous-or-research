# Independent audit: K12 path-conjugate token energy

Date: 2026-07-25

Audited file:
`MATH_ATTACK_K12_PATH_CONJUGATE_TOKEN_ENERGY_20260725.md`.

Method: two independent pure-mathematics audits, followed by a recheck of
all patched statements. No computation, finite search, web search, SAT, or
solver was used.

## 1. Final verdict

PASS after the corrections recorded below.

The following main claims are correct with their stated scopes:

* the exact changed set \(\mathcal D_i\), its inclusion-exclusion count,
  \(|\mathcal D_1|/W=1/16+O(1/m)\), and
  \(|\mathcal D_1|/R_m=m/2\);
* private one-lower exchange components, including the necessary labelled
  parallel-two-cycle case;
* at most \(2R_m\) genuine distinct-middle paths in one chart;
* at most \(2i\) affected intervals per local row, at most two new runs per
  paired interval bit, and the path-wide
  \(O(W\log ^2m/m)=o(W/H)\) interface;
* the persistent binary laminar clean cover on fixed physical leaf blocks;
* the zero lower-flag action, exact same-chart positive Gram, and lossless
  physical packetization;
* the factor
  \[
  A_i-V_i=4\sum_{q,U}w_q^+\binom{\nu_{i,q}(U)}2;
  \]
* exact autonomous token-core floor descent by one unit of weight per
  captured unordered duplicate;
* simultaneous all-chart central legality for recursively path-conjugate
  factors;
* additive autonomous descent on either disjoint parity layer;
* opposite-sign macroblock closure, \(\Gamma\ge0\), and the exact
  \(1/4\)-normalized Haar identity;
* the collar-capacity estimate \(E_{i,q}\le2(q+1)R_m\);
* the exact first-upper and multidepth visibility conditions;
* the forest holonomy criterion and the triangle obstruction for
  consistently labelled pair exchanges when \(m\ge4\).

No theorem in the report proves the hereditary collision-capture lemma or
the constant-one contiguous-OR theorem.

## 2. Constants and row accounting

The exact local row count is

\[
 R_m=\frac1{2m-1}\binom{2m-1}{m-1}
     =\operatorname{Cat}_{m-1}.
\]

Direct cancellation gives

\[
 |\mathcal D_1|=\binom{2m-3}{m-1},\qquad
 \frac{|\mathcal D_1|}{R_m}=\frac m2.
\]

One row has at most \(2i\) affected circular intervals, so

\[
 r_i\le\min\{2iR_m,|\mathcal D_i|\}.
\]

Toggling one paired interval changes two physical row masks and increases
the total selected-run count by at most two. The conditioned Bernoulli
tail, with its \(3/4+O(1/m)\) raw factor and \(O(\sqrt m)\) conditioning
cost, gives

\[
 \sum_i r_i=O(W\log ^2m/m).
\]

For fine chunks, the corrected hypotheses are

\[
 \ell=\lceil H\omega_m\rceil,\qquad
 \omega_m\to\infty,\qquad
 H\omega_m=o(m),\qquad H\log ^2m=o(m).
\]

Then

\[
 \sum_i b_i\le\frac{T}{\ell}+O(W\log ^2m/m)=o(W/H).
\]

The condition \(H\omega_m=o(m)\) is needed for the positive-density
long-block assertion: the fraction of first-chart tokens in intervals
shorter than \(\ell\) is at most \(4\ell/m=o(1)\). The condition
\(H\log ^2m=o(m)\) is independently needed for the total interface bound.

## 3. Private components and simultaneous path legality

For one adjacent chart, if

\[
 Y_i^0(S)=Y_i^1(T),
\]

the common owner avoids both omitted pairs and is fixed by the coordinate
exchange. Injectivity in the old local factor then gives \(S=T\). If the
two owners over this one lower target agree, the alternatives remain
distinct labelled tokens and form a parallel two-cycle; deleting them as a
common edge would incorrectly erase their possible upper-context action.

For the full path atlas, the domains \(\mathcal D_i\) are disjoint. Owners
from chart \(i\) have original categories in \(\{i,i+1\}\), so only
adjacent charts require inspection. Against the old side of chart \(i+1\),
both potentially colliding owners lie in \(F_{i+1}\), and local
injectivity applies. Against its new side, equality forces the common owner
to avoid \(P_{i+1}\cup P_{i+2}\), so it is fixed by
\(\vartheta_{i+1}\); transporting back again reduces to injectivity in
\(F_{i+1}\). Since
\(\mathcal D_i\cap\mathcal D_{i+1}=\varnothing\), no collision occurs.

Thus arbitrary tokenwise choices over all adjacent charts are centrally
legal. A general such corner is a path-conjugate hybrid, not a coherent
first-avoided matching for overlapping simultaneous priority
transpositions.

## 4. Gram and floor normalizations

For old upper targets \(U,V\subseteq[n]\setminus P_i\),

\[
\left\langle
\mathbf e_{\vartheta_iU}-\mathbf e_U,\,
\mathbf e_{\vartheta_iV}-\mathbf e_V
\right\rangle
=2\mathbf1_{\{U=V,\ U\cap P_{i+1}\ne\varnothing\}}.
\]

Distinct proper windows in one physical row are distinct for
\(q\le m-2\). Therefore duplicate occurrences lie in different physical
blocks and

\[
 A_i-V_i
 =4\sum_{q,U}w_q^+\binom{\nu_{i,q}(U)}2.
\]

The factor \(4\) is exact: the shared-target token inner product is \(2\),
and the squared norm expansion counts each unordered block pair twice.

There are two different floor normalizations.

1. For the autonomous \(T\)-token core,

   \[
   c_\alpha=\left\lfloor\frac{T}{K_\alpha}\right\rfloor.
   \]

   At first upper depth \(K=W>T\), so \(c_{1,+}=0\) and

   \[
   Q_{1,+}=\sum_U\mu(U)(\mu(U)-1).
   \]

   Coherent conjugate endpoints are rankwise energy-equal, and fair
   interval bits give exact descent \(\mathcal C_i\) for the unhalved
   floor energy.

2. For a completed \(W\)-mass word,

   \[
   \bar c_\alpha=\left\lfloor\frac{W}{K_\alpha}\right\rfloor,
   \]

   so \(\bar c_{1,+}=1\). If one common compatible completion \(r\) is
   held fixed across a chart, its exact endpoint drift is

   \[
   g_i=2\sum_{q,U}w_q^+\nu_{i,q}(U)
       \bigl(r_q(\vartheta_iU)-r_q(U)\bigr),
   \]

   and fair interval bits have completed expected energy

   \[
   \bar{\mathcal Q}(M_i^-+r)+g_i/2-\mathcal C_i.
   \]

   On a parity layer this becomes

   \[
   \bar{\mathcal Q}(M_0+r)
   +\frac12\sum_{i\in E}g_i-\sum_{i\in E}\mathcal C_i.
   \]

A completion chosen separately for each corner is not part of this affine
identity. Likewise, literal \(H\)-contexts depend on the final row mask;
their flags are charged separately by the established
\(O(HJ)=o(W)\) transfer bound.

## 5. Dependent macroblocks and span

At each upper depth, a nonzero chart-\(i\) innovation is an oriented
incidence vector from first-avoided category \(i\) to category \(i+1\).
Charts at distance at least two are orthogonal. Neighboring charts can
meet only head-to-tail and hence have nonpositive cross Gram.

Join leaf blocks whenever they carry opposite signs at one common
rank-target coordinate, and take transitive closure. If two distinct
macroblock aggregates had opposite nonzero signs at a coordinate, they
would contain opposite-sign constituent leaves there and would have been
joined. Thus distinct macroblocks have coordinatewise same-sign overlap,
so

\[
 \Gamma=\left\|\sum_Qz_Q\right\|^2-\sum_Q\|z_Q\|^2\ge0.
\]

Fair macroblock bits give

\[
 \mathbb E\mathcal Q
 =\frac{\mathcal Q(M^0)+\mathcal Q(M^1)}2-\frac{\Gamma}{4}.
\]

The fixed leaf-grid run bound survives joining. This is a genuine
dependent leaf selection, but the closure can be one giant block, giving
\(\Gamma=0\). Laminar TU before quotienting does not imply a useful
variance deficit after the identifications.

The multidepth span remains proper: every lower coordinate is annihilated,
and each upper-rank span lies in a path-incidence image. Potentials constant
on activated transport components, together with all isolated target
coordinates, lie in its annihilator. The same block bits couple all
depths, so rankwise dimensions cannot be summed.

## 6. Visibility and holonomy

For two changed first-upper occurrences with common target \(Z\), put

\[
 C=Z\setminus S,\qquad C'=Z\setminus S'.
\]

They are jointly activated exactly when

\[
 \varnothing\ne B\cap Z\subseteq C\cap C'.
\]

For distinct occurrences this means that the contexts share the
designated coordinate in \(Z\) and its pair mate lies outside \(Z\).
Disjoint contexts are invisible to every common-partner adjacent chart
which fixes both lower endpoints. At general depth the exact condition is

\[
 \varnothing\ne B\cap U
 \subseteq (U\setminus S)\cap(U\setminus S').
\]

Thus positive switched mass and seam abundance do not imply a positive
fraction of captured collision energy.

For factor conjugacy on a graph, choose tree transports \(g_v\). Every
non-tree edge imposes the exact root-factor invariance

\[
 g_v^{-1}\vartheta_{uv}g_uF_{\rm root}=F_{\rm root}.
\]

Forests are automatically consistent. With the consistently labelled
pair exchanges of the report, a triangle holonomy exchanges two pair
blocks, hence is a product of two transpositions on the local
\((2m-1)\)-point universe. It fixes an \((m-1)\)-target when \(m\ge4\).
Exactness would force the unique owning cyclic row to be holonomy-fixed,
but an involutive reflection of an odd cycle has \(m-1\), not two,
transpositions. This contradiction proves the stated triangle no-go.

The ladder of rails and rungs is only a degree-three coordinate scaffold:
the rungs do not create additional factor-conjugacy relations or
renewability.

## 7. Certified boundary

The report proves an exact positive long-block theorem:

\[
\text{captured duplicate curvature}
\quad\Longrightarrow\quad
\text{equal floor-energy descent}
\]

with at most two new selected runs per paired physical block and a total
literal context charge \(o(W)\).

It does not prove that the captured curvature is a fixed fraction of the
unresolved energy. The missing statement is precisely the hereditary
collision-capture/background-drift lemma displayed in the report. The
parallel-token majority, collar capacity, disjoint-context sector, possible
giant macroblock closure, and cyclic holonomy are real design constraints,
not a global impossibility theorem.
