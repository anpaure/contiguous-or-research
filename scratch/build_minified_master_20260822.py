#!/usr/bin/env python3
"""Build the compact self-contained MASTER_HANDOFF draft.

This is a mechanical section compositor.  It never treats source files as
mathematical premises: selected text is copied into the resulting standalone
document.  The pre-minification MASTER is separately archived.
"""

import gzip
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
with gzip.open(ROOT / "scratch/MASTER_HANDOFF_PREMINIFY_20260822.md.gz", "rt") as source:
    OLD = source.read()
CORE = (ROOT / "scratch/MINIFY_CORE_REPLACEMENT_DRAFT_20260822.md").read_text()
AB = (ROOT / "scratch/MINIFY_GATE_AB_REPLACEMENT_DRAFT_20260822.md").read_text()
GC = (ROOT / "scratch/MINIFY_GATE_C_REPLACEMENT_DRAFT_20260822.md").read_text()
HM = (ROOT / "MATH_THEOREM_PUNCTURED_INDEPENDENT_RESIDUAL_HIGH_MOMENTS_20260822.md").read_text()
NF = (ROOT / "MATH_THEOREM_GATE_B_J2_NEAR_FAR_CUMULANT_AND_VENN_GAP_LOCALIZATION_20260822.md").read_text()


def between(text: str, start: str, end: str | None = None) -> str:
    i = text.index(start)
    j = len(text) if end is None else text.index(end, i)
    return text[i:j].strip() + "\n"


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"expected exactly one occurrence of {old!r}, got {text.count(old)}")
    return text.replace(old, new, 1)


# Front matter and Sections 4--8 from the compact core; Sections 1--3 remain
# the already-audited exact text from the old master.
core = between(
    CORE,
    "# Universal contiguous-subarray OR arrays: authoritative handoff",
    "---\n\n# INTEGRATION MAP",
)
sections_1_3 = between(OLD, "## 1. Problem and exact state model", "## 4. Current coefficient-one architecture")
sections_1_3 = sections_1_3.replace(
    "; the project also stores the resulting word as\n`answers/k17_upper25746.word`",
    "",
)
sections_1_3 = sections_1_3.replace(
    "The proof above is self-contained; the cited implementation is only a reproduction aid.",
    "The proof above is self-contained.",
)
sections_1_3 = sections_1_3.replace(
    "The complete proof of the `sqrt(2)` bound is reproduced in Appendix A;\n"
    "the cited implementation is only a reproduction aid.",
    "The proof is reproduced in Appendix A.",
)
core = replace_once(core, "<!-- Retain current Sections 1--3 verbatim here. -->", sections_1_3.rstrip())


# Appendices A and B are compact already and contain the full unconditional
# construction and the sole [W] exception.
appendix_a_b = between(OLD, "# Appendix A:", "# Appendix C:")


# Appendix C: retain the exact punctured profile, polymer, moment kernel,
# stopped descent, all-depth capacity, positive rounding, generic no-go, and
# stopped protection identity.  Retired collision-energy branches are omitted.
c_intro_through_variance = between(OLD, "# Appendix C:", "## Appendix C.3bis:")
c_intro_through_variance = c_intro_through_variance.replace(
    "This appendix supplies every argument used in Sections 4.3--4.6. The finite checkers cited above are regression tests only; none is a premise of these proofs.",
    "This appendix contains the retained proofs for the direct punctured route. No computation or external file is a premise of an argument below.",
)
c_intro_through_variance = c_intro_through_variance.replace(
    "## Appendix C.1: Boundary-polymer estimate\n\n\n### Proof of the polymer estimate",
    r"""## Appendix C.1: Boundary-polymer estimate

Let \(B_r\) be the punctured boundary graph whose vertices are the \(b\)
boundary cuts and whose \(4r\) edges are the tagged targets of one
configuration:
\[
 B_r=\operatorname {Cay}(\mathbb Z_b,\{\pm1,\pm3\})
       \setminus\{\{0,1\},\{0,3\}\}.
\]
For an edge set \(T\subseteq E(B_r)\), let
\(q(T)=|V(T)|\) be its number of incident boundary cuts.  Define

\[
 \mathcal P_2(z)=
 \sum_{\substack{T\subseteq E(B_r)\\|T|\ge2}}
 |T|^2z^{|T|}r^{-q(T)}.
\]

There are absolute constants \(c_0,c_1>0\) such that, uniformly for
\(0\le z\le c_0\sqrt r\),

\[
 \boxed{\mathcal P_2(z)\le
 c_1\left({z^2\over r^2}+{z^4\over r^2}\right).}
\]

### Proof of the polymer estimate""",
)

rooted_kernel = between(HM, "## 1. Setup and rooted pair kernels", "## 2. Connected overlap tuples")
rooted_kernel = rooted_kernel.replace("## 1. Setup and rooted pair kernels", "## Appendix C.3bis: Rooted overlap kernels")
rooted_kernel = rooted_kernel.replace("### Lemma 1.1", "### Lemma C.3bis.1")
rooted_kernel = rooted_kernel.replace("(1.1)", "(C.3bis.1)")
rooted_kernel = rooted_kernel.replace("(1.2)", "(C.3bis.2)")
rooted_kernel = rooted_kernel.replace("(1.3)", "(C.3bis.3)")
rooted_kernel = rooted_kernel.replace("(1.4)", "(C.3bis.4)")
rooted_kernel = rooted_kernel.replace("(1.5)", "(C.3bis.5)")
rooted_kernel = rooted_kernel.replace("(1.6)", "(C.3bis.6)")
rooted_kernel = rooted_kernel.replace("(1.7)", "(C.3bis.7)")
rooted_kernel = rooted_kernel.replace("(1.8)", "(C.3bis.8)")
rooted_kernel = rooted_kernel.replace("(1.9)", "(C.3bis.9)")
rooted_kernel = rooted_kernel.replace("(1.10)", "(C.3bis.10)")
for i in range(1, 11):
    rooted_kernel = rooted_kernel.replace(f"\\tag{{1.{i}}}", f"\\tag{{C.3bis.{i}}}")

