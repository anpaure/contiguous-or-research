# Independent audit of the A/H collar and row-coherent synthesis

Date: 2026-07-25

Scope: pure-mathematical audit of Theorem 1.1, Theorem 2.1, and the
endpoint-throughput argument in Section 3 of
`MATH_ATTACK_AH_COLLAR_AND_ROW_COHERENT_FUSION_20260725.md`.

## Verdict

Theorem 1.1 and Theorem 2.1 are mathematically sound, subject only to
minor asymptotic/integer wording corrections in Theorem 2.1.  Section 3
contains one material scope error: the counted U7 family is the complement
of the **certified support**, not a proved family of actual holes.  Hence
its cardinality cannot be inserted into the otherwise correct endpoint
lower bound without an additional actual-hole hypothesis.

## 1. Theorem 1.1 passes

For a child family \(\mathcal A\subseteq V_q\), residual transportation
has demand

\[
 \lambda_q|\mathcal A|-f_q(\mathcal A)
\]

and available neighboring supply

\[
 \lambda_{q-1}|N_q(\mathcal A)|
 -f_{q-1}(N_q(\mathcal A)).
\]

Because every selected child in \(\mathcal A\) has its selected parent in
\(N_q(\mathcal A)\), their difference is exactly the selected crossing
count.  Thus (PC) is precisely the weighted Hall condition, with the
correct inequality direction.  Total supply and demand are both
\(W-|J|\).

The independently obtained adjacent-rank fractional flows really do
concatenate: at a depth-\(q\) node, the incoming demand and outgoing supply
are both \(\lambda_q-f_q\).  This supplies a feasible fractional flow in
one layered network.  After splitting every node, the bounds

\[
 c_q-f_q(S)\le h_q(S)\le c_q+1-f_q(S)
\]

are integral arc bounds.  The directed network matrix is totally
unimodular, so an integral residual flow exists.  Removing the return arc
leaves an acyclic integral flow and hence a decomposition into
\(W-|J|\) unit paths.  Adding the prescribed \(|J|\) paths gives every root
once and every lower load in \(\{c_q,c_q+1\}\).  No cross-depth ownership
condition is missing.

When \(\lambda_q\) is integral, the displayed upper bound formally permits
\(c_q+1\), but the fixed total layer mass and the lower bounds force every
load to equal \(c_q\); this is not a flaw.

## 2. Theorem 2.1 passes, with minor wording fixes

The high-degree estimate is valid.  With
\(s=\lfloor\varepsilon H/4\rfloor\),

\[
 e(G)\le (s-1)W+(d-s+1)M_s
\]

and \(e(G)\ge\varepsilon HW\), \(d\le2H+2\) imply
\(M_s\ge\eta W\) for a constant \(\eta(\varepsilon)>0\).  Notice that
\(e(G)\le dW\) also implies \(d\ge\varepsilon H\), so \(s\le d\) for
large \(m\).

The top \(r\) rows contain at least \((r/B)M_s\) high starts.  For every
subfamily \(X\) of them,

\[
 s|X|\le e(X,N(X))\le\Delta|N(X)|,
\]

so \(|N(X)|\ge b_s|X|\), where
\(b_s=\lfloor s/\Delta\rfloor=\Theta(H)\).  This is sufficient for the
cloned Hall matching: for an arbitrary subset of clones, its size is at
most \(b_s\) times the size of its underlying starts.  Hence the theorem
does obtain \(\Theta(CW)\) globally distinct target incidences within
\(O(CB/H)\) rows.

To justify the claimed number of used starts explicitly, retain complete
bundles of \(b_s\) matched clone edges, plus at most one partial bundle.
This uses at most \(\lceil D/b_s\rceil\) starts for \(D\) retained edges.
The start--parent cell condition then gives distinct parents at each used
start.

The literal block length is exact:

\[
 n+(2H+1)=n+2H+1.
\]

The repeated prefix through \(E_{2H}\) gives even the start \(j=n-1\)
the required \(2H+2\) consecutive entries.  Moreover

\[
 \bigcup_{a=0}^{t-1}E_{j+a}=I_\pi(j,m-H+t-1),
 \qquad 1\le t\le2H+2,
\]

so every advertised same-start interval is literal.  Finally,

\[
 \left\lceil\frac{CB}{H}\right\rceil(n+2H+1)
 =O(W/H+B+n)=o(W).
\]

Three wording corrections are advisable:

1. State the result for all sufficiently large \(m\), since
   \(b_s=\Theta(H)\), \(r\le B\), and \(H<m\) are asymptotic facts.
2. Replace “exactly \(\delta W\)” by
   \(D=\lfloor\delta W\rfloor\) (or a ceiling consistently).
3. After appending to a pre-existing word, say that the rows **supply
   witnesses for** \(D\) distinct targets.  They need not add \(D\) new
   masks if some were already represented by the old word.

## 3. Section 3 overstates the endpoint lower bound

The algebraic expansion of the certified-complement ledger is correct:

\[
 \mathcal D_R(\alpha R+O(1))
 =\left(\frac{\alpha^2}{2}-\frac{\alpha^3}{3}
 +\frac{\alpha^4}{24}+o(1)\right)R^4
 =\Theta(RM_R).
\]

The generic endpoint lemma is also correct.  If \(C\) of length \(L\) is
appended to an old word, every target not represented before the appendage
must end at a new endpoint.  At one endpoint the suffix ORs form a chain,
so across \(K\) ranks at most \(KL\) genuinely new targets can be added.

The invalid step is the sentence that “the deficit (3.3) forces
\(L=\Omega(M_R)\).”  The independent U7 audit proves only that
\(\mathcal D_R(h)\) is the complement of the **selected certified U7
support**.  It explicitly does not prove that unadvertised intervals of
the old U7 word, seam-crossing intervals, or cross-parent intervals fail
to represent those targets.  Therefore \(\mathcal D_R(h)\) is an exact
literal-repair upper ledger, not a lower bound on the old word's actual
hole set.

The conclusion becomes valid under either of the following corrected
scopes:

* assume that \(\Omega(\mathcal D_R(h))\) members of the certified
  complement are actual holes of the old word; or
* analyze a restricted repair architecture which requires the appendage
  itself to furnish witnesses for every certified-complement target,
  regardless of incidental old coverage.

Without one of these hypotheses, neither the local assertion
\(L=\Omega(M_R)\) nor the global
\(\Omega(\sqrt{k}\,W(k))\) new-target count follows.

There is a second, smaller scope gap in the sentence transporting
Theorem 2.1 to “the corresponding surface scale.”  Theorem 2.1 is stated
for \(W\) Boolean pointed starts grouped into \(B=W/n\) wreath rows.  A
local four-box with width \(M_R\) has not in this note been equipped with
an analogous row system and incidence graph, so the claim that its
appendage uses \(O(M_R/h)\) starts is an analogy, not a consequence of
Theorem 2.1.  The abstract endpoint lemma does not need this analogy, but
its use still requires actual holes as above.

