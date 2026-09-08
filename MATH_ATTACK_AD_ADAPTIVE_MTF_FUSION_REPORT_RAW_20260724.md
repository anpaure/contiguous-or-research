Outcome: sparse fusion is impossible, but a genuinely overlapping MTF refactor exists. It preserves every certified first-band edge color and reduces the new short-run charge from \(O(H^2)\) to \(O(H)\). The Gaussian-window support lemma remains unproved, so this does not yet prove coefficient one.

## 1. Sparse fusion is ruled out at depth two

Let \(A_1,\dots,A_L\) be any OR word and \(\mathcal R_r(A)\) its represented \(r\)-sets. Choosing one witness interval for each \(S\in\mathcal R_r(A)\), their left endpoints are distinct: intervals with a common left endpoint are nested, so their unions are comparable, impossible for distinct equal-rank sets. The same holds for right endpoints.

Moreover, each endpoint letter is contained in its target. Hence

\[
\boxed{
|\mathcal R_r(A)|
\le
\#\{j:|A_j|\le r\}.
}
\tag{1}
\]

For \(k=2m\),

\[
\frac{N_2}{W}
=
\frac{\binom{2m}{m-2}}{\binom{2m}{m}}
=
\frac{m(m-1)}{(m+1)(m+2)}
=
1-\frac{4m+2}{(m+1)(m+2)}.
\tag{2}
\]

Thus a word covering rank \(m-2\) needs \(W-O(W/m)\) letters of size at most \(m-2\).

The \(T\)-capped first-band rainbow word has no such letters. The singleton-capped version has exactly \(2c_+\), where \(c_+=o(W)\) is its number of nontrivial components. Consequently:

- inserting \(R\) letters and changing \(t\) old letters requires
  \[
  R+t\ge N_2-2c_+=W-o(W);
  \]
- pure insertion yields length at least \(2W-o(W)\);
- any same-length fusion must replace \(W-o(W)\) old positions;
- private letterwise substitution with overhead \(E\) satisfies
  \[
  E\ge \frac{N_2-2c_+}{2}
  =\left(\frac12-o(1)\right)W.
  \]

This includes arbitrary cross-block witnesses. Therefore appending a deep core, preserving the facet word as a subsequence, or privately refining its letters cannot work.

More generally, if \(H=\lfloor A\sqrt m\rfloor\) and \(d_j=(m-|A_j|)_+\), then every band-covering word obeys

\[
\sum_j\bigl(\min\{H,d_j\}-1\bigr)_+
\ge
\sum_{q=2}^{H}\binom{2m}{m-q},
\tag{3}
\]

and hence

\[
\frac{1}{W\sqrt m}
\sum_j\bigl(\min\{H,d_j\}-1\bigr)_+
\ge
\int_0^A e^{-t^2}\,dt+o_A(1).
\tag{4}
\]

A Gaussian-depth solution therefore needs pervasive nested endpoint sharing.

## 2. Exact depth-two shared-seam escape

For a two-sided-rainbow path \(T_0,\dots,T_s\), put

\[
C_i=T_{i-1}\cap T_i,\qquad
U_i=T_{i-1}\cup T_i,
\]

and

\[
D_i=C_i\cap C_{i+1},\qquad
V_i=U_i\cup U_{i+1}.
\]

Depth-one rainbowness gives

\[
|D_i|=m-2,\qquad |V_i|=m+2.
\]

For each internal facet,

\[
C_i\setminus(D_{i-1}\cup D_i)
\]

is empty or a singleton \(\{x_i\}\); the latter occurs exactly for a coordinate run \(0,1,1,0\).

Emit the shared word

\[
a_0,C_1,D_1,Z_2,D_2,\ldots,D_{s-1},C_s,a_s,
\]

where \(Z_i\) is omitted in the good case and equals \(\{x_i\}\) otherwise. Then

\[
C_i=D_{i-1}\cup Z_i\cup D_i,
\]

and interval hulls of consecutive facet witnesses recover every \(T_i,U_i,V_i\).

If \(c_1\) counts one-edge components, \(c_{\ge2}\) longer components, and \(\rho_2\) length-two positive runs, the exact completed length is

\[
\boxed{
W+2c_{\ge2}+c_1+\rho_2
+2(N_1-e)+M_2^-+M_2^+.
}
\tag{5}
\]

Moreover,

\[
\rho_2
\le W-N_2+M_2^-
=O(W/m)+M_2^-.
\tag{6}
\]

Hence, for the existing first-band forest, the first new lemma is exactly

\[
\boxed{M_2^-+M_2^+=o(W).}
\tag{7}
\]

This remains unproved: depth-one rainbowness does not prevent nonadjacent collisions among the \(D_i\) or \(V_i\).

## 3. Main surviving construction: adaptive MTF fusion

Let \(m\ge2H\) and let

\[
T_0,\ldots,T_{K-1}\in\binom{[2m]}m,
\qquad
T_{i+1}=T_i-\{p_i\}+\{q_i\}.
\]

Call a positive coordinate run short if it is entered at \(q_i\), exited at \(p_j\), and \(j-i\le H\).

### MTF lift theorem

The path admits a one-update MTF lift exposing a saturated radius-\(H\) chain through every \(T_i\) if and only if it has no internal short positive run.

No restriction on zero-runs is necessary.

For sufficiency, extend the departure sequence by \(H\) dummy departures at the right boundary. This is possible because the intersection of the last \(H+1\) middle sets has size at least \(m-H\ge H\). Define

\[
L_i=T_i\setminus\{p_i,\ldots,p_{i+H-1}\}.
\tag{8}
\]

Choose an ordered partition \(\Theta_0\) of \([2m]\setminus T_0\) whose first \(H\) blocks are singletons, and recursively set