unrooted_moments = r"""### Lemma C.3bis.2 (unrooted surviving-row moments)

Let \(\mathcal N=b!\) be the number of configurations, let
\(\mathsf Z=\sum_FI_F\) count those surviving the independent product
retention, and put \(w_0=x^{2r}y^{2r}\). For every fixed \(s\ge1\), if
\(0<\alpha<1/(6s)\), \(x\ge r^{-\alpha}\), and \(y\ge x\), then
\[
 \boxed{{\mathbb E(\mathsf Z-\mathbb E\mathsf Z)^{2s}
       \over(\mathbb E\mathsf Z)^{2s}}
       =O_s((rx)^{-s}).}                                  \tag{C.3bis.11}
\]

#### Proof

For configurations \(F,G\), put \(t_0(F,G)=|F\cap G|\), and define
\[
\begin{aligned}
 \widehat R_c&={1\over\mathcal N}\max_F\sum_{G\ne F}
                    (x^{-ct_0(F,G)}-1),\\
 \widehat Q_c&={1\over\mathcal N}\max_F
        \sum_{\substack{G\ne F\\t_0(F,G)>0}}x^{-ct_0(F,G)}.
\end{aligned}                                             \tag{C.3bis.12}
\]
For every \(1\le c\le s\),
\(a_c=O(r^{c\alpha})=o(\sqrt r)\), so the polymer estimate applies. Let
\(A=\binom br\) and
\(\vartheta=D_M/\mathcal N=2r/A=e^{-\Theta(r)}\). With
\(a_c=x^{-c}-1\), expand \((1+a_c)^t-1\) and double-count
\(T\subseteq F\cap G\). Singleton \(T\)'s contribute
\(O(\vartheta r a_c)\), since \(F\) has \(4r\) targets and both target
degrees are \(\Theta(D_M)\). For \(|T|\ge2\), C.7 and C.1 give
\[
 {1\over\mathcal N}\sum_{\substack{T\subseteq F\\|T|\ge2}}
 a_c^{|T|}\deg(T)
 \le C\vartheta r^2\mathcal P_2(Ca_c)
 =O_c(\vartheta(a_c^2+a_c^4)).                            \tag{C.3bis.13}
\]
Also
\[
 {1\over\mathcal N}\sum_{G\ne F}\mathbf1_{t_0(F,G)>0}
 \le {1\over\mathcal N}\sum_{G\ne F}t_0(F,G)
 =O(\vartheta r).                                         \tag{C.3bis.14}
\]
Consequently
\[
\begin{aligned}
 \widehat R_c&=O_c(\vartheta(ra_c+a_c^2+a_c^4)),\\
 \widehat Q_c&=O_c(\vartheta(r+ra_c+a_c^2+a_c^4)).
\end{aligned}                                             \tag{C.3bis.15}
\]

Expand the \(2s\)-th centered moment. For distinct rows, join two indices
when their configurations overlap. A singleton dependency component has
zero expectation. After summation, a two-row component costs
\((\mathcal Nw_0)^2\widehat R_1\). For a component of \(j\ge3\) rows,
put \(t_{ab}=t_0(F_a,F_b)\). A uniformly random spanning tree of the
complete graph on \([j]\) contains each pair with probability \(2/j\).
Thus a maximum-weight spanning tree \(T\) satisfies
\[
 \sum_{a<b}t_{ab}\le {j\over2}\sum_{ab\in T}t_{ab}.
\]
The positive-overlap graph is connected, so \(T\) may use only positive
edges. Since \(0<x\le1\),
\[
 x^{-\sum_{a<b}t_{ab}}
 \le\prod_{ab\in T}\mathbf1_{\{t_{ab}>0\}}
                         x^{-(j/2)t_{ab}}.
\]
There are \(j^{j-2}\) labelled trees. Root one and sum its leaves
successively with \(\widehat Q_{j/2}\). The component sum is at most
\[
 O_j((\mathcal Nw_0)^j\widehat Q_{j/2}^{\,j-1}).
\]
Because \(\vartheta=e^{-\Theta(r)}\) while
\(a_c\le r^{c\alpha}\), (C.3bis.15) is smaller than every required fixed
power of \((rx)^{-1}\). Thus a \(j\)-row component costs
\(O_s((\mathcal Nw_0)^j(rx)^{-j/2})\); multiplying components gives the
right side of (C.3bis.11).

For repeated rows use
\((I-w_0)^h=A_h(I-w_0)+B_h\), where
\(|A_h|\le1\) and \(|B_h|\le w_0\), and group equal indicators.
The resulting terms have fewer distinct rows and an extra \(w_0\) for
each constant group. They are negligible because
\(\mathcal Nw_0\ge\exp((2-4\alpha+o(1))r\log r)\).
\(\square\)"""

fixed_slice = between(OLD, "## Appendix C.3ter:", "For the sixth moment")
fixed_slice = fixed_slice.replace(
    "Combining\n(C.3t.4)--(C.3t.8) with C.3bis proves",
    "Combining (C.3t.4)--(C.3t.8) with the product "
    "dependency-component estimate (G.21)--(G.22) gives",
)
fixed_slice = fixed_slice.replace(
    "For distinct configurations `F_1,...,F_j`, let `I_F` be its survival",
    "Fix a root target \\(v\\) and distinct configurations "
    "`F_1,...,F_j` containing \\(v\\). Let `I_F` be its survival",
)
fixed_slice = fixed_slice.replace(
    "gives, uniformly on every exact two-shore\nslice,",
    "gives, uniformly on every exact two-shore slice, where "
    "\\(\\widetilde\\mu=\\mathbb E_{\\rm sl}X_v\\),",
)
fixed_slice = fixed_slice.replace(
    "                         t(F,G)=|(F\\cap G)-\\{v\\}|.\n\\]\n\n"
    "When the union queries",
    "                         t(F,G)=|(F\\cap G)-\\{v\\}|.\n\\]\n\n"
    "For each shore \\(\\sigma\\), let \\(p_\\sigma\\) be its product "
    "retention probability, let \\(a_\\sigma\\) be the number of nonroot "
    "shore-\\(\\sigma\\) targets in one \\(F_i\\), and for "
    "\\(S\\subseteq[j]\\) put\n"
    "\\[\n u_\\sigma(S)=\\left|\\bigcup_{i\\in S}"
    "((F_i\\cap V_\\sigma)-\\{v\\})\\right|.\n\\]\n"
    "Thus \\(w=\\prod_\\sigma p_\\sigma^{a_\\sigma}\\). "
    "When the union queries",
)
fixed_slice = fixed_slice.replace(
    "The identical comparison with the unrooted kernels\ngives",
    "The identical slice comparison applied to Lemma C.3bis.2 gives",
)

