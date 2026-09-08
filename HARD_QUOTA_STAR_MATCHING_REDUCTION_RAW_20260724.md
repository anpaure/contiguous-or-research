# Proposed hard-quota star-matching reduction (raw)

This note records the theorem submitted in the main thread for independent
audit. It does not claim MWB.

Put

\[
n=2m+1,\quad W=\binom nm,\quad N_q=\binom n{m-q},\quad
c_q=\lfloor W/N_q\rfloor,\quad t_m=W/n.
\]

## Weight mass

With \(\lambda_q=W/N_q\),

\[
\lambda_q=\prod_{i=0}^{q-1}\frac{m+2+i}{m-i},
\qquad
\frac1{c_q}\le\frac2{\lambda_q}.
\]

Using \(\log(1+x)\ge x/(1+x)\), the proposal obtains

\[
\log\lambda_q\ge \frac{q(q+1)}{2m+1}
\]

and therefore

\[
\sum_{q=1}^{m-1}\frac1{c_q}=O(\sqrt m).
\tag{1}
\]

## Exceptional core charging

Let an exact factor split as \(F=G\sqcup B\). Assume that for every
controlled depth there is a balanced full-mass quota vector \(b_q\) with

\[
\mu_q^G(S)\le b_q(S)\quad\text{for every target }S.
\tag{2}
\]

Since each exceptional wreath supplies \(n\) occurrences at each depth,

\[
O_q(F)\le n|B|.
\]

Together with (1),

\[
\sum_{q\le H}\frac{O_q(F)}{c_q}
=O(n|B|\sqrt m)
=O\left(W\sqrt m\frac{|B|}{t_m}\right).
\tag{3}
\]

Thus \(|B|=o(t_m/\sqrt m)\) suffices for MWB; in particular
\(|B|=O(t_m/m)\) gives \(O(W/\sqrt m)\).

Also

\[
O_q(F)=\frac12\min_{b\text{ balanced}}\|\mu_q-b\|_1.
\tag{4}
\]

## Star matching

Let the full wreath hypergraph have the middle \(m\)-sets as vertices and
unoriented wreath supports as edges. Fix coordinate \(v\), and split its
vertices into

\[
P_v=\{A:v\in A\},\qquad Q_v=\{A:v\notin A\}.
\]

Every wreath contains exactly \(m\) vertices of \(P_v\) and \(m+1\) of
\(Q_v\). A full-hypergraph matching saturating \(P_v\) has exactly

\[
|P_v|/m=t_m
\]

edges, hence covers \(nt_m=W\) middle vertices and is automatically a
perfect exact factor.

The proposed unoriented degrees are

\[
D_m=\frac{m!(m+1)!}{2},
\]

and, if \(|A\setminus B|=|B\setminus A|=d\),

\[
D_m(A,B)=d!^2(m-d)!(m+1-d)!,
\]

so

\[
\frac{D_m(A,B)}{D_m}
=\frac{2}{\binom md\binom{m+1}d}.
\]

For distinct \(A,B\in P_v\), \(d\le m-1\), and the proposed maximum is

\[
\max\frac{D_m(A,B)}{D_m}\le\frac2{m(m+1)}.
\tag{5}
\]

## Unproved hard-quota star lemma

Find an exact factor \(F=G\sqcup B\) with

\[
|B|=O(t_m/m)
\]

such that simultaneously at all controlled depths there are balanced
full-mass quotas satisfying (2). By (3), this implies MWB.

The raw heuristic is that (5) is the favorable scale for an almost-perfect
star-side matching. The unresolved requirements are global disjointness on
the \(Q_v\) side and near-covering/hard capacities at shallow lower ranks;
growing uniformity and the mean-one first shadow prevent direct use of a
standard nibble theorem.