\[
\Theta_{i+1}=(\{p_i\},\,\Theta_i-\{q_i\}).
\tag{9}
\]

Then

\[
\Pi_i=
\bigl(
L_i,
\{p_{i+H-1}\},\ldots,\{p_i\},
\Theta_i
\bigr)
\tag{10}
\]

is an ordered-partition state exposing every rank \(m-H,\ldots,m+H\), and

\[
L_{i+1}=L_i-\{p_{i+H}\}+\{q_i\}.
\tag{11}
\]

Direct block subtraction gives the exact transition

\[
\boxed{\Pi_{i+1}=M_{L_{i+1}}(\Pi_i).}
\tag{12}
\]

If \(q_i\) is among the current upper singleton markers, it is deleted there; if it lies in a later tail block, it is extracted from that block. In either case, prepending \(p_i\) leaves at least \(H\) singleton upper markers. This is why arbitrary zero-runs are legal. The stricter first-wave rotor relation is only a subrelation of this physical MTF transition.

The exposed lower masks are

\[
P^-_{i,q}
=
T_i\setminus\{p_i,\ldots,p_{i+q-1}\}
=
\bigcap_{s=0}^{q}T_{i+s},
\tag{13}
\]

while the upper masks are adaptive recency flags

\[
P^+_{i,q}
=
T_i\cup\{\text{first \(q\) singleton blocks of }\Theta_i\}.
\tag{14}
\]

At depth one,

\[
P^-_{i,1}=T_i\cap T_{i+1},
\qquad
P^+_{i+1,1}=T_i\cup T_{i+1}.
\tag{15}
\]

Thus every old two-sided-rainbow edge color survives exactly.

Initialize \(\Pi_0\) by writing its \(2H+2\) blocks in reverse, then append \(L_1,\ldots,L_{K-1}\). The exact component length is

\[
K+2H+1.
\tag{16}
\]

All bulk entries have rank \(m-H\); this is precisely the pervasive low-letter replacement required by (1)–(4).

### Necessity audit

Suppose consecutive MTF states all expose ranks \(m-H,\ldots,m\). A coordinate newly entering the middle set lies in the new first block. Unless it is moved again, each later update can create at most one additional block before its residual block.

For that coordinate to lie beyond the middle boundary, there must be:

- at least one block forming the rank-\((m-H)\) prefix; and
- the following \(H\) singleton blocks.

Thus at least \(H+1\) later blocks must precede it. It cannot leave within \(H\) transitions. This proves the positive-run condition is intrinsic to any one-update-per-edge saturated fusion, not an artifact of the construction.

## 4. Exact forest-level bound

Let the original spanning path forest have:

- \(c\) components;
- \(e\) globally distinct two-sided first-band colors;
- \(\rho_H\) internal positive runs of length at most \(H\).

Cut before every such run. There are exactly \(c+\rho_H\) resulting components.

A cut does not lose its old first-band colors. If the cut edge removes \(p\), choose \(p\) as:

- the first dummy terminal departure on the left, giving the lower color \(T-p\);
- the first initial upper singleton on the right, giving the upper color \(T'+p\).

Let \(\widetilde M_q^\pm\) be the missing supports of the adaptive flags (13)–(14). Concatenating the component words and appending only genuinely missing masks gives

\[
\boxed{
L_{\mathrm{band}}
\le
W+(2H+1)(c+\rho_H)
+2(N_1-e)
+\sum_{q=2}^{H}
\bigl(\widetilde M_q^-+\widetilde M_q^+\bigr).
}
\tag{17}
\]

This is the decisive improvement over ordinary erosion repair: the short-run charge is \(O(H\rho_H)\), not \((H^2+2H)\rho_H\). The price is that the deeper upper masks are adaptive MTF recency flags rather than consecutive path unions.

## 5. Exact remaining lemma in lane AD

For every fixed \(A>0\), put \(H=\lceil A\sqrt m\rceil\).

The surviving theorem is:

\[
\boxed{
H(c+\rho_H)
+
\sum_{q=2}^{H}
\bigl(\widetilde M_q^-+\widetilde M_q^+\bigr)
=o(W),
}
\tag{AD\(_A\)}
\]

for one spanning chronology whose first-band edge defect satisfies \(N_1-e=o(W)\).

This is unproved.

The current near-rainbow forest supplies only

\[
N_1-e=o(W),\qquad c=o(W).
\]

Unconstrained endpoint splicing can reduce \(c\) to \(O(W/m)\), which is sufficient for \(Hc=o(W)\), but it gives no control of new short positive runs or adaptive deep-label collisions. Restricting the splices to preserve both conditions is the still-missing dynamic support theorem.

The deep core also cannot be selected independently in this construction. Once the middle chronology is fixed,

\[
L_i=P^-_{i,H}
=
T_i\setminus\{p_i,\ldots,p_{i+H-1}\}
\]

is forced, and the bulk update is \(L_{i+1}\). A separate core can fuse only if it realizes these same future-deletion minima, or if one abandons the canonical first-band adjacency witnesses and proves a different global MTF state-transversal theorem.

If \((\mathrm{AD}_A)\) holds for every fixed \(A\), (17) gives a \(W+o(W)\) central-band word. The audited outer tails cost

\[
O\!\left((1+A^2)e^{-A^2+o(1)}W\right).
\]

Taking \(m\to\infty\) and then \(A\to\infty\) proves coefficient one in even dimension, and the standard one-bit lift gives odd dimension.

This route directly constructs a literal OR word. It proves neither MWB nor labelled wreath synchronization, and it requires no exact wreath factor. The lane is exhausted at \((\mathrm{AD}_A)\): sparse fusion is rigorously impossible, depth two reduces to two support defects, and the strongest surviving all-window construction is the adaptive MTF refactor (17).