c_drift_descent_nogo = between(OLD, "## Appendix C.4:", "## Appendix C.7:")
c_drift_descent_nogo = c_drift_descent_nogo.replace(
    "## Appendix C.4: Cluster drift and its scale\n\n### Proof of the drift identity and its scale",
    r"""## Appendix C.4: Cluster drift and its scale

In the initial full hypergraph, let \(s_e(p)\) be the probability that no
target of a fixed configuration \(e\) is deleted by an accepted
isolated-edge bite, and define \(s_v(p)\) analogously for one target.  Put

\[
 \mathfrak E(e)=\sum_{F:|F\cap e|>0}(|F\cap e|-1).
\]

Then

\[
 \boxed{\left.{d\over dp}\log
 {s_e(p)\over\prod_{v\in e}s_v(p)}\right|_{p=0}
 =\mathfrak E(e),\qquad
 {\mathfrak E(e)\over D_M}=12+O(1/r).}
\]

### Proof of the drift identity and its scale

Write \(t_F=|F\cap e|\) and
\(S(e)=\sum_F\binom{t_F}{2}\).""",
)
c_drift_descent_nogo = c_drift_descent_nogo.replace(
    "## Appendix C.5: Isolated-count covariance and one-cap descent\n\n### Isolated-count covariance and one-cap descent",
    r"""## Appendix C.5: Isolated-count covariance and one-cap descent

Use the process and averages of Section 4.2.  Fix \(K\ge1\), put
\(\gamma=1/(96K)\), \(p_j=\gamma/(r\bar d_j^M)\), and assume the two
maximum-degree caps (4.7) while \(x_j\ge r^{-\alpha}\), where
\(0<\alpha\le1/(256K)\).  Then

\[
 \Pr(\text{the caps persist to the threshold but a bite estimate or
 the descent fails})\le e^{-\Omega(r)}.
\]

On the complementary stopped event the accepted configurations form a
matching leaving \(r^{-\alpha}(1+O_K(1/r))\) of the lower shore and
\(o(1)\) of the middle shore, and the average-degree floor remains at
least \(\exp(r\log r)\).

### Proof""",
)
c_drift_descent_nogo = c_drift_descent_nogo.replace(
    "and a union bound over \\(O(k^2L^2)\\) pairs tends to zero.\n\n"
    "Put \\(Q=\\log(2eDk)\\)",
    "and a union bound over \\(O(k^2L^2)\\) pairs tends to zero.\n\n"
    "Simultaneously, with probability \\(1-o(1)\\), no two points have the "
    "same vector of blocks across all \\(k\\) partitions. For fixed "
    "\\(x\\ne y\\), independence of the partitions gives probability\n"
    "\\[\n \\left({D-1\\over LD-1}\\right)^k=O_{D,k}(L^{-k}).\n\\]\n"
    "There are \\(O_D(L^2)\\) point pairs, and the displayed hypothesis "
    "implies \\(k>2\\), so another union bound is \\(o(1)\\).\n\n"
    "Put \\(Q=\\log(2eDk)\\)",
)
c_drift_descent_nogo = c_drift_descent_nogo.replace(
    "containing \\(x\\).  It is \\(D\\)-regular, and pair codegrees are at most two.",
    "containing \\(x\\). The block-vector event makes these edges distinct, "
    "so the hypergraph is simple. It is \\(D\\)-regular, and pair codegrees "
    "are at most two.",
)
c_drift_descent_nogo = c_drift_descent_nogo.replace(
    "Thus deterministic partitions exist with both properties.",
    "Thus deterministic partitions exist with all three properties.",
)
c_profile_capacity_rounding = between(OLD, "## Appendix C.7:", "## Appendix C.12:")
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(
    "## Appendix C.7: Global boundary-codegree theorem\n\n\n### Proof of the punctured-circulant density bound",
    r"""## Appendix C.7: Global boundary-codegree theorem

For targets \(T\) inside one fixed directed punctured configuration, let
\(q(T)\) be the number of distinct boundary cuts used by those targets.
For every \(|T|\ge2\), an absolute constant \(C\) satisfies

\[
 \boxed{{\deg(T)\over D_M}\le C^{|T|}r^{2-q(T)}.}
\]

The boundary graph is
\(\operatorname {Cay}(\mathbb Z_{2r+1},\{\pm1,\pm3\})\) with the two
start-zero edges deleted, and every subgraph with \(m\) edges and \(v\)
nonisolated vertices satisfies \(m\le2(v-1)\).

### Proof of the punctured-circulant density bound""",
)
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(
    "\\sum_{\\varnothing\\ne S\\subseteq E(F)}z^{|S|}r^{2-v_q(S)}",
    "\\sum_{\\varnothing\\ne S\\subseteq F}z^{|S|}r^{2-v_q(S)}",
)
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(
    "\\mathcal S_q^-(P)={I", "\\mathcal S_q^-(P)=\\{I"
)
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(
    "\\mathcal S_q^+(P)={I", "\\mathcal S_q^+(P)=\\{I"
)
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(
    "B_q\\ge c_BA,quad",
    "B_q\\ge c_BA,\\quad",
)
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(
    "To prove it, The unrooted concentration",
    "To prove it, the unrooted concentration",
)
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(
    "A=|\\mathcal M|,\\qquad\n L=|\\mathcal L|={r\\over r+2}A.",
    "A=|\\mathcal M|,\\qquad B=A/b=\\operatorname{Cat}_r,\\qquad\n "
    "L=|\\mathcal L|={r\\over r+2}A.",
)
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(
    "Let `h_q^-` and `h_q^+` count distinct absent targets in their respective\n"
    "supports, and put",
    "Let \\(\\mathcal H_q^-\\) and \\(\\mathcal H_q^+\\) be the complements "
    "of those two supports in their full layers, put "
    "\\(h_q^\\pm=|\\mathcal H_q^\\pm|\\), and set",
)
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(
    "Continue with Appendix C.9 and let `Q` be its shallow cutoff.",
    "Continue with Appendix C.9, put \\(B=A/b=\\operatorname{Cat}_r\\), "
    "and let `Q` be its shallow cutoff.",
)
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(
    "D_q=|\\Omega_q(T)|=b,k_q!(b-k_q)!={b,b!\\over B_q}.",
    "D_q=|\\Omega_q(T)|=b\\,k_q!(b-k_q)!={b\\,b!\\over B_q}.",
)
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(
    "\\mathbb EZ=b!\\rho,quad \\mu_q:=\\mathbb EX_{q,T}=D_q\\rho,quad\n"
    " {\\mathbb EZ\\over\\mu_q}={B_q\\over b},quad",
    "\\mathbb EZ=b!\\rho,\\quad \\mu_q:=\\mathbb EX_{q,T}=D_q\\rho,\\quad\n"
    " {\\mathbb EZ\\over\\mu_q}={B_q\\over b},\\quad",
)
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(
    "Expanding\n`x^(-|E(F) cap E(G)|)-1=sum_(emptyset!=S subseteq E(F) cap E(G))a^|S|`,\n"
    "then using (C.11.3)--(C.11.7), proves",
    "The covariance ratio is at most\n"
    "\\[\n x^{-|F\\cap G|}-1="
    "\\sum_{\\varnothing\\ne S\\subseteq F\\cap G}a^{|S|}.\n\\]\n"
    "Using (C.11.3)--(C.11.7) therefore proves",
)
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(
    "(C.11.8) at `q=2` and (C.11.2) first give\n"
    "`Z>=mathbb EZ/4` with high probability.",
    "the product-law unrooted concentration (C.3bis.11) with \\(s=1\\) first gives\n"
    "\\(Z\\ge\\mathbb EZ/4\\) with high probability.",
)
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(
    "## Appendix C.11: Shallow external regularity and the survivor-catalogue no-go\n\n"
    "Put `k_q=r-q`, `B_q=binom(b,k_q)`,",
    "## Appendix C.11: Shallow external regularity and the survivor-catalogue no-go\n\n"
    "Continue with \\(b=2r+1\\), \\(A={b\\choose r}\\), "
    "\\(B=A/b\\), and \\(L={b\\choose r-1}\\) from C.9. "
    "Put `k_q=r-q`, `B_q=binom(b,k_q)`,",
)
coalesce = (
    "  Coalescing puncture origins into\n"
    "physical rows changes the catalogue count by relative expectation `O(xy)`\n"
    "and can only lower each external degree, so the same conclusion holds for\n"
    "distinct physical rows."
)
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(coalesce, "")
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(
    "p_j\\le\\tfrac12,quad \\sum_{j<\\tau}",
    "p_j\\le\\tfrac12,\\quad \\sum_{j<\\tau}",
)
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(
    "Gates B may therefore be closed",
    "Gate B may therefore be closed",
)
c_profile_capacity_rounding = c_profile_capacity_rounding.replace(
    "Assume `x=o(1)`, `rx^3->infinity`, put",
    "Assume `x=o(1)`, `x>=r^-alpha` for one fixed `alpha<1/6`, put",
)
c_protection = between(OLD, "## Appendix C.13:", "## Appendix C.14:")
c_protection = c_protection.replace(
    "All stopping times below are bounded by the\n"
    "deterministic round cap.",
    "All stopping times below are bounded by the deterministic round cap. "
    "Fix a positive terminal density scale \\(x\\), put "
    "\\(Q=\\lfloor\\sqrt{rx}/4\\rfloor\\), and use this \\(Q\\) for the "
    "aggregate shallow-depth statements.",
)
c_protection = c_protection.replace(
    "\\Pr\\!\\left(U_\\tau(T)=1,\\\n",
    "\\Pr\\!\\left(U_\\tau(T)=1,\\;\n",
)
c_protection = c_protection.replace(
    "Let \\(U_j(T)\\) indicate that no earlier accepted full row contains \\(T\\).",
    "Let \\(U_j(T)\\) indicate that no earlier accepted full row contains "
    "\\(T\\), and put \\(h_q(n)=\\sum_TU_n(T)\\) over the shore-tagged "
    "depth-\\(q\\) layer (rank \\(r-q\\) or \\(r+1+q\\)).",
)
c_protection = c_protection.replace(
    "B_{q(T)}", "B_{\\operatorname{depth}(T)}"
)
c_protection = c_protection.replace(
    "where \\(\\mathcal H\\) is the restored tagged hole universe.",
    "where \\(\\mathcal H\\) is the restored tagged hole universe and "
    "\\(\\operatorname{depth}(T)\\) is the unique \\(q\\) for which "
    "\\(T\\) belongs to its shore-tagged depth-\\(q\\) layer.",
)

appendix_c = "\n\n".join(
    part.rstrip()
    for part in [
        c_intro_through_variance,
        rooted_kernel,
        unrooted_moments,
        fixed_slice,
        c_drift_descent_nogo,
        c_profile_capacity_rounding,
        c_protection,
    ]
) + "\n"


# Appendix G: exact scalar/Palm finite-bite bridge, the conditional twelfth-
# moment closure, and the current connected-carrier frontier.
g_bridge = between(AB, "## 2. Standalone replacement: exact Palm recursion and finite bites", "## 3. Standalone replacement:")
g_bridge = g_bridge.replace(
    "## 2. Standalone replacement: exact Palm recursion and finite bites",
    "## G.1 Exact Palm recursion, finite bites, and exact-slice mixtures",
)
g_bridge = g_bridge.replace("A.", "G.1.")
g_bridge = g_bridge.replace(
    "The purpose of this block is only to connect G.1 to the product-reference",
    "The purpose of this section is to connect the stopped target G.2 to the product-reference",
)
g_bridge = g_bridge.replace(
    "Equations (G.1.2)--(G.1.16) are the complete bridge needed by G.1.",
    "Equations (G.1.2)--(G.1.16) are the exact finite-bite and slice bridge "
    "used by the stopped target G.2.",
)
g_bridge = g_bridge.replace(
    "objects in G.14--G.19.",
    "objects in G.14, G.15, G.18, and G.19.",
)

g2_body = between(
    OLD,
    "For a fixed even \\(m=2s\\), the already proved product and uniform-slice",
    "Here \\(U_m\\) may be restricted to the upper tail",
)
g2_body = g2_body.replace(
    "For a fixed even \\(m=2s\\), the already proved product and uniform-slice\nrooted component expansion gives, at a reference checkpoint,",
    "For a fixed even \\(m=2s\\), the rooted component expansion from\nC.3--C.3bis gives, at a product reference checkpoint,",
)
g2_body = g2_body.replace(
    "Hence\n\n\\[\n U_m^{\\rm ref}=",
    "Writing \\(U_m^{\\rm ref}\\) for the normalized central moment on the "
    "left of (G.21), we obtain\n\n\\[\n U_m^{\\rm ref}=",
)
g2_body = g2_body.replace(
    "a component of size \\(j\\ge3\\) is\n"
    "summed along a maximum spanning tree and costs "
    "\\(Q_{j/2}^{j-1}\\).\n"
    "Singleton components vanish. Repeated Bernoulli powers reduce to fewer\n"
    "distinct centered indicators. There are only \\(j^{j-2}\\) labelled trees.",
    "a component of size \\(j\\ge3\\) has pair-overlap weights "
    "\\(t_{ab}\\). A uniform spanning tree contains each pair with "
    "probability \\(2/j\\), so a maximum-weight tree \\(T\\) satisfies\n"
    "\\[\\sum_{a<b}t_{ab}\\le{j\\over2}\\sum_{ab\\in T}t_{ab}.\\]\n"
    "Connectedness lets \\(T\\) use positive-overlap edges. Hence "
    "\\(x^{-\\sum t_{ab}}\\le\\prod_{ab\\in T}"
    "\\mathbf1_{\\{t_{ab}>0\\}}x^{-(j/2)t_{ab}}\\), and rooting "
    "\\(T\\) and summing leaves costs \\(Q_{j/2}^{j-1}\\). "
    "Singleton components vanish. Repeated Bernoulli powers reduce to fewer "
    "distinct centered indicators. There are only \\(j^{j-2}\\) labelled trees.",
)
g2_body = g2_body.replace(
    "summed along a maximum spanning tree and costs \\(Q_{j/2}^{j-1}\\).",
    "controlled as follows. Give pair \\(ab\\) weight \\(t_{ab}\\). A "
    "uniform spanning tree contains each pair with probability \\(2/j\\), "
    "so a maximum-weight tree \\(T\\) satisfies "
    "\\(\\sum_{a<b}t_{ab}\\le(j/2)\\sum_{ab\\in T}t_{ab}\\). "
    "Connectedness lets \\(T\\) use only positive-overlap edges. Therefore "
    "\\(x^{-\\sum t_{ab}}\\le\\prod_{ab\\in T}"
    "\\mathbf1_{\\{t_{ab}>0\\}}x^{-(j/2)t_{ab}}\\); rooting the tree "
    "and summing its leaves costs \\(Q_{j/2}^{j-1}\\).",
)
g2 = r"""## G.2 Product high moments and the exact stopped target

The following reference-law estimate is proved; its adaptive stopped
analogue is not.

""" + g2_body.strip() + r"""

Appendix C.3ter transfers (G.22) to uniform two-shore slices.  For the
actual process, on shore \(\sigma\) define
\[
 U_{12,aw_j}(H_j)=
 {1\over n_{j,\sigma}z_{j,\sigma}^{12}}
 \sum_{v:d_j(v)>a w_{j,\sigma}}
       |d_j(v)-z_{j,\sigma}|^{12},
\]
where \(n_{j,\sigma}=|V_\sigma(H_j)|\), \(d_j(v)\) is the degree of
\(v\) in \(H_j\), \(z_{j,\sigma}=n_{j,\sigma}^{-1}
\sum_{v\in V_\sigma(H_j)}d_j(v)\),
\(w_{j,\sigma}\) is a predictable shadow center, and \(a>1\) is fixed.
Stop before any cap, shore-comparability, degree-floor, or fixed
shadow-ratio bound fails.  For a fixed-ratio density bin
\([\xi_\ell,2\xi_\ell)\), let \(\mathcal G_{j,\ell}\) be the event that
round \(j\) precedes every stop and lies in that bin.

The exact missing stopped-law input is [O]:
\[
 \boxed{\mathbb E[U_{12,aw_j}(H_j)\mid\mathcal G_{j,\ell}]
 \le r^{\kappa+o(1)}(r\xi_\ell^3)^{-6}+e^{-\Omega(r)},
 \qquad \kappa<2-20\alpha.}                              \tag{G.29}
\]
It must be accompanied by finite-bite, realized-center, purge, and
accepted-count errors whose total is \(o(r^{-\alpha}/r)\).  These are
premises of a possible Gate-A closure, not conclusions of this section.
The product and exact-slice estimates do not imply (G.29)."""

g14_15 = between(OLD, "### G.14 The exact punctured connected-carrier correction", "### G.16 Directional decomposition")
g14_15 = g14_15.replace("### G.14 ", "## G.14 ", 1).replace("### G.15 ", "## G.15 ", 1)
g14_15 = g14_15.replace(
    "For an ordered $m$-carrier $\\gamma=(v;F_1,\\ldots,F_m)$, define the\n"
    "signed connected statistic $\\Xi_\\gamma$ in (G.14.3.3) below.  If",
    "In a retained target state let $E(H)$ be the surviving catalogue rows,\n"
    "$d_v=|\\{G\\in E(H):v\\in G\\}|$, and\n"
    "$\\Gamma_H(F)=\\{G\\in E(H):G\\cap F\\ne\\varnothing\\}$. For an ordered\n"
    "$m$-carrier $\\gamma=(v;F_1,\\ldots,F_m)$ put\n"
    "$h_\\gamma=|\\bigcup_i\\Gamma_H(F_i)|$ and define the signed connected\n"
    "statistic $\\Xi_\\gamma$ in (G.14.3.3) below. If",
)
g14_15 = g14_15.replace("##### Theorem 3.1", "##### Theorem G.14.3.1")
g14_15 = g14_15.replace("##### 3.2 Removing", "##### G.14.3.2 Removing")
g14_15 = g14_15.replace(
    "The law of total covariance under the Palm mixture is",
    "For completeness, Harris's inequality here follows by induction on the\n"
    "independent Bernoulli coordinates: condition on the last coordinate and\n"
    "use total covariance; the two conditional means are increasing in that\n"
    "coordinate. The law of total covariance under the Palm mixture is",
)
g14_15 = g14_15.replace(
    "For an ordered \\(s\\)-subcarrier\n"
    "\\(\\alpha=(F_1,\\ldots,F_s)\\), define",
    "Put \\(\\mathcal S_v=\\{F\\in\\mathcal C_r:v\\in F\\}\\). For an ordered\n"
    "\\(s\\)-subcarrier \\(\\alpha=(F_1,\\ldots,F_s)\\) from\n"
    "\\(\\mathcal S_v\\), define",
)
g14_15 = g14_15.replace(
    "For every ordered \\(m\\)-carrier,\n\n",
    "For \\(A\\subseteq[m]\\), let \\(\\gamma_A=(F_i)_{i\\in A}\\) "
    "in increasing index order. For every ordered \\(m\\)-carrier,\n\n",
)
g18_19 = between(OLD, "### G.18 The two-shore overlap-cell determinant", "## Appendix H.")
g18_19 = g18_19.replace("### G.18 ", "## G.18 ", 1).replace("### G.19 ", "## G.19 ", 1)
g18_19 = g18_19.replace("proved in C.1 gives", "proved in C.3 and C.3bis gives")
g18_19 = g18_19.replace(
    "The two covariances in G.17 recombine exactly.",
    "The two covariances in the carrier comparison recombine exactly.",
)
g18_19 = g18_19.replace(
    "Hence, for the signed two-star kernel \\(K\\),",
    "Hence, writing \\(K(P)=K_2^\\circ(F,H)\\) for \\(P=(F,H)\\), "
    "with \\(K_2^\\circ\\) defined in (G.15.11),",
)
g18_19 = g18_19.replace(
    "Its first honest sufficient boundary target is\n",
    "Write \\(z=z_\\sigma\\) for the average degree on the root shore. "
    "Its first honest sufficient boundary target is\n",
)
g18_19 = g18_19.replace(
    "Retain middle and lower\ntargets independently with probabilities \\(x,y\\in(0,1)\\).",
    "Retain middle and lower\ntargets independently with probabilities \\(y,x\\in(0,1)\\), respectively.",
)
g18_19 = g18_19.replace(
    "q_P=q_\\tau=x^{4r-t_M-\\delta_M}y^{4r-t_L-\\delta_L}.",
    "q_P=q_\\tau=y^{4r-t_M-\\delta_M}x^{4r-t_L-\\delta_L}.",
)
g18_19 = g18_19.replace(
    "with a middle root, \\(x=3/4,y=1/2,c=12\\),",
    "with a middle root and global shore convention \\((x,y)=(1/2,3/4)\\),\nwith \\(c=12\\),",
)
example_start = g18_19.index("Neither stronger shortcut is valid.")
example_end = g18_19.index("## G.19 Factorial pair-Palm mass is off-root disjoint")
g18_19 = (
    g18_19[:example_start]
    + "No cellwise sign is asserted. The open theorem is the aggregate "
      "punctured estimate in (G.18.9)--(G.18.12), followed by the kernels "
      "\\(3\\le s\\le12\\) and the slice, stopped, center, and purge transfers.\n\n"
    + g18_19[example_end:]
)
g18_19 = g18_19.replace(
    "Condition on retaining a root \\(v\\).  Let \\(\\mathcal F_v\\)",
    "Assume \\(x\\ge r^{-\\alpha}\\) for a fixed \\(\\alpha>0\\), condition "
    "on retaining a root \\(v\\), and let \\(\\mathcal F_v\\)",
)

g_prelude = r"""# Appendix G: Gate A—stopped tail transfer and connected carriers

Let a finite simple hypergraph have shores \(V_\sigma\), every edge meeting
shore \(\sigma\) in \(k_\sigma\) vertices.  Write

\[
 Z=|E|,\qquad n_\sigma=|V_\sigma|,\qquad
 z_\sigma={k_\sigma Z\over n_\sigma},\qquad d(v)=|\{F:v\in F\}|.
\]

For an edge \(F\), put

\[
 \Gamma(F)=\{G:G\cap F\ne\varnothing\},\qquad C_F=|\Gamma(F)|.
\]

For \(v\notin G\), also put

\[
 a_G(v)=|\{F:v\in F,\ F\cap G\ne\varnothing\}|,\qquad
 E_v={1\over d(v)}\sum_{F\ni v}(C_F-d(v)),\qquad
 \bar C={1\over Z}\sum_FC_F.
\]

Swapping the two finite sums gives
\(\sum_{G\not\ni v}a_G(v)=d(v)E_v\).  In the punctured application
\(k_M=k_L=2r\).  All laws below are stopped
before a displayed cap, shore-comparability condition, or degree floor
fails.  No assertion conditions on a future persistence event.

The cap alone cannot propagate itself in a general hypergraph.  Take the
disjoint union of the Fano plane and \(K_4^{(3)}\).  Initially every vertex
has degree three.  If exactly one Fano edge and no other edge is marked,
that edge is isolated; deleting its vertices destroys all seven Fano edges.
The residual has four zero-degree Fano vertices and four degree-three
\(K_4^{(3)}\) vertices, so its average degree is \(3/2\), its maximum is
three, and the maximum/average ratio jumps from one to two.  This event has
positive probability.  A Gate-A proof must therefore use punctured
interval geometry, not the degree cap alone.
"""

appendix_g = "\n\n".join(
    part.rstrip() for part in [g_prelude, g_bridge, g2, g14_15, g18_19]
) + "\n"


# Appendix H: retain only the independently reconstructible zero-avoidance
# lemmas.  The earlier representation/singular-value bridge and finite
# determinant are omitted because their printed enumeration was incomplete.
h_bridge = r"""## H.1 Exact zero-avoidance setup

Put \(b=2r+1\), identify the label and position sets with
\(\Omega=\mathbb Z_b\), and define
\(I_s^w(u)=\{w_u,\ldots,w_{u+s-1}\}\), with cyclic subscripts. A
permutation \(w\) defines

\[
 E(w)=\{(M,I_r^w(u)):u\ne0\}\mathbin{\dot\cup}
      \{(L,I_{r-1}^w(u)):u\ne0\},\qquad
 D_M=2r\,r!(r+1)! .                                      \tag{H.1.1}
\]

Write \(I_s(u)=I_s^{\mathrm{id}}(u)\), and put
\[
 X=\{(M,I_r(u)),(L,I_{r-1}(u)):u\in\mathbb Z_b\},\quad
 A_0=(M,I_r(0)),\quad B_0=(L,I_{r-1}(0)),\quad
 E_0=X-\{A_0,B_0\}.                                      \tag{H.1.2}
\]
For a tagged target \(S=(\sigma,U)\), write \(\underline S=U\). If
\(J\) is a set of tagged targets, \(\deg(S,J)\) counts the permutations
whose configuration contains \(S\) and every member of \(J\). For
\(s\in\{r,r-1\}\), define
\[
\begin{aligned}
 d_s(S)&=|\{w:S\in E(w)\}|,\\
 W_{1,s}(S)&=\sum_{T\in E_0}\deg(S,\{T\}),\\
 e_s(S)&=\sum_{w:S\in E(w)}(|E(w)\cap E_0|-1)_+,\\
 Z_s(S)&=|\{w:S\in E(w),\ E(w)\cap E_0=\varnothing\}|.
\end{aligned}                                             \tag{H.1.3}
\]
The identity \((m-1)_+=m-1+\mathbf1_{\{m=0\}}\) and finite
inclusion--exclusion give
\[
 \boxed{e_s=W_{1,s}-d_s+Z_s,\qquad
 Z_s(S)=\sum_{J\subseteq E_0}(-1)^{|J|}\deg(S,J).}         \tag{H.1.4}
\]

Fix \(2\le j\le r-2\) disjoint ordered label pairs \((a_i,b_i)\), put
\(k=r-2\), \(\ell=r+3\), and, for every \(U\subseteq\Omega\), set
\[
 H_j(U)=\prod_{i=1}^j
 (\mathbf1_{\{a_i\in U\}}-\mathbf1_{\{b_i\in U\}}),
 \qquad H_{s,j}(S)=H_j(\underline S).                     \tag{H.1.5}
\]
For a permutation \(z\), let \(zU=\{z(u):u\in U\}\) and
\(z(\sigma,U)=(\sigma,zU)\). For \(K_t=I_k(t)\), let \(\mathcal B_t\)
be the injective placements of the distinguished labels in which pair one
occupies positions \((t-1,t)\), pair two occupies
\((t+k-1,t+k)\), and every remaining pair has one position in
\(K_t-\{t,t+k-1\}\) and one in its complement after the four boundary
positions are removed. Both orientations are allowed. Thus
\[
 |\mathcal B_t|=2^j(k-2)_{j-2}(\ell-2)_{j-2}.              \tag{H.1.6}
\]
Complete each placement arbitrarily to a permutation \(z\), and put
\(\varepsilon(z)=H_j(zK_t)\). For a coefficient function \(x\) on the
tagged shore-\(s\) targets, define
\[
 \omega_x(t)={1\over|\mathcal B_t|}
 \sum_{z\in\mathcal B_t}\varepsilon(z)
       \sum_{S:|\underline S|=s}x(S)H_j(z\underline S).    \tag{H.1.7}
\]
Only the positions of the distinguished labels occur, so the value is
independent of the completion of \(z\).

The zero-avoidance coefficient has exactly the same boundary profile as
the exposure coefficient. First, \(d_s(S)\) is constant in \(S\) by label
symmetry, and the sum of \(H_j\) over one rank is zero by swapping
\(a_1,b_1\); hence \(\omega_{d_s}=0\). Next fix \(T\in E_0\) and one
boundary placement \(z\). Let \(u_i,v_i\) be the two position coordinates
occupied by event pair \(i\). If \(T\) has equal membership at \(u_i,v_i\),
then \(\tau=(u_i\ v_i)\) fixes \(T\). Pair the inner-sum root set \(S\)
with \(\tau S\). Label equivariance gives
\(\deg(\tau S,\{T\})=\deg(S,\{T\})\), while \(\varepsilon(z)\) is fixed
and \(H_j(z\tau\underline S)=-H_j(z\underline S)\). Thus the two inner
terms cancel. If neither event edge permits this involution, both are
boundaries of \(T\); their intervening arcs have
lengths \(k,\ell\), whereas \(T\) has rank \(r\) or \(r-1\), a
contradiction. Thus the profile of \(S\mapsto\deg(S,\{T\})\) is zero.
Summing over \(T\in E_0\) and using (H.1.4) gives
\[
                         \boxed{\omega_{e_s}(t)=\omega_{Z_s}(t).}
                                                               \tag{H.1.7a}
\]

The blocker coordinates must move with the event. For
\(T=(\sigma,I_{s_\sigma}(u))\in X\), where
\(s_M=r\) and \(s_L=r-1\), define
\[
 \psi_t(T)=\{-2(u-t),-2(u+s_\sigma-t)\}\subseteq\mathbb Z_b.
 \tag{H.1.8}
\]
This bijects \(X\) with the edges of
\(\widetilde B_r=\operatorname {Cay}(\mathbb Z_b,\{\pm1,\pm3\})\),
and sends the event cuts to the fixed roots \(0,5\). The two omitted
targets become
\[
 \mathcal P_t=\{\{2t,2t+1\},\{2t,2t+3\}\},\qquad
 B_r(t)=\widetilde B_r\setminus\mathcal P_t.               \tag{H.1.9}
\]
For an edge set \(J\), abbreviate
\(\deg_t(S,J)=\deg(S,\psi_t^{-1}(J))\). Appendices H.11, H.15, and H.16
prove a local affine identity, a remote shore-difference estimate, and a
Venn-gap bound. They do not prove Gate B: the missing output remains the
compatible all-depth positive cover stated in Section 5 and C.10."""

h11 = r"""## H.11 Sixteen local atoms for zero avoidance [I]

Assume \(r\ge6\). In the nonwrapping integer neighbourhood of the event
roots \(0,5\), the four-vertex supports of blocker terms incident with both
roots are exactly
\[
\begin{array}{rrrr}
(-3,0,2,5),&(-3,0,4,5),&(-3,0,5,6),&(-3,0,5,8),\\
(-1,0,2,5),&(-1,0,4,5),&(-1,0,5,6),&(-1,0,5,8),\\
(0,1,2,5),&(0,1,4,5),&(0,1,5,6),&(0,1,5,8),\\
(0,2,3,5),&(0,3,4,5),&(0,3,5,6),&(0,3,5,8).
\end{array}                                                \tag{H.11.1}
\]
Call this list \(\mathscr V\). For \(V\in\mathscr V\), let \(M(V)\)
be the unique two-edge matching in \(\widetilde B_r[V]\) covering all
four vertices. For the six supports
\[
 \mathscr Q_V=\{(-1,0,2,5),(0,1,2,5),(0,1,4,5),
 (0,2,3,5),(0,3,4,5),(0,3,5,6)\},                         \tag{H.11.2}
\]
the induced graph has one additional connector; write
\(P(V)=E(\widetilde B_r[V])\) for the resulting three-edge path. The
other ten induced graphs equal \(M(V)\). This is exhaustive: choose one
of the four neighbours of each root, giving the sixteen supports in
(H.11.1); on a support in (H.11.2), an edge set incident with all four
vertices is either its endpoint matching or its full path.

For a tagged shore-\(s\) root target \(S\), define the punctured local
coefficient
\[
\begin{aligned}
 \mathcal L_{s,t}(S)={}&
 \sum_{V\in\mathscr V\setminus\mathscr Q_V}
  \mathbf1_{\{M(V)\cap\mathcal P_t=\varnothing\}}
       \deg_t(S,M(V))\\
 &+\sum_{V\in\mathscr Q_V}\left[
  \mathbf1_{\{M(V)\cap\mathcal P_t=\varnothing\}}
       \deg_t(S,M(V))
 -\mathbf1_{\{P(V)\cap\mathcal P_t=\varnothing\}}
       \deg_t(S,P(V))\right],
\end{aligned}                                             \tag{H.11.3}
\]
and put \(L_{s,j}(t)=\omega_{\mathcal L_{s,t}}(t)\). These are exactly
the ten matching terms and the six matching-minus-path pairs, hence 22
signed inclusion--exclusion terms. Every bracket is nonnegative: if the
matching survives the puncture but its path does not, only the positive
term remains; otherwise
\[
 \deg_t(S,M(V))-\deg_t(S,P(V))\ge0                         \tag{H.11.4}
\]
because containment of the full path implies containment of its matching.

Remove the puncture indicators in (H.11.3), call the resulting coefficient
\(\mathcal L_{s,t}^{\circ}\), and set
\(\Omega_{s,j}=\omega_{\mathcal L_{s,t}^{\circ}}(t)\).
Cyclic translation makes \(\Omega_{s,j}\) independent of \(t\). Put
\(C_{s,j}(t)=\Omega_{s,j}-L_{s,j}(t)\).

Before edge orientation is forgotten, the unique edge of a local term
incident with an event root is its supplier. Mark it \(S\) if that root is
the start cut of the corresponding central interval, and \(E\) if it is
the end cut. Let \(F_{s,SS},F_{s,SE},F_{s,ES},F_{s,EE}\) be the complete
signed profile totals by the supplier types at roots \(0,5\). Reflection
\(u\mapsto5-u\) permutes the 22 terms, preserves the degree kernel and the
orientation-free harmonic product, and reverses both suppliers. Hence
\(F_{s,SS}=F_{s,EE}\).

Now \(\mathcal P_0=\{\{0,1\},\{0,3\}\}\), while
\(2\ell=5\pmod b\) gives
\(\mathcal P_\ell=\{\{5,6\},\{5,8\}\}\). At either shift, no local
term contains both omitted edges, because it has a unique supplier at the
affected root. Therefore
\[
 C_{s,j}(0)=F_{s,SS}+F_{s,SE},\qquad
 C_{s,j}(\ell)=F_{s,SS}+F_{s,ES}.                          \tag{H.11.5}
\]
At \(t=3\), \(\mathcal P_3=\{\{6,7\},\{6,9\}\}\), and neither edge
occurs in any of the 22 terms, so \(L_{s,j}(3)=\Omega_{s,j}\). Using
\(F_{s,SS}=F_{s,EE}\) in (H.11.5) gives
\[
 C_{s,j}(0)+C_{s,j}(\ell)=\Omega_{s,j},\qquad
 \boxed{L_{s,j}(0)+L_{s,j}(\ell)=L_{s,j}(3).}              \tag{H.11.6}
\]

For arbitrary \(x,y\in\mathbb R\), put
\(p_t=xL_{r,j}(t)+yL_{r-1,j}(t)\) and \(e_t=1-p_t\). Then
\(e_0+e_\ell-e_3=1\), so Cauchy--Schwarz proves
\[
 \boxed{{1\over b}\min_{x,y}\sum_{t\in\mathbb Z_b}
 (1-xL_{r,j}(t)-yL_{r-1,j}(t))^2\ge {1\over3b}.}           \tag{H.11.7}
\]

For completeness, a boundary-event profile vanishes unless its blocker
edge set is incident with both roots: transposing the two positions on an
unsplit event edge preserves the blocker constraints and reverses the
harmonic sign. The preceding neighbour enumeration therefore contains
every nonzero four-cut term. Let \(R_{s,j}(t)\), denoted \(R_s(t)\) when
\(j\) is fixed in H.15, be the sum of every other nonzero
inclusion--exclusion term. The remote-tail theorem H.15 gives
\[
 \omega_{Z_s}(t)=L_{s,j}(t)+R_{s,j}(t),\qquad
 |R_{s,j}(t)|=O(D_M/r^2),\quad
 |R_{r,j}(t)-R_{r-1,j}(t)|=O(jD_M/r^3).                    \tag{H.11.8}
\]
Thus the local affine gap is rigorous, but these absolute remote bounds do
not transfer it to the full zero-avoidance profile. The compatible
all-depth positive cover required by Gate B remains open."""
h15 = between(OLD, "### H.15 A shore-difference", "### H.16 The exact")
h15 = h15.replace("### H.15 ", "## H.15 ", 1)
h15 = h15.replace(
    "## H.15 A shore-difference current bound and the remote cone",
    "## H.15 A shore-difference current bound for the remote tail [I]",
)
h15 = h15.replace(
    "## H.15 A shore-difference current bound for the remote tail [I]\n\n",
    "## H.15 A shore-difference current bound for the remote tail [I]\n\n"
    "Assume \\(r\\ge6\\) and \\(2\\le j\\le r-2\\), as in H.1 and H.11.\n\n",
)
h15 = h15.replace(
    "Thus for fixed harmonic depth the remote dressing lies in a cone of angle\n"
    "`O(1/r)` about the common-shore line.  This is the relative mechanism which\n"
    "an absolute `O(D_M/r^2)` estimate misses.  It does not by itself prove that\n"
    "the full two-column determinant is nonzero: a rooted-core determinant at\n"
    "the corresponding order is still required.",
    "Equivalently, the remote vector has ambient radius `O(D_M/r^2)` and\n"
    "transverse distance `O(jD_M/r^3)` from the common-shore line. This is an\n"
    "absolute directional statement; it does not assert a relative angle when\n"
    "the common component vanishes, and it does not prove Gate B.",
)
h15 = h15.replace(
    "B_r=\\operatorname {Cay}(\\mathbb Z_b,\\{\\mathord\\pm1,\n"
    "                                      \\mathord\\pm3\\}),",
    "\\widetilde B_r=\\operatorname {Cay}(\\mathbb Z_b,\\{\\mathord\\pm1,\n"
    "                                      \\mathord\\pm3\\}),\\qquad\n"
    " \\mathcal P_t=\\{\\{2t,2t+1\\},\\{2t,2t+3\\}\\},\\qquad\n"
    " B_r(t)=\\widetilde B_r\\setminus\\mathcal P_t,",
)
h15 = h15.replace("Corollary 2.2\nand", "Corollary H.15.2.2\nand")
h15 = h15.replace(
    "with two edges punctured.  The two boundary-event roots",
    "The event-dependent formula is (H.1.9), and blocker terms use "
    "\\(B_r(t)\\). The two boundary-event roots",
)
h15 = h15.replace("##### Theorem 2.1", "##### Theorem H.15.2.1")
h15 = h15.replace(
    "##### Corollary 2.2 (signed families and boundary averaging)",
    "##### Corollary H.15.2.2 (signed families and boundary averaging)",
)
h15 = h15.replace(
    "The next\nfinite calculation is the six-vertex rooted-core determinant at `j=2`;\n"
    "the five-vertex truncation is insufficient and can have the opposite sign.",
    "These estimates do not construct the compatible all-depth positive cover\n"
    "required by Gate B in Section 5 and C.10.",
)
h15 = h15.replace(
    "Let `A_rem(t)` consist of all nonvanishing inclusion--exclusion blocker\n"
    "sets except the sixteen four-vertex rooted atoms (ten two-edge matchings\n"
    "and six matching-minus-path atoms).",
    "Let `A_rem(t)` be the family of all nonzero signed inclusion--exclusion\n"
    "terms `((-1)^|J|,J)` other than the 22 local terms in H.11: ten\n"
    "matching-only terms and, on six supports, one matching and one path term.",
)
h15 = h15.replace(
    "A connected\nshape meeting both `p,q`, outside the six four-vertex paths, has at least\n"
    "five vertices.",
    "A connected rooted shape meeting both `p,q` and not among the six local\n"
    "four-vertex paths has at least five vertices.",
)
h15 = h15.replace(
    "If the rooted shape is one of the\n"
    "sixteen four-vertex atoms but at least one additional component is present,",
    "If the rooted part is one of the 22 local signed terms but at least one\n"
    "additional component is present,",
)
h15 = h15.replace(
    "For fixed `j`, the remote vector is therefore confined to an `O(1/r)`\n"
    "cone around the common-shore line. For `j` comparable with `r`, (H.15.3.6)\n"
    "does not improve the old absolute estimate; the uniform all-depth transfer\n"
    "still needs a depth-sensitive rooted-core argument.",
    "Thus its transverse distance from the common-shore line is\n"
    "`O(jD_M/r^3)` inside an ambient radius `O(D_M/r^2)`. For `j` comparable\n"
    "with `r`, (H.15.3.6) does not improve the absolute estimate.",
)
h15 = h15.replace(
    "For fixed `j`, the remote vector is therefore confined to an `O(1/r)`\n"
    "cone around the common-shore line.  For `j` comparable with `r`, (H.15.3.6)\n"
    "does not improve the old absolute estimate; the uniform all-depth transfer\n"
    "still needs a depth-sensitive rooted-core argument.",
    "Thus its transverse distance from the common-shore line is\n"
    "`O(jD_M/r^3)` inside an ambient radius `O(D_M/r^2)`. For `j` comparable\n"
    "with `r`, (H.15.3.6) gives no improvement over the absolute estimate.",
)
h15 = h15.replace(
    "Applied to the complete remote zero-avoidance tail outside\n"
    "the sixteen four-cut atoms, it gives",
    "Applied to the complete remote zero-avoidance tail outside the 22 signed\n"
    "local terms of H.11, it gives",
)
h15 = h15.replace(
    "B_r(t)=\\widetilde B_r\\setminus\\mathcal P_t,",
    "B_r(t)=\\widetilde B_r\\setminus\\mathcal P_t.",
)
h15 = h15.replace(
    "at most `A^m` connected `m`-edge shapes.",
    "at most `A_*^m` connected `m`-edge shapes for an absolute constant `A_*`.",
)
h15 = h15.replace("`O(rA^m)` placements", "`O(rA_*^m)` placements")
h15 = h15.replace(
    "matching-only terms and, on six supports, one matching and one path term.  The boundary-codegree estimate is",
    "matching-only terms and, on six supports, one matching and one path term. "
    "For this indexed signed family define "
    "\\(\\mathcal M(A_{\\rm rem}(t))="
    "\\sum_{(\\epsilon,J)\\in A_{\\rm rem}(t)}\\deg(J)\\). "
    "The boundary-codegree estimate is",
)
h15 = h15.replace(
    "The theorem is exact before blocker summation and is independent of the\n"
    "number of blocker components.  It proves the missing shore-adapted\n"
    "directional bound at every fixed depth, especially `j=2`.  It does not\n"
    "control cancellation along the common-shore line and it does not certify a\n"
    "nonzero determinant for the fully dressed two-column profile.",
    "The theorem is exact before blocker summation and is independent of the\n"
    "number of blocker components. It controls the shore difference at every\n"
    "fixed harmonic depth, but it neither controls cancellation along the\n"
    "common-shore line nor proves the Gate-B cover.",
)

near_far_gap = between(NF, "## 4. Venn-gap localization", "## 5. The first rootless-edge sector")
near_far_gap = near_far_gap.replace(
    "## 4. Venn-gap localization",
    "### H.16.1 Venn-gap localization",
)
near_far_gap = near_far_gap.replace(
    "Multiplying by the rooted-current bound `2r`",
    "Multiplying by the current bound \\(2r\\) from (H.15.2.2)",
)
near_far_gap = near_far_gap.replace("(0.3)", "(H.16.1)")
near_far_gap = near_far_gap.replace(
    "\\boxed{{\\deg(J)\\over D_M}\\n \\le32^{|J|-1}{r+2\\over\\n  (\\delta+1){r\\choose\\delta+1}}.}",
    "\\boxed{{\\deg(J)\\over D_M}\\n \\le32^{|J|-1}{r+2\\over\\n  (\\delta+1){r\\choose\\delta+1}}.}",
)
for i in range(1, 11):
    near_far_gap = near_far_gap.replace(f"(4.{i})", f"(H.16.{i + 1})")
    near_far_gap = near_far_gap.replace(f"\\tag{{4.{i}}}", f"\\tag{{H.16.{i + 1}}}")
near_far_gap = near_far_gap.replace("(4.4a)", "(H.16.5a)")
near_far_gap = near_far_gap.replace("\\tag{4.4a}", "\\tag{H.16.5a}")
near_far_gap = near_far_gap.replace("### Theorem 4.1", "#### Theorem H.16.1")
near_far_gap = near_far_gap.replace(
    "Stirling's\nbounds now give, uniformly in this range,",
    "The integral comparisons\n"
    "\\(\\int_1^n\\log t\\,dt\\le\\log(n!)"
    "\\le\\int_1^n\\log t\\,dt+\\log n\\) give\n"
    "\\(\\log(n!)=n\\log n-n+O(\\log(n+1))\\). Hence\n"
    "\\[\n"
    " \\log{\\prod_i g_i!\\over r!(r+1)!}\n"
    " =-b\\{H(p)-\\log2\\}+O_{t_0}(\\log r),\n"
    "\\]\n"
    "and therefore, uniformly in this range,",
)
near_far_gap = near_far_gap.replace(
    "Fix `t_0` and a family",
    "Fix `t_0>=2` and a family",
)
near_far_gap = near_far_gap.replace(
    "shapes, each rooted at `{p,q}` and having",
    "shapes, each incident with both event roots `{0,5}` and having",
)
near_far_gap = near_far_gap.replace(
    "On this set Shannon entropy is at least `log 2+c_(t_0)` for some\n"
    "`c_(t_0)>0`: under `max p_i<=1/2`, equality at `log 2` is possible only\n"
    "for `(1/2,1/2,0,...)`, which the lower bound on `p_3` excludes.",
    "Put `H(p)=-sum_i p_i log p_i`. This continuous function has a minimum\n"
    "on the displayed compact set. Under `max p_i<=1/2`, its value is at\n"
    "least `log 2`, with equality only at a permutation of\n"
    "`(1/2,1/2,0,...)`; the lower bound on the third-largest coordinate\n"
    "excludes every equality point. Hence `H(p)>=log 2+c_(t_0)` for some\n"
    "`c_(t_0)>0`.",
)
near_far_gap = near_far_gap.replace(
    "Let `J` contain `t>=1` prescribed tagged central targets.",
    "Let `J subseteq E_0` contain `t>=1` canonical tagged central targets.",
)
near_far_gap = near_far_gap.replace(
    "List the\n`q>=2` distinct original cut positions of `J` in cyclic order, and let\n"
    "their positive elementary gaps be\n\n"
    "\\[\n                         g_1\\ge g_2\\ge\\cdots\\ge g_q,\n"
    " \\qquad\\sum_i g_i=b,",
    "List the `q>=2` distinct original cut positions of `J` in cyclic order and\n"
    "call the resulting positive gaps `d_1,...,d_q`. Reorder this gap multiset\n"
    "nonincreasingly as\n\n"
    "\\[\n                         g_1\\ge g_2\\ge\\cdots\\ge g_q,\n"
    " \\qquad\\sum_i g_i=b,",
)
near_far_gap = near_far_gap.replace(
    "J:\\text{from the fixed core family}\\\n"
    "                         \\text{plus one edge}",
    "J:\\text{from the fixed core family}\\\\\n"
    "                         \\text{plus one edge}",
)

near_far_intro = r"""## H.16 Venn-gap localization [I]

Let \(\varnothing\ne J\subseteq E_0\) be a finite set of canonical tagged central
targets, and let \(\deg(J)\) be the number of directed punctured
configurations containing them. Their standard interval presentations in
(H.1.2) give canonical boundary cuts. List the distinct cuts cyclically,
form their positive cyclic gaps, reorder that multiset as
\(g_1\ge g_2\ge\cdots\ge g_q\), and put
\(\delta=\sum_{i=3}^qg_i\). The proved estimate is

\[
 \boxed{{\deg(J)\over D_M}
 \le32^{|J|-1}{r+2\over
  (\delta+1){r\choose\delta+1}}}
 \qquad(0\le\delta\le r-2).                         \tag{H.16.1}
\]
"""

near_far_outro = r"""The conclusion proved here is exactly this: after fixing
an \(O(1)\)-sized family of blocker-edge patterns incident with both event
roots, adjoining one further blocker edge with Venn-gap defect at least
seven has total normalized profile contribution \(O(r^{-5})\), after the
\(2r\) current factor. It does not sum arbitrary root-incident patterns,
two or more components disjoint from both roots, or the full
inclusion--exclusion series. These retained lemmas do not prove Gate B; the
missing output is the compatible all-depth positive cover stated in
Section 5 and C.10."""

near_far = "\n\n".join([near_far_intro, near_far_gap, near_far_outro])

h_header = """# Appendix H: Gate B—certified zero-avoidance lemmas\n\nOnly independently reconstructible local, shore-current, and Venn-gap\nlemmas are retained. Skipped labels correspond to omitted branches.\n"""
appendix_h = "\n\n".join(
    part.rstrip() for part in [h_header, h_bridge, h11, h15, near_far]
) + "\n"


# Appendix I is a purpose-written standalone replacement.  Rename its local
# C-labels to I-labels to avoid collision with Appendix C.
appendix_i = GC.replace("# Gate C: direct-hole compilation and balanced coset tour banks", "# Appendix I: Gate C—direct-hole compilation and balanced coset tour banks", 1)
appendix_i = appendix_i.replace("C.", "I.")


document = "\n\n".join(
    part.rstrip()
    for part in [core, appendix_a_b, appendix_c, appendix_g, appendix_h, appendix_i]
) + "\n"

# Mechanical hygiene before writing the draft.
for forbidden in [
    "<!-- Retain current Sections",
    "# INTEGRATION MAP",
    "MATH_THEOREM_",
    "MATH_REDUCTION_",
    "MATH_AUDIT_",
]:
    if forbidden in document:
        raise ValueError(f"forbidden integration residue: {forbidden}")

out = ROOT / "scratch/MASTER_HANDOFF_MINIFIED_DRAFT_20260822.md"
out.write_text(document)
print(f"wrote {out}: {document.count(chr(10))} lines, {len(document.encode())} bytes")
